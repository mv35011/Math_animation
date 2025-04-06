
from manim import *
class Addition(Scene):
    def construct(self):
                
        expr1 = Tex(r"$4 + 5$", font_size=96)
    
                
        full_expr = Tex(r"$4 + 5 = 9$", font_size=96)
    
        self.play(Write(expr1))
        self.wait(0.5)
        self.play(Transform(expr1, full_expr))
        self.wait()
    