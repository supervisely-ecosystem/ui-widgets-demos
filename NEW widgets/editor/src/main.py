import os
from dotenv import load_dotenv
import supervisely as sly
from supervisely.project.project_meta import ProjectMeta
from supervisely.app.widgets import Container, Editor, Text, Card, Button

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

editor = Editor('{ "value": 10 }')
show_lines_button = Button('Show line numbers', button_type='success')
hide_lines_button = Button('Hide line numbers', button_type='danger')
readonly_true_button = Button('Set readonly=True', button_type='success')
readonly_false_button = Button('Set readonly=False', button_type='danger')
get_text_button = Button('Get Text')
label = Text("")
label.hide()

card = Card(
    title="Editor",
    content=Container([editor, Container([
        show_lines_button, hide_lines_button, readonly_true_button, readonly_false_button
    ], direction='horizontal'), get_text_button, label], gap=5)
)
layout = Container(widgets=[card])

app = sly.Application(
    layout=layout
)

@show_lines_button.click
def show_lines():
    editor.show_line_numbers()

@hide_lines_button.click
def hide_lines():
    editor.hide_line_numbers()

@readonly_true_button.click
def readonly_true():
    editor.readonly = True

@readonly_false_button.click
def readonly_false():
    editor.readonly = False

@get_text_button.click
def get_text():
    label.show()
    label.text = editor.get_text()
