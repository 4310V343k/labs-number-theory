def lagrange_interpolation(x: list[float], y: list[float], x0: float) -> float:
    n = len(x)
    result = 0.0

    print("=== Интерполяция полиномом Лагранжа ===")
    if len(x) != len(y):
        print("Ошибка: количество узлов и значений функции в них должно совпадать.")
        return None
    for i in range(n):
        print(f"x[{i}] = {x[i]}, f(x[{i}]) = {y[i]}")
        if x[i] == x0:
            print(
                f"Точка x0 совпадает с узлом x[{i}] = {x[i]}. "
                f"Результат: f({x0}) = {y[i]}"
            )
            return y[i]

    print(f"Точка для интерполяции: x0 = {x0}\n")

    for i in range(n):
        # Значение базисного многочлена L_i(x0)
        L_i = 1.0
        for j in range(n):
            # Вычисляем L_i(x0) = П_{j≠i} (x0 - x[j]) / (x[i] - x[j])
            if i != j:
                L_i *= (x0 - x[j]) / (x[i] - x[j])

        term = y[i] * L_i
        result += term

        print(f"L_{i}(x0) = {L_i:.6f}, вклад в результат L_{i} * f(x[{i}]): {term:.6f}")

    print(f"\nИнтерполированное значение в точке x0: f({x0}) = {result:.6f}")
    return result


if __name__ == "__main__":
    f = [(0.0, 11.0), (1.0, 12.0), (3.0, 13.0), (5.0, 11.0)]
    x = [point[0] for point in f]
    y = [point[1] for point in f]
    x0 = 2.0

    lagrange_interpolation(x, y, x0)
