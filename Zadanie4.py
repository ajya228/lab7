#Напишите программу, которая добавляет на изображение водяной знак. Можно тоже применять сразу к нескольким изображениям.

from PIL import Image
import os

watermark_path = 'C:/Users/AlexSash/Downloads/watermark.png'
output_folder = 'watermark_image'
os.makedirs(output_folder, exist_ok=True)
watermark = Image.open(watermark_path).convert("RGBA")

input_file = 'C:/Users/AlexSash/Downloads/privet/privet.png'
output_file = os.path.join(output_folder, f'watermarked_privet.png')

with Image.open(input_file).convert("RGBA") as img:
    width, height = img.size
    watermark_width, watermark_height = watermark.size
    position = (width - watermark_width - 0, height - watermark_height - 0)
    combined = Image.new("RGBA", img.size)
    combined.paste(img, (0, 0))
    combined.paste(watermark, position, watermark)
    combined.convert("RGB").save(output_file)

print("Изображения сохранены в папке.")
