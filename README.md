# T-Shirt Overlay
A python script that takes t-shirt images and applies an overlay graphic to each of them at specified positions and scales.

## Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [Pillow library](https://pillow.readthedocs.io/en/stable/installation.html)

## Usage
The script uses two dictionaries to map t-shirt images to their corresponding overlay images and positions/scales.
- `overlay_images` - Dictionary that maps each t-shirt image to its corresponding overlay image
- `tshirt_positions_scale` - Dictionary that maps each t-shirt image to its corresponding position and scale

The script opens each t-shirt image, resizes the overlay image, positions it on the t-shirt image and saves the resulting image with a prefix "modified_".

## Example


### Dictionary that maps each t-shirt image to its corresponding overlay image

```python
overlay_images = {
    "mockups/tshirt1.jpg": "graphic/graphic.png",
    "mockups/tshirt2.jpg": "graphic/graphic.png",
    "mockups/tshirt3.jpg": "graphic/graphic_black.png",
    "mockups/tshirt4.jpg": "graphic/graphic.png"
}
```

### Dictionary that maps each t-shirt image to its corresponding position and scale.

```python
tshirt_positions_scale = {
    "mockups/tshirt1.jpg": ((781, 372), (490,490)),
    "mockups/tshirt2.jpg": ((2535, 1004), (1500,1500)),
    "mockups/tshirt3.jpg": ((1680, 1116), (580,580)),
    "mockups/tshirt4.jpg": ((618, 448), (791,791))
}
```