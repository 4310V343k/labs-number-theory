import math

def dot(v1, v2):  # скаляpное произведение векторов
    return sum(x * y for x, y in zip(v1, v2))

def norm(v):  # норма вектора
    return math.sqrt(dot(v, v))

def normalize(v):  # нормализация вектора
    n = norm(v)
    return [x / n for x in v]

def mult_matrix_vector(A, v):  # умножение матрицы на вектор
    return [dot(A[i], v) for i in range(len(A))]

def power_method(A: list[list[float]], eps: float) -> list[float]:
    n = len(A)
    v = [1.0] * n  # начальное приближение
    v = normalize(v)
    
    max_iter = 1000  # защита от бесконечного цикла
    prev_ev = 0
    for step in range(1, max_iter + 1):
        Av = mult_matrix_vector(A, v)
        ev = dot(v, Av)

        v = normalize(Av)
        diff = abs(ev - prev_ev)
        prev_ev = ev

        print(f"Шаг {step}:")
        print(f"  Av = A * v = {[round(x, 6) for x in Av]}")
        print(f"  λ_{step} = v^T * Av = {ev:.6f}")
        print(f"  Разность ||λ_{step} - {f'λ_{step - 1}' if step > 1 else '0'}|| = {diff:.6f}")

        if diff < eps:
            print("-" * 50)
            print(f"\nУсловие остановки выполнено: {diff:.6f} <= eps ({eps})")
            print(f"Собственное значение: λ ~ {ev}")
            print(f"Собственный вектор: x ~ {[round(v, 6) for v in v]}")
            print(f"Количество шагов: {step}")
            return ev, v

    return prev_ev, v

def power_method_all(A: list[list[float]], eps: float) -> list[float]:
    print("=== Метод степеней ===")
    print(f"Требуемая точность: eps = {eps}")

    n = len(A)
    A = [row[:] for row in A]  # копия
    eigenvalues = []

    for step in range(n):
        print(f"\n=== Поиск собственного значения {step + 1} ===")
        eigenvalue, eigenvector = power_method(A, eps)
        eigenvalues.append(eigenvalue)

        # A_next = A - lambda * (v * v^T) / (v^T * v)
        for i in range(n):
            for j in range(n):
                A[i][j] -= eigenvalue * eigenvector[i] * eigenvector[j]

    print("\nНайденные собственные значения:")
    for i, eigenvalue in enumerate(eigenvalues):
        print(f"  λ_{i+1} = {eigenvalue}")

    return eigenvalues

if __name__ == "__main__":
    A = [
        [1.0, 2.0, -7.0],
        [2.0, 3.0, 4.0],
        [-7.0, 4.0, 5.0],
    ]
    
    power_method_all(A, 1e-6)
