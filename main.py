# MoonBunkerQrCodeProjectV1

import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Define constants for clarity
CSV_FILE = 'data.csv'
OUTPUT_FOLDER = 'qr_codes/'
BACKGROUND_IMAGE_PATH = 'background.png'
QR_SIZE = (300, 300)  # 1 inch x 1 inch at 300 DPI
BACKGROUND_SIZE = (1200, 1800)  # 4 inches x 6 inches at 300 DPI
QR_CODE_Y_POSITION = 600
FONT_SIZE = 40
TEXT_PADDING = 20

def create_qr_code_image(name, info):
    """Creates a QR code image with name label below it."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(info)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    img = img.resize(QR_SIZE, Image.Resampling.LANCZOS)
    background = Image.open(BACKGROUND_IMAGE_PATH).convert('RGBA')
    if background.size != BACKGROUND_SIZE:
        background = background.resize(BACKGROUND_SIZE, Image.Resampling.LANCZOS)
    x_position = (background.width - img.width) // 2
    position = (x_position, QR_CODE_Y_POSITION)
    background.paste(img, position, img)
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("arial.ttf", FONT_SIZE) if os.path.exists("arial.ttf") else ImageFont.load_default()
    text_position = (x_position, QR_CODE_Y_POSITION + QR_SIZE[1] + TEXT_PADDING)
    draw.text(text_position, name, fill="black", font=font)
    return background

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    with open(CSV_FILE, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['Name']
            info = row['Info']
            image = create_qr_code_image(name, info)
            output_filename = f'{OUTPUT_FOLDER}{name}_with_background.png'
            image.save(output_filename)

if __name__ == "__main__":
    main()

