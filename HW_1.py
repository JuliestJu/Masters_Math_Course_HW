import cv2 as cv
import urllib
import numpy as np

# Функція для створення матриці перетворення з масштабуванням
def scaling_matrix(scale_x, scale_y):
    return np.array([[scale_x, 0], [0, scale_y]])

# Функція для створення матриці перетворення з обертанням на кут angle у градусах
def rotation_matrix(angle):
    angle_rad = np.radians(angle)
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)
    return np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

# Функція для створення матриці перетворення з переміщенням на dx по X і dy по Y
def translation_matrix(dx, dy):
    return np.array([[1, 0, dx], [0, 1, dy]])

# Вектор x
x = np.array([[2], [1]])

# Задання матриці для зменшення в 2 рази по вісі OX та збільшення в 3 рази по вісі OY
scaling_matrix_M1 = scaling_matrix(0.5, 3)

# Задання матриці для відображення відносно початку координат
reflection_matrix_M2 = np.array([[-1, 0], [0, -1]])

# Задання матриці для повороту на 60° по вісі OY
rotation_matrix_1_M4 = rotation_matrix(60)

# Задання матриці для повернення на 30°
rotation_matrix_2_M5 = rotation_matrix(30)

# Об'єднання матриць перетворень
combined_matrix = rotation_matrix_2_M5 @ rotation_matrix_1_M4 @ reflection_matrix_M2 @ scaling_matrix_M1

# Застосування об'єднаної матриці перетворення до вектора x
transformed_x = combined_matrix @ x

# Виведення результату
print("Transformed x:")
print(transformed_x)