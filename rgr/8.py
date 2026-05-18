import math


def df(x: float, y: float) -> float:
    return math.cos(math.sqrt(x * y * y))


def euler_method(
    x0: float, y0: float, x_start: float, x_end: float, steps: int
) -> tuple[list[float], list[float]]:
    print("=== Метод Эйлера ===")
    print(f"Начальное условие: y({x0}) = {y0}")
    print(f"Интервал: [{x_start}, {x_end}]")
    print(f"Количество шагов: N = {steps}\n")

    h = (x_end - x_start) / steps
    if x_start != x0:
        print(
            "Начальное условие задано в точке, отличной от начальной точки интервала.\n"
            "Пройдем от x0 до x_start с той же точностью для получения начального значения y(x_start).\n"
        )
        _, primed_y_values = euler_method(
            x0, y0, x0, x_start, int(abs((x_start - x0) / h))
        )
        new_y = primed_y_values[-1]
        print(f"\n=== Изменённое начальное условие ===")

        y_values = [new_y] + [0.0] * (steps)
    else:
        y_values = [y0] + [0.0] * (steps)
    x_values = [x_start + i * h for i in range(steps + 1)]
    dy_values = [0.0] * (steps)

    print(f"Шаг 0: x_0 = {x_values[0]:.6f}, y_0 ~ {y_values[0]:.6f}")
    for i in range(1, steps + 1):
        dy_values[i - 1] = df(x_values[i - 1], y_values[i - 1])
        y_values[i] = y_values[i - 1] + h * dy_values[i - 1]
        print(
            f"Шаг {i}: dy_{i - 1} = f(x_{i - 1}, y_{i - 1}) ~ {dy_values[i - 1]:.6f}, x_{i} = {x_values[i]:.6f}, y_{i} ~ {y_values[i]:.6f}"
        )

    return x_values, y_values


if __name__ == "__main__":
    x0 = 0.0
    y0 = 2.0
    t0 = 1.0
    T = 2.0
    N = 10

    euler_method(x0, y0, t0, T, N)
