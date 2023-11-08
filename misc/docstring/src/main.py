import os

import pandas as pd
from dotenv import load_dotenv

import supervisely as sly
from supervisely.api.image_api import ImageApi  # we will use ImageApi class docstring as examples
from supervisely.app.widgets import Card, Container, Docstring

# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

docstring_example_1 = ImageApi.__doc__

docstring_example_2 = """<html>
<head>
<style>
table, th, td { border: 1px solid black; border-collapse: collapse; }
th, td { padding: 5px; }
th { text-align: left; }
</style>
</head>
<body>

<table>
  <tr> <th>Class name</th> <th>Images count</th> <th>Labels count</th> </tr>
  <tr> <td>Lemon</td> <td>6</td> <td>6</td> </tr>
  <tr> <td>Kiwi</td> <td>6</td> <td>20</td> </tr>
</table>
</body>
</html>"""


docstring_1 = Docstring(content=docstring_example_1)

docstring_2 = Docstring()
docstring_2.set_content(content=docstring_example_2, is_html=True)

card_1 = Card(title="Docstring example 1", content=docstring_1)
card_2 = Card(title="Docstring example 2", content=docstring_2)

layout = Container(widgets=[card_1, card_2])
app = sly.Application(layout=layout)
