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
QR_CODE_Y_POSITION = 350
FONT_SIZE = 40
TEXT_PADDING = 20
SPACE_BETWEEN_QR_CODES = 100


def create_qr_code_image(name, uuid):
  dynamic_url = f'https://www.sieclipse.com/download?uuid={uuid}'
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(dynamic_url)
  qr.make(fit=True)
  img = qr.make_image(fill_color="white", back_color="black").convert('RGBA')
  img = img.resize(QR_SIZE, Image.Resampling.LANCZOS)

  draw = ImageDraw.Draw(img)
  if os.path.exists("arial.ttf"):
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
  else:
    font = ImageFont.load_default()

  # Using textbbox to accommodate both TrueType and default fonts
  text_width, text_height = font.getsize(name) if hasattr(
      font, 'getsize') else (draw.textbbox(
          (0, 0), name, font=font)[2], draw.textbbox(
              (0, 0), name, font=font)[3])
  text_x_position = (QR_SIZE[0] - text_width) / 2
  text_y_position = QR_SIZE[1] + TEXT_PADDING
  draw.text((text_x_position, text_y_position), name, fill="black", font=font)

  return img


def main():
  os.makedirs(OUTPUT_FOLDER, exist_ok=True)

  with open(CSV_FILE, mode='r') as file:
    csv_reader = csv.DictReader(file)
    items = list(csv_reader)

  for i in range(0, len(items), 2):
    if i == len(items) - 1:
      # For an odd number of items, handle the last item separately if necessary
      continue

    duel_bg = Image.open(DUEL_BACKGROUND_IMAGE_PATH).convert('RGBA')
    qr_code1 = create_qr_code_image(items[i]['Company Name'], items[i]['UUID'])
    qr_code2 = create_qr_code_image(items[i + 1]['Company Name'],
                                    items[i + 1]['UUID'])

    total_width = QR_SIZE[0] * 2 + SPACE_BETWEEN_QR_CODES
    # Adjustments
    x1_adjustment = 460
    x2_adjustment = 1660

    start_x1 = (BACKGROUND_SIZE[0] - total_width) // 2 + x1_adjustment
    start_x2 = start_x1 + QR_SIZE[
        0] + SPACE_BETWEEN_QR_CODES + x2_adjustment - x1_adjustment
    y_position = QR_CODE_Y_POSITION

    duel_bg.paste(qr_code1, (start_x1, y_position), qr_code1)
    duel_bg.paste(qr_code2, (start_x2, y_position), qr_code2)

    output_filename = f'{OUTPUT_FOLDER}{items[i]["Company Name"]}_{items[i + 1]["Company Name"]}_combined.png'
    duel_bg.save(output_filename)


if __name__ == "__main__":
  main()
