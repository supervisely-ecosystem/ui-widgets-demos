<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/12828725/182181033-d0d1a690-8388-472e-8862-e0cacbd4f082.png"/>  

# Hello, World!

</div>

[Read this tutorial in developer portal.](#)

## Introduction

In this tutorial you will learn how to create Supervisely apps with UI on pure python using Supervisely app engine and widgets.
We will create a simple "Hello, World!" app that will generate names using `Text` and `Button` widgets.

## Requirements

Install latest `supervisely` version to have access to all [available widgets](https://ecosystem.supervise.ly/docs/table) and `names` library for names generation

```
names # requires for names generation
supervisely
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
import names
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
layout = Card(
    title="Hello, World!", 
    content=Container([hello_msg, start_btn])
    )
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```

![App](https://user-images.githubusercontent.com/48913536/194583142-06d801c8-fe97-4429-9d9a-6bac720eefda.png)

### Handle button clicks

Use the decorator as shown below to handle button click. 
When we change `hello_msg.text` value, data will be pushed to web browser via web sockets.


```python
@start_btn.click
def generate_name():
    hello_msg.text = f"Hello, {names.get_first_name()}!"
```
![App demo](https://user-images.githubusercontent.com/48913536/194533336-6983fbd9-c6dc-4f44-867d-aec8526d9a64.gif)
