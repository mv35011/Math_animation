# just run "manim -pqm plus.py Addition" in the Terminal

from manim import *


class Addition(Scene):
    def construct(self):
        expr1 = Tex(r"$2 + 3 =$", font_size=96)

        result = Tex(r"$5$", font_size=96)

        result.next_to(expr1, RIGHT)

        self.add_sound("Animation Audio/Addition.mp3", gain=5)

        self.play(Write(expr1))
        self.wait(0.65)

        self.play(Write(result))
        self.wait(1)
