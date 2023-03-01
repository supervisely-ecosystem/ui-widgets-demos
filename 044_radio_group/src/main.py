import supervisely as sly
from dotenv import load_dotenv
from supervisely.app.widgets import RadioGroup, Text, OneOf, Container, Card


items=[
    RadioGroup.Item(value="cat", label="Cat", content=Text(text='Cat says "Meow!"')), 
    RadioGroup.Item(value="dog", label="Dog", content=Text(text='Dot says "Woof!"')), 
    RadioGroup.Item(value="bird", label="Bird", content=Text(text='Bird says "Tweet!"')),
]

radio_group = RadioGroup(items=items, size="large")
one_of = OneOf(radio_group)

widgets = Container(
    widgets=[radio_group, one_of],
)

layout = Card(content=widgets, title="Radio group")
app = sly.Application(layout=layout)
