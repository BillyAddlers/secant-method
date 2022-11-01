input_x0 = float(input("Insert x0: "))
input_x1 = float(input("Insert x1: "))


def f(x):
    #     Function (x) is f(x) = x^3-x^2-x+1 = 0
    return x ** 3 - x ** 2 - x + 1


def find_x2(x0, x1):
    return x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))


iter_limit = 25
current_iter = 1
err_tolerance = 0.0001
state = True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x2 = 0
    while state:
        if f(input_x0) == f(input_x1):
            print("ERRNOENT: Divide by zero!@")
            break

        x2 = find_x2(input_x0, input_x1)
        print(f"Iteration-{current_iter}, x2 = {x2} and f(x2) = {f(x2)}")
        input_x0 = input_x1
        input_x1 = x2
        current_iter = current_iter + 1

        if current_iter > iter_limit:
            print("Equation is not Convergent!")
            break

        state = abs(f(x2)) > err_tolerance

    print(f"\n Required root is: {x2}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
