# Annotating an Image Using OpenCV

This README provides a step-by-step guide on how to annotate an image by adding a rectangle and text with a transparent background using OpenCV. Coordinates are determined using an Image Map Generator and reference image provided by the instructor.

## Dependencies
- Python 3.x
- OpenCV (`cv2`)

## Steps

1. **Determine Coordinates**: Use an Image Map Generator to get the coordinates of each object by referencing the solution image provided by the instructor.
2. **Read the Image**: The image is read using the `cv2.imread()` function.
3. **Draw the Rectangle**: A green-bordered rectangle is drawn to highlight the region of interest (ROI).
4. **Add the Text with Transparent Background**:
    - A little dark transparent box is drawn behind the text to simulate a background with adjustable transparency.
    - The text is centered within the transparent box and drawn in green color.

## Code Explanation with comments ( [annotate_img.py](annotate_img.py))
    
```python
import cv2  # Import OpenCV library

# Read the image
image = cv2.imread('../Basic_Operations/assignment-001-given.jpg')

# Coordinates for my region of interest
top_left_x, top_left_y = 989, 198
bottom_right_x, bottom_right_y = 261, 924

# Draw a green rectangle to show the ROI
cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 6)

# Coordinates for the  transparent box
box_top_left_x, box_top_left_y, box_bottom_right_x, box_bottom_right_y = 1266,194,809,73

# Calculate the text position and size
text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.2
thickness = 7
font_color = (0, 255, 0)  # Green

# Get text size
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

# Center the text within the box
text_x = box_top_left_x + (box_bottom_right_x - box_top_left_x - text_width) // 2
text_y = box_top_left_y + (box_bottom_right_y - box_top_left_y + text_height) // 2

# Create a copy of the image to draw the transparent box
overlay = image.copy()

# Draw the darker  transparent box
dark_color = (0, 0, 0)  # Darker  color (in BGR)
alpha = 0.4  # Transparency factor
cv2.rectangle(overlay, (box_top_left_x, box_top_left_y), (box_bottom_right_x, box_bottom_right_y), dark_color, -1)

# Blend the original image with the rectangle image
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# Add the green text on top of the darker  transparent box
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the updated image to a new file
cv2.imwrite('myResults.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()

