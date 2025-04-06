# This File generates simple math operation animations based on user inputs(without audio)
# run this as python main.py in the terminal

from manim import *
import subprocess
from typing import Tuple, Literal


class MathsGenerator:
    def __init__(self):
        self.file_name = "manim_file.py"
        self.operations = ["Multiplication", "Addition", "Subtraction", "Modulus", "Division"]

    def user_input(self) -> Tuple[float, float, str]:

        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print("/n Choose the operation")
                for i, op in enumerate(self.operations, 1):
                    print(f"{i}, {op}")
                op_length = len(self.operations)
                choice = int(input("/n Enter the number 1-5"))
                if choice < 1 or choice > op_length:
                    print("Enter a valid number between 1-5")
                    continue
                return num1, num2, self.operations[choice - 1]
            except ValueError:
                print("Value Error, Enter numeric Inputs")

    def generate_codes(self, num1: float, num2: float, op: str) -> None:
        num1_str = str(int(num1)) if num1 == int(num1) else str(num1)
        num2_str = str(int(num2)) if num2 == int(num2) else str(num2)

        op_symbols = {
            "Addition": "+",
            "Subtraction": "-",
            "Multiplication": "\\times",
            "Division": "\\div",
            "Modulus": "\\mod"
        }

        if op == "Addition":
            result = num1 + num2
        elif op == "Subtraction":
            result = num1 - num2
        elif op == "Multiplication":
            result = num1 * num2
        elif op == "Division":
            result = num1 / num2
        elif op == "Modulus":
            result = num1 % num2

        result_str = str(int(result)) if result == int(result) else str(result)

        code = f'''
from manim import *
class {op}(Scene):
    def construct(self):
                
        expr1 = Tex(r"${num1_str} {op_symbols[op]} {num2_str}$", font_size=96)
    
                
        full_expr = Tex(r"${num1_str} {op_symbols[op]} {num2_str} = {result_str}$", font_size=96)
    
        self.play(Write(expr1))
        self.wait(0.5)
        self.play(Transform(expr1, full_expr))
        self.wait()
    '''
        with open(self.file_name, 'w') as f:
            f.write(code)
            print(f"\\n Generated code for manim {op} of {num1} and {num2}")

    def run_manim_command(self, operation: str) -> None:
        command = f"manim render -p -ql {self.file_name} {operation}"
        print(f"\nRunning command: {command}")

        try:
            subprocess.run(command, shell=True, check=True)
            print(f"\nSuccessfully generated {operation} animation!")
        except subprocess.CalledProcessError as e:
            print(f"\nError running Manim command: {e}")

    def run(self) -> None:

        print("Welcome to Manim Math Animation Generator!")

        while True:
            num1, num2, operation = self.user_input()
            self.generate_codes(num1, num2, operation)

            self.run_manim_command(operation)

            continue_choice = input("\nDo you want to create another animation? (y/n): ").lower()
            if continue_choice != 'y':
                print("Thank you for using Math Animation Generator. Goodbye!")
                break


if __name__ == "__main__":
    generator = MathsGenerator()
    generator.run()
