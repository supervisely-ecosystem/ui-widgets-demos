import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Hotkeys, Input, Text

load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

instructions = Text(
    text=(
        "Press <b>A</b>, <b>Ctrl+A</b>, <b>Ctrl+S</b>, or <b>Ctrl+Z</b> anywhere on this page.<br>"
        "Then click into one of the inputs below and press the same keys there &mdash; "
        "typing / selecting text always takes priority, so the hotkeys will NOT fire there."
    ),
    status="info",
)

status_text = Text(text="No hotkey pressed yet", status="text")
counter_text = Text(text="Presses: 0", status="text")

text_input = Input(placeholder="Single-line input: try 'a' or Ctrl+A here...")
textarea_input = Input(placeholder="Textarea: try the same here...", type="textarea")

hotkeys = Hotkeys(hotkeys=["a", "ctrl+a", "ctrl+s", "ctrl+z"])

layout = Card(
    title="Hotkeys",
    content=Container([instructions, status_text, counter_text, text_input, textarea_input, hotkeys]),
)

app = sly.Application(layout=layout)

press_count = 0

combo_to_label = {
    "a": ("text", "You pressed A"),
    "ctrl+a": ("info", "You pressed Ctrl+A (Select All)"),
    "ctrl+s": ("success", "You pressed Ctrl+S (Save)"),
    "ctrl+z": ("warning", "You pressed Ctrl+Z (Undo)"),
}


@hotkeys.key_pressed()
def on_hotkey_pressed(combo):
    global press_count
    press_count += 1
    status, label = combo_to_label.get(combo, ("text", f"You pressed: {combo}"))
    status_text.set(f"{label}!", status)
    counter_text.text = f"Presses: {press_count}"
