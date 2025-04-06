# just run "manim -pqm division.py Division" in the Terminal

from manim import *


class Division(Scene):
    def construct(self):
        expr1 = Tex(r"$6 \div 3 =$", font_size=96)

        result = Tex(r"$2$", font_size=96)

        result.next_to(expr1, RIGHT)

        self.add_sound("Animation Audio/Division.mp3", gain=5)

        self.play(Write(expr1))
        self.wait(0.8)

        self.play(Write(result))
        self.wait(1)
