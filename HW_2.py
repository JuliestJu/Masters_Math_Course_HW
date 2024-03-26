import numpy as np


def solve_system_matrix_method(A, b):
    try:
        # Розв'язуємо систему за допомогою оберненої матриці
        x = np.linalg.inv(A).dot(b)
        return x
    except np.linalg.LinAlgError:
        # Якщо матриця невирішувана (наприклад, немає оберненої матриці), повертаємо помилку
        return None

def solve_system_cramer_method(A, b):
    n = len(b)
    det_A = np.linalg.det(A)
    if det_A == 0:
        return None  # Матриця невирішувана
    x = np.zeros(n)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        x[i] = det_Ai / det_A
    return x

# Задання матриці коефіцієнтів A та вектора правих частин b
A = np.array([[-1, 1, 2], [0, -1, -3], [4, -3, 2]])
b = np.array([1, -4, 7])

# Викликаємо функцію для розв'язання системи
solution_matrix_method = solve_system_matrix_method(A, b)

if solution_matrix_method is not None:
    print("Розв'язок системи рівнянь (матричний метод):")
    print(solution_matrix_method)
else:
    print("Система рівнянь невирішувана.")


# Викликаємо функцію для розв'язання системи методом Крамера
solution_cramer_method = solve_system_cramer_method(A, b)

if solution_cramer_method is not None:
    print("Розв'язок системи рівнянь (метод Крамера):")
    print(solution_cramer_method)
else:
    print("Система рівнянь невирішувана.")