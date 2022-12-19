# Text

WIP

## Introduction

In this tutorial you will learn how to use `Text` widget in Supervisely app.

[Read this tutorial in developer portal.](https://developer.supervise.ly/app-development/apps-with-gui/button)

## Function signature

```python
Text(text=None, status="text", widget_id=None)
```

![default](https://user-images.githubusercontent.com/48913536/202175644-0dc9c62a-544c-4460-8efa-f9af66e0b14f.png)

## Parameters

| Parameters |                          Type                          |       Description        |
| :--------: | :----------------------------------------------------: | :----------------------: |
|    text    |                          str                           | determine displayed text |
|   status   | Literal["text", "info", "success", "warning", "error"] |       text status        |
| widget_id  |                          str                           |     id of the widget     |

### text

Determine displayed text.

**type:** `str`

**default value:** `None`

```python
button = Button(text="My text")
```

### status

Text status.

**type:** `str`

**default value:** `text`

```python
button_icon_gap_5 = Button(text="icon gap 5", icon="zmdi zmdi-play", icon_gap=5)
button_icon_gap_50 = Button(text="icon gap 50", icon="zmdi zmdi-play", icon_gap=50)
```

### widget_id

ID of the widget.

**type:** `str`

**default value:** `None`
