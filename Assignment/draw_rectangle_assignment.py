import cv2  # Import OpenCV library

# Read the image
image = cv2.imread('../Basic_Operations/assignment-001-given.jpg')

# Coordinates for your region of interest
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
