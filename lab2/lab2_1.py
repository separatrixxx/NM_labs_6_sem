import numpy as np
import sys
import matplotlib.pyplot as plt


def newton(x0, e):
    max_iter = 1000

    counter = 0

    for _ in range(max_iter):
        counter += 1

        f_x = np.log(x0 + 1) - 2*x0**2 + 1
        df_x = 1 / (x0 + 1) - 4*x0
        x1 = x0 - f_x / df_x

        if abs(x1 - x0) < e:
            return x1, counter

        x0 = x1

    return x0, counter

def iter(x0, e):
    max_iter = 1000

    counter = 0

    for _ in range(max_iter):
        counter += 1

        x1 = np.sqrt((np.log(x0 + 1) + 1) / 2)

        if abs(x1 - x0) < e:
            return x1, counter

        x0 = x1

    return x0, counter

def graf(eq1, eq2):
    x = np.linspace(-0.6, 1, 100)
    plt.figure(figsize=(10, 6), dpi=80)

    plt.plot(x, eq1(x), label='f1(x) = ln(x + 1)')
    plt.plot(x, eq2(x), label='f2(x) = 2x^2 - 1')

    plt.xticks(np.arange(-0.6, 1.1, 0.1))
    plt.yticks(np.arange(-1, 1, 0.1))

    plt.legend()

    plt.title('Графики уравнений')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():
    e = float(input())

    # equation = lambda x: np.log(x + 1) - 2 * (x ** 2) + 1
    eq1 = lambda x: np.log(x + 1)
    eq2 = lambda x:  2 * (x ** 2) - 1

    # graf(eq1, eq2)
    
    root_newton, counter_newton = newton(0.95, e)
    root_iter, counter_iter = iter(0.95, e)

    file_name = sys.argv[1]

    output_file_name = file_name.replace(".txt", "_answer.txt")
    with open(output_file_name, "w") as output_file:
        output_file.write(f"x by Newton: {root_newton}\n")
        output_file.write(f"Number of iterations: {counter_newton}\n")
        output_file.write(f"Dependence: {counter_newton / e}\n")
        output_file.write(f"x by iter: {root_iter}\n")
        output_file.write(f"Number of iterations: {counter_iter}\n")
        output_file.write(f"Dependence: {counter_iter / e}\n")

    print("Результаты записаны в файл:", output_file_name)

main()