import cv2
from PIL import Image
import matplotlib.pyplot as plt
from pdf417decoder import PDF417Decoder
from pyzbar.pyzbar import decode

# Load the image
image_path = "../data/IMG_1903 2.jpg"
npimg = cv2.imread(image_path)

if npimg is None:
    print("Error: Image not found or could not be loaded!")
    exit()

# Define the known barcode region {X=49, Y=33, Width=643, Height=175}
x, y, w, h = 49, 33, 643, 175
cropped_image = npimg[y:y+h, x:x+w]  # Crop barcode area

# Increase resolution (scale up)
scale_factor = 3  # 3x the original size
width = w * scale_factor
height = h * scale_factor
resized_image = cv2.resize(cropped_image, (width, height), interpolation=cv2.INTER_CUBIC)

# Convert to PIL format
image = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

# Display cropped and upscaled barcode
plt.imshow(image)
plt.title("Cropped & Upscaled Barcode")
plt.show()

# Try decoding using PDF417Decoder
print("Trying PDF417Decoder...")
decoder = PDF417Decoder(image)

if decoder.decode() > 0:
    print("Decoded using PDF417Decoder:")
    decoded_text = decoder.barcode_data_index_to_string(0)
    print(decoded_text)
else:
    print("PDF417Decoder failed to decode the barcode.")

# Try alternative decoder: pyzbar
print("\nTrying pyzbar decoder...")
decoded_objects = decode(resized_image)

if decoded_objects:
    for obj in decoded_objects:
        print("Decoded using pyzbar:")
        print(obj.data.decode("utf-8"))
else:
    print("pyzbar also failed to decode the barcode.")
