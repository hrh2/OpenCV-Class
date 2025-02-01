# PDF417 Barcode Decoder

This project extracts and decodes **PDF417 barcodes** from an image using **Python**. It first crops the barcode, increases resolution, and then applies multiple decoders to extract the text.

## 🚀 Features
- **Automatic Barcode Cropping** (Based on predefined coordinates)
- **Image Upscaling** (Enhances barcode readability)
- **PDF417 Barcode Decoding** (Using `pdf417decoder`)
- **Fallback Decoder** (Uses `pyzbar` if the first method fails)
- **Text Cleaning** (Removes unwanted characters for a clean output)

## 📦 Installation
Ensure you have Python installed, then install the dependencies:
```bash
pip install matplotlib pillow opencv-python pyzbar pdf417decoder
```

## 📂 Usage
1. **Place your barcode image** in `../data/IMG_1903 2.jpg`
2. **Run the script:**
   ```bash
   python barcode_decoder.py
   ```
3. **View the decoded text** in the terminal

## 📌 Expected Output
If successful, the script will output:
```plaintext
Decoded using PDF417Decoder:
1 1977 8 0003689 0 240228022034BAZIRAMWABO              Gabriel                  B                       C  CÒUq9 8ªªq) (á¥¥q ÄÄô ©ÿ â   VÄlÄ ÿ÷.A¦¢lÿW¤ 
À 
Ä 
Äÿÿa Ê111111j­9¡9%bE/¨C/ÁF$>FBÆ,=+ÁnnE*ÄÉ£EJW´
8)Ê8ý
I·ÉC,ÊL ;I*ãJD(
Fm  ¥ ª UABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

```

If `PDF417Decoder` fails, it will try `pyzbar` as an alternative.

## 🛠️ Troubleshooting
- **Got 'Image not found' error?**
  - Ensure the image path is correct.
- **Barcode not decoding?**
  - Try increasing `scale_factor` in the script.

## Try to remove unwanted Characters