import math


def f(x: float) -> float:
    return math.sin(x + math.pi / 3) - 0.5 * x


def bisection(g: callable, a: float, b: float, eps: float) -> float | None:
    print(f"Начальный интервал: [{a}, {b}]")
    print(f"Требуемая точность: eps = {eps}\n")

    if g(a) * g(b) > 0:
        print("Ошибка: на концах интервала функция должна иметь разные знаки.")
        return None

    step = 1
    while (b - a) / 2 > eps:  #
        c = (a + b) / 2
        fc = g(c)
        print(f"Шаг {step}:")
        print(f"  a = {a:.6f}, f(a) = {g(a):.6f}")
        print(f"  b = {b:.6f}, f(b) = {g(b):.6f}")
        print(f"  c = (a+b)/2 = {c:.6f}, f(c) = {fc:.6f}")
        print(f"  Достигнутая точность (b-a)/2 = {(b - a) / 2:.6f}")

        if fc == 0.0:
            print("  Найден точный корень!")
            return c
        elif g(a) * fc < 0:
            print("  f(a) и f(c) имеют разные знаки, новый интервал: [a, c]")
            b = c
        else:
            print("  f(b) и f(c) имеют разные знаки, новый интервал: [c, b]")
            a = c

        print("-" * 50)
        step += 1

    root = (a + b) / 2
    print(f"\nДостигнутая точность: {(b - a) / 2:.6f} <= eps ({eps})")
    print(f"Корень: x ~ {root:.6f}")
    print(f"Значение функции в корне: f(x) ~ {g(root):.6f}")
    print(f"Количество шагов: {step - 1}")
    return root


if __name__ == "__main__":
    # Выбираем начальный интервал [0, 2]
    # так как f(0) ~ 0.866 > 0, а f(2) ~ -0.905 < 0
    a = 0.0
    b = 2.0
    eps = 0.001

    bisection(f, a, b, eps)
