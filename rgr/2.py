def f(x: float) -> float:
    return x**3 + 3 * x - 1


def df(x: float) -> float:
    return 3 * x**2 + 3


def newton_method(x0: float, eps: float) -> float:
    print("=== Метод Ньютона ===")
    print(f"Требуемая точность: eps = {eps}")
    print(f"Начальное приближение: x0 = {x0}\n")

    x_prev = x0
    step = 1
    while True:
        fx = f(x_prev)
        dfx = df(x_prev)
        x_curr = x_prev - fx / dfx
        diff = abs(x_curr - x_prev)

        print(f"Шаг {step}:")
        print(f"  x_{step - 1} = {x_prev:.6f}, f(x_{step - 1}) = {fx:.6f}")
        print(f"  x_{step} = x_{step - 1} - f(x_{step - 1}) / f'(x_{step - 1}) = {x_curr:.6f}")
        print(f"  Разность приближений |x_i - x_{{i-1}}| = {diff:.6f}")

        if diff <= eps:
            print("-" * 50)
            print(f"\nДостигнутая точность: {diff:.6f} <= eps ({eps})")
            print(f"Корень: x ~ {x_curr:.6f}")
            print(f"Значение функции в корне: f(x) ~ {f(x_curr):.6f}")
            print(f"Количество шагов: {step}\n")
            return x_curr

        print("-" * 50)
        x_prev = x_curr
        step += 1


def chord_method(a: float, b: float, eps: float) -> float | None:
    print("=== Метод хорд ===")
    print(f"Интервал: [{a}, {b}]")
    print(f"Требуемая точность: eps = {eps}\n")

    if f(a) * f(b) > 0:
        print("Ошибка: на концах интервала функция должна иметь разные знаки.")
        return None

    # Неподвижная точка для метода хорд выбирается там, где f(x)*f''(x) > 0
    # Вторая производная f''(x) = 6x.
    # f(0)=-1, f''(0)=0. f(1)=3, f''(1)=6. Знаки совпадают при x=1.
    def d2f(x: float) -> float:
        return 6 * x

    if f(a) * d2f(a) > 0:
        fixed = a
        curr = b
    else:
        fixed = b
        curr = a

    step = 1
    x_prev = curr

    while True:
        fx = f(x_prev)
        f_fixed = f(fixed)

        # Формула хорд, где одна точка (fixed) остается неподвижной
        x_curr = x_prev - fx * (fixed - x_prev) / (f_fixed - fx)
        diff = abs(x_curr - x_prev)

        print(f"Шаг {step}:")
        print(f"  x_{step - 1} = {x_prev:.6f}, f(x_{step - 1}) = {fx:.6f}")
        print(f"  x_{step} = {x_curr:.6f}")
        print(f"  Разность приближений |x_i - x_{{i-1}}| = {diff:.6f}")

        if diff <= eps:
            print("-" * 50)
            print(f"\nДостигнутая точность: {diff:.6f} <= eps ({eps})")
            print(f"Корень: x ~ {x_curr:.6f}")
            print(f"Значение функции в корне: f(x) ~ {f(x_curr):.6f}")
            print(f"Количество шагов: {step}\n")
            return x_curr

        print("-" * 50)
        x_prev = x_curr
        step += 1


if __name__ == "__main__":
    eps = 0.001

    # Решаем уравнение x^3 + 3x - 1 = 0
    # На отрезке [0, 1] есть корень, так как f(0) = -1 < 0, f(1) = 3 > 0

    newton_method(1.0, eps)
    chord_method(0.0, 1.0, eps)
