#Подготовьте любой графический файл для выполнения практической работы. Напишите программу, которая открывает и выводит этот файл на экран.
# Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.

from PIL import Image

# Открываем изображение
image_path = "C:/Users/AlexSash/Downloads/privet/privet.png"
image = Image.open(image_path)

# Получаем информацию об изображении
image_format = image.format
image_size = image.size
image_mode = image.mode


# Выводим информацию в консоль
print(f"Формат изображения: {image_format}")
print(f"Размер изображения: {image_size}")
print(f"Цветовая модель: {image_mode}")
image.show()