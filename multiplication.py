# just run "manim -pqm multiplication.py Multiplication" in the Terminal

from manim import *


class Multiplication(Scene):
    def construct(self):
        expr1 = Tex(r"$2 \times 3 =$", font_size=96)

        result = Tex(r"$6$", font_size=96)

        result.next_to(expr1, RIGHT)

        self.add_sound("Animation Audio/Multiplication.mp3", gain=5)

        self.play(Write(expr1))
        self.wait(0.77)

        self.play(Write(result))
        self.wait(1)
