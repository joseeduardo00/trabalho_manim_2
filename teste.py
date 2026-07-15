from manim import *

class Teste(Scene):
    def construct(self):
        texto = Text("Olá, Manim!")
        self.play(Write(texto))
        self.wait(2)