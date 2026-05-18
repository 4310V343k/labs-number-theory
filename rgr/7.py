import math


def f(x: float) -> float:
    return (x + 1) / (2 + math.log(1 + x * x))


def simpson_method(a: float, b: float, eps: float, runge_rule=False) -> float:
    print(f"=== Метод Симпсона {'с поправкой Рунге' if runge_rule else ''} ===")
    print(f"Интервал: [{a}, {b}]")
    print(f"Требуемая точность: eps = {eps}\n")

    n = 2  # начальное количество разбиений (должно быть четным)
    step = 1

    while True:
        h = (b - a) / n

        x0 = f(a)
        x1 = 4 * sum(f(a + i * h) for i in range(1, n, 2))  # нечетные
        x2 = 2 * sum(f(a + i * h) for i in range(2, n - 1, 2))  # четные
        x3 = f(b)

        integral = (h / 3) * (x0 + x1 + x2 + x3)

        if step == 1:
            prev_integral = integral
            print(f"Шаг {step}: n = {n}, I_{step} ~ {integral:.6f}")
        else:
            diff = abs(integral - prev_integral)
            if runge_rule:
                diff /= 15  # поправка Рунге для метода Симпсона
            print(
                f"Шаг {step}: n = {n}, I_{step} ~ {integral:.6f}, {'(1/15)*' if runge_rule else ''}|I_{step} - I_{step - 1}| = {diff:.6f}"
            )

            if diff <= eps:
                print("-" * 50)
                print(f"\nДостигнутая точность: {diff:.6f} <= eps ({eps})")
                print(f"Приближенное значение интеграла: I ~ {integral:.6f}")
                print(f"Количество шагов: {step}\n")
                return integral

            prev_integral = integral

        print("-" * 50)
        n *= 2
        step += 1


if __name__ == "__main__":
    a = 1.0
    b = 2.0
    eps = 0.01

    simpson_method(a, b, eps)
    simpson_method(a, b, eps, runge_rule=True)
