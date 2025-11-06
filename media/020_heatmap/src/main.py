import os
import cv2
import numpy as np
import supervisely as sly
from supervisely.app.widgets import Card, Container, Heatmap, Text

# Create a sample background image with gradient
height, width = 400, 600
background = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    background[i, :] = [50 + i // 3, 100, 150 + i // 5]

# Create a sample heatmap mask (multiple Gaussian blobs)
y, x = np.ogrid[:height, :width]
# First blob
center_y1, center_x1 = height // 3, width // 3
mask1 = np.exp(-((x - center_x1) ** 2 + (y - center_y1) ** 2) / (2 * 80**2))
# Second blob
center_y2, center_x2 = 2 * height // 3, 2 * width // 3
mask2 = np.exp(-((x - center_x2) ** 2 + (y - center_y2) ** 2) / (2 * 60**2))
# Combine masks
mask = (mask1 + mask2 * 0.7) * 255
mask = mask.astype(np.float32)

# Static directory for storing images
static_dir = "static"

# Initialize Heatmap widget
heatmap = Heatmap(
    static_dir=static_dir,
    background_image=background,
    heatmap_mask=mask,
    vmin=0,
    vmax=255,
    transparent_low=True,
    colormap=cv2.COLORMAP_JET,
    width=600,
    height=400,
)

# Set initial opacity
heatmap.opacity = 70

# Create text widget to display click information
info_text = Text("Click on the heatmap to see values", status="info")

# Create app layout
card = Card(
    title="Heatmap Widget",
    description="Interactive heatmap overlay with click detection",
    content=Container([heatmap, info_text]),
)

app = sly.Application(layout=card, static_dir=static_dir)


@heatmap.click
def handle_heatmap_click(y: int, x: int, value: float):
    info_text.text = f"Clicked at position (x={x}, y={y}), value={value:.2f}"
