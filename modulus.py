# just run "manim -pqm modulus.py Modulus" in the Terminal

from manim import *

class Modulus(Scene):
    def construct(self):
        expr1 = Tex(r"$7 \bmod 3 =$", font_size=96)
        result = Tex(r"$1$", font_size=96)

        result.next_to(expr1, RIGHT)


        self.add_sound("Animation Audio/Modulus.mp3", gain=5)


        self.play(Write(expr1))
        self.wait(0.7)


        self.play(Write(result))
        self.wait(1)
