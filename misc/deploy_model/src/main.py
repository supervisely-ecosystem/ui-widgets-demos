import os
import threading
import time
import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Button, Text, DeployModel, Flexbox

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

# Get team_id from environment
team_id = sly.env.team_id()
workspace_id = sly.env.workspace_id()
# Initialize DeployModel widget with all modes
# You can customize modes: modes=["connect"], modes=["pretrained"], modes=["custom"]
# or any combination: modes=["connect", "pretrained"]
deploy_model = DeployModel(api=api, team_id=team_id, modes=["connect", "pretrained", "custom"])

# Create info text widgets to display information
info_text = Text("", status="text")
info_text.hide()

model_info_text = Text("", status="text")
model_info_text.hide()

# Create buttons to interact with the widget
get_params_button = Button("Get Deploy Parameters", icon="zmdi zmdi-info")
load_pretrained_button = Button("Load Pretrained (YOLOv8n)", icon="zmdi zmdi-download")
get_model_info_button = Button("Get Model Info", icon="zmdi zmdi-info-outline")
get_model_info_button.hide()

buttons_container = Flexbox(
    [get_params_button, load_pretrained_button, get_model_info_button], gap=10
)

# Create main card
card = Card(
    title="Deploy Model Widget Demo",
    description="This widget allows you to deploy or connect to models in three modes: Connect, Pretrained, Custom.",
    content=Container([deploy_model, buttons_container, info_text, model_info_text], gap=20),
)

layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@get_params_button.click
def show_deploy_params():
    """Show current deployment parameters based on selected mode and options"""
    try:
        params = deploy_model.get_deploy_parameters()
        mode = params.get("mode", "unknown")

        # Format the output based on mode
        if mode == "connect":
            session_id = params.get("session_id")
            info_text.set(f"<b>Mode:</b> Connect<br><b>Session ID:</b> {session_id}", status="info")
        elif mode == "pretrained":
            framework = params.get("framework")
            model_name = params.get("model_name")
            agent_id = params.get("agent_id")
            info_text.set(
                f"<b>Mode:</b> Pretrained<br>"
                f"<b>Framework:</b> {framework}<br>"
                f"<b>Model:</b> {model_name}<br>"
                f"<b>Agent ID:</b> {agent_id}",
                status="info",
            )
        elif mode == "custom":
            experiment_info = params.get("experiment_info")
            agent_id = params.get("agent_id")
            if experiment_info:
                info_text.set(
                    f"<b>Mode:</b> Custom<br>"
                    f"<b>Task ID:</b> {experiment_info.get('task_id')}<br>"
                    f"<b>Agent ID:</b> {agent_id}",
                    status="info",
                )
            else:
                info_text.set(f"<b>Mode:</b> Custom<br><b>Agent ID:</b> {agent_id}", status="info")

        info_text.show()
    except Exception as e:
        info_text.set(f"<b>Error getting parameters:</b> {str(e)}", status="error")
        info_text.show()


@load_pretrained_button.click
def load_example_state():
    """Load example state - automatically select YOLOv8n segmentation model"""
    try:
        # Example: Load state to select a pretrained YOLOv8n segmentation model
        example_state = {
            "mode": "pretrained",
            "agent_id": None,
            "framework": "yolov8",
            "model_name": "yolov8n-seg",
        }
        deploy_model.load_from_json(example_state)
        info_text.set(
            "<b>Example state loaded successfully!</b><br>"
            "Mode: Pretrained<br>"
            "Model: YOLOv8n Segmentation<br>"
            "You can now select an agent and click Deploy.",
            status="success",
        )
        info_text.show()
    except Exception as e:
        info_text.set(f"<b>Error loading state:</b> {str(e)}", status="error")
        info_text.show()


@get_model_info_button.click
def show_model_info():
    """Show information about the currently deployed/connected model"""
    try:
        if deploy_model.model_api is None:
            model_info_text.set(
                "<b>No model is currently deployed or connected.</b><br>"
                "Please deploy or connect to a model first.",
                status="warning",
            )
            model_info_text.show()
            return

        # Get model information
        model_info = deploy_model.model_api.get_info()
        task_id = deploy_model.model_api.task_id

        model_name = model_info.get("model_name", "Unknown")

        model_info_text.set(
            f"<b>Model Information:</b><br>"
            f"<b>Session ID:</b> {task_id}<br>"
            f"<b>Model Name:</b> {model_name}",
            status="success",
        )
        model_info_text.show()
    except Exception as e:
        model_info_text.set(f"<b>Error getting model info:</b> {str(e)}", status="error")
        model_info_text.show()


def check_selection_state():
    """Monitor deployment status and selection state to enable/disable buttons"""
    while True:
        time.sleep(0.5)

        # Show/hide Get Model Info button based on deployment
        if deploy_model.model_api is not None:
            get_model_info_button.show()
        else:
            get_model_info_button.hide()
            model_info_text.hide()

        # Enable/disable Get Deploy Parameters button based on selection
        try:
            active_tab = deploy_model.tabs.get_active_tab()
            has_selection = False

            if active_tab == "Connect":
                # Check if Connect mode has any sessions and a selection
                connect_mode = deploy_model.modes.get(deploy_model.MODE.CONNECT)
                if connect_mode and hasattr(connect_mode, "sessions_table"):
                    selected_row = connect_mode.sessions_table.get_selected_row()
                    has_selection = selected_row is not None

            elif active_tab == "Pretrained":
                # Check if Pretrained mode has a model selected
                pretrained_mode = deploy_model.modes.get(deploy_model.MODE.PRETRAINED)
                if pretrained_mode and hasattr(pretrained_mode, "model_selector"):
                    try:
                        selected = pretrained_mode.model_selector.get_selected()
                        has_selection = selected is not None
                    except:
                        has_selection = False

            elif active_tab == "Custom":
                # Check if Custom mode has an experiment selected
                custom_mode = deploy_model.modes.get(deploy_model.MODE.CUSTOM)
                if custom_mode and hasattr(custom_mode, "experiment_table"):
                    try:
                        selected = custom_mode.experiment_table.get_selected_experiment_info()
                        has_selection = selected is not None
                    except:
                        has_selection = False

            # Enable or disable the button based on selection
            if has_selection:
                get_params_button.enable()
            else:
                get_params_button.disable()

        except Exception:
            # If any error occurs, keep button enabled to avoid breaking the UI
            get_params_button.enable()


# Start background thread to monitor deployment status and selection
monitor_thread = threading.Thread(target=check_selection_state, daemon=True)
monitor_thread.start()
