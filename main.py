import csv
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Constants - Adjust as needed
CSV_FILE = 'data.csv'
OUTPUT_FOLDER = 'qr_codes/'
DUEL_BACKGROUND_IMAGE_PATH = 'duel_code.png'
QR_SIZE = (300, 300)
BACKGROUND_SIZE = (1200, 1800)
QR_CODE_Y_POSITION = 600  # Adjust if needed for single background layout
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
  img = qr.make_image(fill_color="white", back_color="black").convert('RGBA')
  img = img.resize(QR_SIZE, Image.Resampling.LANCZOS)

  # Add name label below the code
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype(
      "arial.ttf",
      FONT_SIZE) if os.path.exists("arial.ttf") else ImageFont.load_default()
  text_y_position = QR_SIZE[1] + TEXT_PADDING
  text_position = (0, text_y_position)
  draw.text(text_position, name, fill="black", font=font)

  return img


def main():
  os.makedirs(OUTPUT_FOLDER, exist_ok=True)

  with open(CSV_FILE, mode='r') as file:
    csv_reader = csv.DictReader(file)
    items = list(csv_reader)

  for i in range(0, len(items), 2):
    # Handle last item if an odd number in the list
    if i == len(items) - 1:
      image = create_qr_code_image(items[i]['Name'], items[i]['Info'])
      output_filename = f'{OUTPUT_FOLDER}{items[i]["Name"]}_with_background.png'
      image.save(output_filename)
      continue

    # Process items in pairs for duel background
    duel_bg = Image.open(DUEL_BACKGROUND_IMAGE_PATH).convert('RGBA')

    for index, item in enumerate([items[i], items[i + 1]]):
      qr_code = create_qr_code_image(item['Name'], item['Info'])

      # Adjust the y-position for each QR code
      y_position_adjustment = -150  # Move up by 100 pixels

      # Determine the position for each QR code based on its index
      # If the index is even, place the QR code on the left side
      # If the index is odd, place the QR code on the right side
      if index % 2 == 0:  # Left side
        x_position = 715  # adjust as needed
      else:  # Right side
        x_position = 2325  # adjust as needed

      # Calculate the final y-position by adding the adjustment
      final_y_position = 500 + y_position_adjustment

      # Paste the QR code onto the duel background at the calculated position
      # The y-position is adjusted, but you can further adjust it as needed
      duel_bg.paste(qr_code, (x_position, final_y_position), qr_code)

    output_filename = f'{OUTPUT_FOLDER}{items[i]["Name"]}_{items[i + 1]["Name"]}_combined.png'
    duel_bg.save(output_filename)


if __name__ == "__main__":
  main()
