#Напишите программу, которая создаёт уменьшенную в три раза копию изображения. Получите горизонтальный и вертикальный зеркальный образ изображения.
# Сохраните изображения в текущую папку под новым именем.
from PIL import Image

def process_image(input_image_path):
    png = Image.open(input_image_path)

    width, height = png.size
    resized_img = png.resize((width // 3, height // 3))
    resized_img.save('resized_png.png')

    horizontal_mirror = png.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal_mirror.save('horizontal_privet.png')

    vertical_mirror = png.transpose(Image.FLIP_TOP_BOTTOM)
    vertical_mirror.save('vertical_privet.png')
    print("Изображения сохранены")

input_image_path = "C:/Users/AlexSash/Downloads/privet/privet.png"
process_image(input_image_path)
