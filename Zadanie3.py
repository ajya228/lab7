#Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg. Напишите программу, которая применит ко всем этим файлам сразу любой
# фильтр (кроме размытия, т.к. он рассматривался на лекции). Сохраните изображения в новую папку под новыми именами.
from PIL import Image, ImageFilter
import os

output_folder = 'images_laba'
os.makedirs(output_folder, exist_ok=True)
filter = ImageFilter.CONTOUR

for i in range(1, 6):
    input_file = f'C:/Users/AlexSash/Downloads/{i}.jpg'
    output_file = os.path.join(output_folder, f'countoured_{i}.jpg')
    with Image.open(input_file) as img:
        processed_img = img.filter(filter)
        processed_img.save(output_file)

print("Изображения сохранены в папке images_laba.")
