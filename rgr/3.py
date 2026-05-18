def simple_iteration(C, d, eps):
    n = len(d)

    # В качестве начального приближения берем свободный член (x0 = d)
    x_prev = d.copy()

    print("Начальное приближение:")
    print(f"  x_0 = {[round(v, 6) for v in x_prev]}\n")

    step = 1
    max_iter = 1000  # защита от бесконечного цикла

    while step <= max_iter:
        x_curr = [0.0] * n

        # Вычисляем x_k = C * x_{k-1} + d
        for i in range(n):
            s = sum(C[i][j] * x_prev[j] for j in range(n))
            x_curr[i] = s + d[i]

        # Находим норму разности (максимальное отклонение по модулю)
        diff = max(abs(x_curr[i] - x_prev[i]) for i in range(n))

        print(f"Шаг {step}:")
        print(f"  x_{step} = C * x_{step - 1} + d = {[round(v, 6) for v in x_curr]}")
        print(f"  Разность ||x_{step} - x_{step - 1}|| = {diff:.6f}")

        if diff <= eps:
            print("-" * 50)
            print(f"\nУсловие остановки выполнено: {diff:.6f} <= eps ({eps})")
            print(f"Вектор решения: x ~ {[round(v, 6) for v in x_curr]}")
            print(f"Количество шагов: {step}")
            return x_curr

        print("-" * 50)
        x_prev = x_curr
        step += 1

    print(
        f"\nМетод не сошелся за {max_iter} шагов. Возможно, нарушено условие сходимости ||C|| < 1."
    )
    return None


if __name__ == "__main__":
    eps = 0.001

    # Матрица C
    C = [
        [0.0, 0.1, -0.1, 0.2],
        [0.2, 0.0, -0.2, 0.1],
        [0.13, -0.2, 0.0, 0.3],
        [0.1, -0.1, -0.2, 0.0],
    ]

    # Вектор столбец d
    d = [-1.0, -1.0, 2.0, 0.1]

    print("=== Метод простой итерации (СЛАУ x = Cx + d) ===")
    print(f"Требуемая точность: eps = {eps}\n")

    simple_iteration(C, d, eps)
