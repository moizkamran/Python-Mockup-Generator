from PIL import Image

# Dictionary that maps each t-shirt image to its corresponding overlay image
overlay_images = {
    "mockups/tshirt1.jpg": "graphic/graphic.png",
    "mockups/tshirt2.jpg": "graphic/graphic.png",
    "mockups/tshirt3.jpg": "graphic/graphic_black.png",
    "mockups/tshirt4.jpg": "graphic/graphic.png",
    "mockups/tshirt5.jpg": "graphic/graphic_black.png",
    "mockups/tshirt6.jpg": "graphic/graphic.png",
    "mockups/tshirt7.jpg": "graphic/graphic.png"
}


# Dictionary that maps each t-shirt image to its corresponding position and scale
tshirt_positions_scale = {
    "mockups/tshirt1.jpg": ((781, 372), (490,490)),
    "mockups/tshirt2.jpg": ((2535, 1004), (1500,1500)),
    "mockups/tshirt3.jpg": ((1680, 1116), (580,580)),
    "mockups/tshirt4.jpg": ((618, 448), (791,791)),
    "mockups/tshirt5.jpg": ((618, 448), (791,791)),
    "mockups/tshirt6.jpg": ((618, 448), (791,791)),
    "mockups/tshirt7.jpg": ((365, 498), (15,1506))
}

# Iterate over the t-shirt images
for tshirt_img, (position,scale) in tshirt_positions_scale.items():
    overlay_img = Image.open(overlay_images[tshirt_img])
    overlay_img = overlay_img.convert("RGBA")
    # Open the t-shirt image
    tshirt = Image.open(tshirt_img)
    overlay_img = overlay_img.resize(scale)
    # Position the overlay image at the desired location on the t-shirt image
    tshirt.paste(overlay_img, position, overlay_img)
    # Save the resulting image
    tshirt.save("modified_" + tshirt_img)
