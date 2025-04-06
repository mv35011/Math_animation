# just run "manim -pqm subtract.py Subtraction" in the Terminal

from manim import *


class Subtraction(Scene):
    def construct(self):
        expr1 = Tex(r"$5 - 3 =$", font_size=96)

        result = Tex(r"$2$", font_size=96)

        result.next_to(expr1, RIGHT)

        self.add_sound("Animation Audio/Subtraction.mp3", gain=5)

        self.play(Write(expr1))
        self.wait(0.7)

        self.play(Write(result))
        self.wait(1)
