import os, requests

import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import Card, Container, Docstring, Button


# for convenient debug, has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api()

button_list = Button(text="Set list example")
button_table = Button(text="Set table example")
button_checkboxes = Button(text="Set checkboxes example")
button_clean = Button(text="Clean content")
buttons_container = Container(
    widgets=[button_list, button_table, button_checkboxes, button_clean],
    direction="horizontal",
)

list_example = """<html>
<body>

<h2>Unordered List with Disc Bullets</h2>

<ul style="list-style-type:disc;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>  

</body>
</html>"""


table_example = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
}
th {
  text-align: left;
}
</style>
</head>
<body>

<h2>Left-align Headings</h2>
<p>To left-align the table headings, use the CSS text-align property.</p>

<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>

</body>
</html>"""

checkboxes_example = """<html>
<body>

<h2>Checkboxes</h2>
<p>The <strong>input type="checkbox"</strong> defines a checkbox:</p>

<form action="/action_page.php">
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label><br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>"""

docstring = Docstring(data=list_example)


card = Card(title="Docstring", content=Container([docstring, buttons_container]))
layout = Container(widgets=[card], direction="vertical")
app = sly.Application(layout=layout)


@button_list.click
def gmail_content():
    docstring.set_value(list_example)


@button_table.click
def gmail_content():
    docstring.set_value(table_example)


@button_checkboxes.click
def google_content():
    docstring.set_value(checkboxes_example)


@button_clean.click
def clear():
    docstring.set_value("")
