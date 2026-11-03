"""A basic calculator and a visible brute-force linear equation solver."""

import math


def _read_number(prompt: str) -> float:
    """Read a finite number, prompting again when the input is invalid."""
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if math.isfinite(number):
            return number
        print("Please enter a finite number.")


def basic_calculate() -> float:
    """Prompt for two numbers and an arithmetic operation, then return the result."""
    first = _read_number("First number: ")
    operator = input("Operation (+, -, *, /): ").strip()
    second = _read_number("Second number: ")

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = first / second
    else:
        raise ValueError("Unsupported operation. Choose +, -, *, or /.")

    print(f"Result: {result}")
    return result


def _validate_equation_values(a: float, b: float, c: float) -> None:
    if not all(math.isfinite(value) for value in (a, b, c)):
        raise ValueError("Equation coefficients must be finite numbers.")


def _search_for_x(a: float, b: float, c: float, *, show_attempts: bool) -> float:
    _validate_equation_values(a, b, c)

    best_x = -100.0
    best_error = math.inf

    for step in range(-1000, 1001):
        x = step / 10
        error = abs((a * x + b) - c)

        if show_attempts:
            print(f"Trying x = {x:6.1f} | distance from zero: {error:.6g}")

        if error < best_error:
            best_x = x
            best_error = error

    return best_x


def solve_for_x(a: float, b: float, c: float) -> float:
    """Find the closest x in [-100, 100] for the equation a*x + b = c."""
    return _search_for_x(a, b, c, show_attempts=False)


def visualize_search(a: float, b: float, c: float) -> float:
    """Print every brute-force candidate and its equation error, then return the best x."""
    best_x = _search_for_x(a, b, c, show_attempts=True)
    best_error = abs((a * best_x + b) - c)
    print(f"Closest value: x = {best_x:.1f} (distance: {best_error:.6g})")
    return best_x


def equation_solver_menu() -> None:
    """Offer solving and search-visualization options for a*x + b = c."""
    while True:
        print("\nEquation solver (a*x + b = c)")
        print("1. Solve for x")
        print("2. Visualize the brute-force search")
        print("3. Return to the main menu")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            return
        if choice not in {"1", "2"}:
            print("Choose 1, 2, or 3.")
            continue

        a = _read_number("Enter a: ")
        b = _read_number("Enter b: ")
        c = _read_number("Enter c: ")

        if choice == "1":
            x = solve_for_x(a, b, c)
            error = abs((a * x + b) - c)
            print(f"Closest solution: x = {x:.1f} (distance: {error:.6g})")
        else:
            visualize_search(a, b, c)

def search_algorithms():
    print("\nSearch algorithms are systematic methods used to locate specific pieces of data within a structure collection or to explore a space of possible problem solutions.")


def main() -> None:
    """Run the calculator's main menu."""
    while True:
        print("\nSmart Calculator")
        print("1. Basic calculation")
        print("2. Equation solver")
        print("3. Search algorithms")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                basic_calculate()
            except (ValueError, ZeroDivisionError) as error:
                print(f"Calculation error: {error}")
        elif choice == "2":
            equation_solver_menu()
        elif choice == "3":
            search_algorithms()
        elif choice == "4":
            return
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()