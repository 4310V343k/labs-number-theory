import math

# Для метода простой итерации уравнения приведены к виду:
# x = 0.5 * cos(y + 1)
# y = -0.4 - sin(x)


def phi_x(x, y):
    return 0.5 * math.cos(y + 1)


def phi_y(x, y):
    return -0.4 - math.sin(x)


def simple_iteration(x0, y0, eps, seidel=False):
    print(f"=== Метод { 'Зейделя' if seidel else 'простой итерации' } ===")
    print(f"Требуемая точность: eps = {eps}")
    print(f"Начальное приближение: x0 = {x0}, y0 = {y0}\n")

    x_prev, y_prev = x0, y0
    step = 1

    while True:
        x_curr = phi_x(x_prev, y_prev)
        y_curr = phi_y(x_curr if seidel else x_prev, y_prev)

        diff = max(abs(x_curr - x_prev), abs(y_curr - y_prev))

        print(f"Шаг {step}:")
        print(f"  x_{step - 1} = {x_prev:.6f}, y_{step - 1} = {y_prev:.6f}")
        print(f"  x_{step} = {x_curr:.6f}, y_{step} = {y_curr:.6f}")
        print(f"  Разность приближений = {diff:.6f}")

        if diff <= eps:
            print("-" * 50)
            print(f"\nТекущая разность приближений: {diff:.6f} <= eps ({eps})")
            print(f"Вектор решения: x ~ {x_curr:.6f}, y ~ {y_curr:.6f}")
            print(f"Количество шагов: {step}\n")
            return x_curr, y_curr

        print("-" * 50)
        x_prev, y_prev = x_curr, y_curr
        step += 1


# Для метода Ньютона уравнения приведены к виду f(x, y) = 0:
# f1(x, y) = 2x - cos(y + 1) = 0
# f2(x, y) = y + sin(x) + 0.4 = 0


def f1(x, y):
    return 2 * x - math.cos(y + 1)


def f2(x, y):
    return y + math.sin(x) + 0.4


# Частные производные (для матрицы Якоби)
def df1_dx(x, y):
    return 2.0


def df1_dy(x, y):
    return math.sin(y + 1)


def df2_dx(x, y):
    return math.cos(x)


def df2_dy(x, y):
    return 1.0


def newton_method(x0, y0, eps):
    print("=== Метод Ньютона (для систем) ===")
    print(f"Требуемая точность: eps = {eps}")
    print(f"Начальное приближение: x0 = {x0}, y0 = {y0}\n")

    x_prev, y_prev = x0, y0
    step = 1

    while True:
        F1 = f1(x_prev, y_prev)
        F2 = f2(x_prev, y_prev)
        
        # Определитель матрицы Якоби
        # J = [
        #   [df1/dx, df1/dy]
        #   [df2/dx, df2/dy]
        # ]

        J11 = df1_dx(x_prev, y_prev)
        J12 = df1_dy(x_prev, y_prev)
        J21 = df2_dx(x_prev, y_prev)
        J22 = df2_dy(x_prev, y_prev)

        detJ = J11 * J22 - J12 * J21
        if detJ == 0:
            print("Якобиан равен нулю. Метод расходится.")
            return None, None

        # Обратная матрица Якобиана:
        # J_inv = (1/detJ) * [
        #   [J22, -J12],
        #   [-J21, J11]
        # ]
        
        # Разность приближений: [dx, dy] = J_inv * [F1, F2]

        dx = (F1 * J22 - J12 * F2) / detJ
        dy = (J11 * F2 - F1 * J21) / detJ

        x_curr = x_prev - dx
        y_curr = y_prev - dy

        diff = max(abs(dx), abs(dy))

        print(f"Шаг {step}:")
        print(f"  x_{step - 1} = {x_prev:.6f}, y_{step - 1} = {y_prev:.6f}")
        print(f"  dx = {dx:.6f}, dy = {dy:.6f}")
        print(f"  x_{step} = {x_curr:.6f}, y_{step} = {y_curr:.6f}")
        print(f"  Разность приближений = {diff:.6f}")

        if diff <= eps:
            print("-" * 50)
            print(f"\nТекущая разность приближений: {diff:.6f} <= eps ({eps})")
            print(f"Вектор решения: x ~ {x_curr:.6f}, y ~ {y_curr:.6f}")
            print(
                f"Значения функций: f1 ~ {f1(x_curr, y_curr):.6f}, f2 ~ {f2(x_curr, y_curr):.6f}"
            )
            print(f"Количество шагов: {step}\n")
            return x_curr, y_curr

        print("-" * 50)
        x_prev, y_prev = x_curr, y_curr
        step += 1


if __name__ == "__main__":
    eps = 0.001

    # Начальное приближение взято из свободного члена уравнений
    # Альтернативно можно взять значения из грубой оценки, например:
    # x = 0.5 * cos(y+1) => x находится в [-0.5, 0.5]
    # y = -0.4 - sin(x) => y находится в [-1.4, 0.6]
    x0 = 0
    y0 = -0.4

    simple_iteration(x0, y0, eps)
    simple_iteration(x0, y0, eps, seidel=True)
    newton_method(x0, y0, eps)
