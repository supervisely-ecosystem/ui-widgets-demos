# Heatmap Chart

## Introduction

**`HeatmapChart`** widget in Supervisely is a widget used for displaying a heatmap chart. It allows users to visualize data in a way that highlights patterns and trends. Users can hover over each cell to see the data for that cell. The HeatmapChart widget is often used in data analysis and visualization tasks, such as exploring the distribution of object instances in a dataset.
`HeatmapChart` allows downloading data series from widget in `svg`, `png`, and `csv` formats.

[Read this tutorial in developer portal.](https://developer.supervisely.com/app-development/widgets/charts-and-plots/heatmapchart)

## Function signature

```python
HeatmapChart(
    title="Multiplication Table",
    data_labels=True,
    xaxis_title=None,
    color_range="row",
    tooltip=None,
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/218247387-621e000a-56ef-4b0a-9900-1ef8cd0ebf38.gif" alt="default" />
</p>

## Parameters

|  Parameters   |           Type            |                                Description                                |
| :-----------: | :-----------------------: | :-----------------------------------------------------------------------: |
|    `title`    |           `str`           |                           `HeatmapChart` title                            |
| `data_labels` |          `bool`           | Determines whether the values ​​in the `HeatmapChart` cells are displayed |
| `xaxis_title` |           `str`           |                               `X` axe title                               |
| `color_range` | `Literal["table", "row"]` |            Determines the color distribution on `HeatmapChart`            |
|   `tooltip`   |           `str`           |        Determines the displayed value in the `HeatmapChart` cells         |

### title

Determines `HeatmapChart` title.

**type:** `str`

### data_labels

Determines whether the values ​​in the `HeatmapChart` cells are displayed.

**type:** `bool`

**default value:** `true`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="",
    data_labels='False'
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![data_labels](https://user-images.githubusercontent.com/120389559/218247687-c27fcc47-16ab-40a5-a025-df8766dc5f42.gif)

### xaxis_title

Determines `X` axe title.

**type:** `str`

**default value:** `None`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="xaxis_title",
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![xaxis_title](https://user-images.githubusercontent.com/120389559/218247762-ea5506e9-c029-41cf-b976-d9d80aee8b09.png)

### color_range

Determines the color distribution on `HeatmapChart`.

**type:** `Literal["table", "row"]`

**default value:** `row`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="xaxis_title",
    color_range="table",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

![color_range](https://user-images.githubusercontent.com/120389559/220913004-f46fa248-3368-4be9-9bb4-0396ebffe56c.png)

### tooltip

Determines the displayed value in the `HeatmapChart` cells.

**type:** `str`

**default value:** `None`

```python
chart = HeatmapChart(
    title="Multiplication Table",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/218247998-6d6503a6-d5b4-4565-a4de-7aa0e96d52e1.gif" alt="tooltip" />
</p>

## Methods and attributes

|                    Attributes and Methods                    | Description                                                 |
| :----------------------------------------------------------: | ----------------------------------------------------------- |
|               `add_series_batch(series: dict)`               | Add batch of series to chart.                               |
| `add_series(name: str, x: list, y: list, send_changes=True)` | Add series of data in `HeatmapChart`.                       |
|                  `get_clicked_datapoint()`                   | Return data clicked in `HeatmapChart`.                      |
|                    `get_clicked_value()`                     | Return `seriesIndex` nad `dataPointIndex` for clicked cell. |
|                  `set_colors(colors: list)`                  | Set colors for series in chart.                             |
|                   `set_title(title: str)`                    | Set chart title.                                            |
|                           `@click`                           | Decorator function is handled when chart cell is clicked.   |

## Mini App Example

You can find this example in our Github repository:

[supervisely-ecosystem/ui-widgets-demos/charts-and-plots/002_heatmap_chart/src/main.py](https://github.com/supervisely-ecosystem/ui-widgets-demos/blob/master/charts-and-plots/002_heatmap_chart/src/main.py)

### Import libraries

```python
import os

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, HeatmapChart
```

### Init API client

First, we load environment variables with credentials and init API for communicating with Supervisely Instance:

```python
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()
```

### Initialize function to build example chart

```python
def multiplication_chart():
    data = []
    for row in list(range(1, 11)):
        temp = [round(row * number, 1) for number in list(range(1, 11))]
        data.append(temp)
    return data
```

### Initialize `HeatmapChart` widget

```python
chart = HeatmapChart(
    title="Multiplication Table",
    xaxis_title="",
    color_range="row",
    tooltip="Result multiplication of {x} * {series_name}",
)
```

### Add data to `HeatmapChart` widget

```python
data = multiplication_chart()

lines = [
    {"name": idx + 1, "x": list(range(1, 11)), "y": line}
    for idx, line in enumerate(data)
]

chart.add_series_batch(lines)
```

### Create app layout

Prepare a layout for app using `Card` widget with the `content` parameter and place widget that we've just created in the `Container` widget.

```python
card = Card(
    title="Heatmap Chart",
    content=Container([chart, text]),
)

layout = Container(widgets=[card])
```

### Create app using layout

Create an app object with layout parameter.

```python
app = sly.Application(layout=layout)
```


<p align="center">
  <img src="https://user-images.githubusercontent.com/120389559/218247387-621e000a-56ef-4b0a-9900-1ef8cd0ebf38.gif" alt="layout" />
</p>
