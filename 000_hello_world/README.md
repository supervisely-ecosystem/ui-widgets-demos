# Hello, World!

![App](https://user-images.githubusercontent.com/48913536/194531508-52ae0e99-144f-49ec-a4fc-7e99b549eac0.png)

[Read this tutorial in developer portal.](#)

## Introduction

In this tutorial you will learn how to create Supervisely apps with UI on pure python using Supervisely app engine and widgets.
We will create a simple "Hello, World!" app that will generate names using `Text` and `Button` widgets.

[Supervisely widget collection](https://github.com/supervisely/supervisely/tree/master/supervisely/app/widgets) is growing everyday, as of version `v6.66.10` - 40+ widgets are available.

## Requirements

UI Widgets and new no-html app engine has been integrated in Supervisely version 6.63.0

```requirements.txt
supervisely>=6.63.0
```

## How to debug this tutorial

**Step 1.** Prepare `~/supervisely.env` file with credentials. [Learn more here.](https://developer.supervise.ly/getting-started/basics-of-authentication#how-to-use-in-python)


**Step 2.** Clone [repository](https://github.com/supervisely-ecosystem/ui-widgets-demos) with source code and create [Virtual Environment](https://docs.python.org/3/library/venv.html).

```bash
git clone https://github.com/supervisely-ecosystem/ui-widgets-demos
cd ui-widgets-demos
./create_venv.sh
```

**Step 3.** Open repository directory in Visual Studio Code.&#x20;

```bash
code -r .
```

**Step 4.** Start debugging `000_hello_world/src/main.py`&#x20;

## Hello, World! app

### Import libraries

```python
import os
import names  # requires for names generation
from dotenv import load_dotenv
import supervisely as sly
from supervisely.app.widgets import Button, Card, Container, Text
```

### Init API client

Init API for communicating with Supervisely Instance. First, we load environment variables with credentials:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
api = sly.Api()
```

### Initialize `Text` and `Button` widgets.

```python
hello_msg = Text(text="Hello, World!", status="text")
start_btn = Button(text="Generate Name", icon="zmdi zmdi-play")
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place 2 widgets that we've just created in the `Container` widget. Place order in the `Container` is also important, we want the "hello text" to be above the name generation button.

```python
card = Card(
    title="Hello, World!", 
    content=Container([hello_msg, start_btn]))
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

### Add button functionality

To assign name generation function on our button widget on click use decorator as shown below.

```python
@start_btn.click
def generate_name():
    hello_msg.text = f"Hello, {names.get_first_name()}!"
```
![App demo](https://user-images.githubusercontent.com/48913536/194533336-6983fbd9-c6dc-4f44-867d-aec8526d9a64.gif)
