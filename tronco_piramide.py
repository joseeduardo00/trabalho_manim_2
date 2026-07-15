from manim import *
import numpy as np

class TroncoPiramide(Scene):
    def construct(self):

        titulo = Text("Dedução da Fórmula do Volume do Tronco de Pirâmide", font_size=38)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # ---------- Pontos da base maior ----------
        A = np.array([-3, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([2, 2, 0])
        D = np.array([-2, 2, 0])

        # ---------- Vértice ----------
        V = np.array([0, 3, 0])

        # ---------- Base ----------
        base = Polygon(
            A, B, C, D,
            color=BLUE
        )

        # ---------- Arestas ----------
        arestas = VGroup(
            Line(V, A),
            Line(V, B),
            Line(V, C),
            Line(V, D)
        )

        piramide = VGroup(base, arestas)

        self.play(Create(base))
        self.play(Create(arestas))
        self.wait()

        texto = Text(
            "Considere uma pirâmide.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(2)

        self.play(FadeOut(texto))

        # ---------- Plano de corte ----------

        fator = 0.45

        A2 = V + fator * (A - V)
        B2 = V + fator * (B - V)
        C2 = V + fator * (C - V)
        D2 = V + fator * (D - V)

        base_menor = Polygon(
            A2, B2, C2, D2,
            color=GREEN
        )

        corte = DashedVMobject(
            Polygon(A2, B2, C2, D2),
            num_dashes=35
        )

        self.play(Create(corte))
        self.wait()

        texto = Text(
            "Fazemos um corte paralelo à base.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(2)

        self.play(FadeOut(texto))

        # ---------- Tronco ----------

        lados = VGroup(
            Polygon(A, B, B2, A2,
                    fill_color=YELLOW,
                    fill_opacity=0.35,
                    stroke_color=WHITE),

            Polygon(B, C, C2, B2,
                    fill_color=YELLOW,
                    fill_opacity=0.35,
                    stroke_color=WHITE),

            Polygon(C, D, D2, C2,
                    fill_color=YELLOW,
                    fill_opacity=0.35,
                    stroke_color=WHITE),

            Polygon(D, A, A2, D2,
                    fill_color=YELLOW,
                    fill_opacity=0.35,
                    stroke_color=WHITE)
        )

        self.play(
            FadeIn(base_menor),
            FadeIn(lados)
        )

        self.wait()

        texto = Text(
            "A parte inferior é o tronco da pirâmide.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)

        self.play(FadeOut(texto))

        # ==========================================================
        # IDENTIFICAÇÃO DAS BASES
        # ==========================================================

        label_B = MathTex("B", color=BLUE).next_to(base, DOWN)
        label_b = MathTex("b", color=GREEN).next_to(base_menor, UP)

        self.play(
            Write(label_B),
            Write(label_b)
        )

        self.wait(2)

        texto = Text(
            "Denotamos por B a área da base maior\n"
            "e por b a área da base menor.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto))

        # ==========================================================
        # ALTURA h
        # ==========================================================

        centro_base = base.get_center()
        centro_menor = base_menor.get_center()

        altura = DashedLine(
            centro_base,
            centro_menor,
            color=RED
        )

        label_h = MathTex("h", color=RED)

        label_h.next_to(
            altura,
            RIGHT
        )

        self.play(
            Create(altura),
            Write(label_h)
        )

        texto = Text(
            "A distância entre as bases é a altura h.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto))

        # ==========================================================
        # DESTACANDO A PIRÂMIDE MENOR
        # ==========================================================

        piramide_menor = VGroup(

            Polygon(
                A2,
                B2,
                C2,
                D2,
                color=GREEN,
                fill_opacity=0.15
            ),

            Line(V, A2),
            Line(V, B2),
            Line(V, C2),
            Line(V, D2)

        )

        self.play(
            Indicate(piramide_menor),
            run_time=2
        )

        texto = Text(
            "Observe que existe uma pirâmide menor\n"
            "semelhante à original.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto))

        # ==========================================================
        # MOSTRANDO AS DUAS PIRÂMIDES
        # ==========================================================

        self.play(
            piramide.animate.set_color(BLUE),
            piramide_menor.animate.set_color(GREEN),
            run_time=2
        )

        self.wait()

        texto = Text(
            "As duas pirâmides são semelhantes.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto))

        # ==========================================================
        # EQUAÇÕES
        # ==========================================================

        self.play(
            FadeOut(
                lados,
                altura,
                label_h,
                label_B,
                label_b,
                corte
            )
        )

        self.wait()

        eq1 = MathTex(
            r"V_{tronco}=V_{maior}-V_{menor}"
        )

        self.play(Write(eq1))
        self.wait(2)

        self.play(
            eq1.animate.to_edge(UP)
        )

        eq2 = MathTex(
            r"V=\frac{H\,B}{3}-\frac{x\,b}{3}"
        )

        self.play(Write(eq2))
        self.wait(3)

        # ==========================================================
        # SEMELHANÇA DAS PIRÂMIDES
        # ==========================================================

        self.play(
            FadeOut(eq2)
        )

        semelhanca = MathTex(
            r"\frac{x}{H}=\frac{\sqrt{b}}{\sqrt{B}}"
        )

        self.play(Write(semelhanca))
        self.wait(3)

        self.play(
            semelhanca.animate.to_edge(UP)
        )

        eq3 = MathTex(
            r"x=H\cdot\frac{\sqrt{b}}{\sqrt{B}}"
        )

        self.play(Write(eq3))
        self.wait(3)

        self.play(
            Transform(
                eq3,
                MathTex(
                    r"x=H\sqrt{\frac{b}{B}}"
                )
            )
        )

        self.wait(2)

        # ==========================================================
        # SUBSTITUIÇÃO NO VOLUME
        # ==========================================================

        self.play(
            FadeOut(eq3)
        )

        substituicao = MathTex(
            r"V=\frac{HB}{3}-\frac{H\sqrt{\frac{b}{B}}\,b}{3}"
        )

        self.play(Write(substituicao))
        self.wait(4)

        self.play(
            substituicao.animate.to_edge(UP)
        )

        simplifica = MathTex(
            r"V=\frac{H}{3}\left(B-\frac{b\sqrt{b}}{\sqrt{B}}\right)"
        )

        self.play(Write(simplifica))
        self.wait(4)

        # ==========================================================
        # RELAÇÃO ENTRE H E h
        # ==========================================================

        self.play(
            FadeOut(simplifica)
        )

        relacao = MathTex(
            r"h=H-x"
        )

        self.play(Write(relacao))
        self.wait(2)

        self.play(
            relacao.animate.to_edge(UP)
        )

        relacao2 = MathTex(
            r"h=H-H\sqrt{\frac{b}{B}}"
        )

        self.play(Write(relacao2))
        self.wait(3)

        self.play(
            Transform(
                relacao2,
                MathTex(
                    r"h=H\left(1-\sqrt{\frac{b}{B}}\right)"
                )
            )
        )

        self.wait(3)

        self.play(
            relacao2.animate.next_to(relacao, DOWN)
        )

        texto = Text(
            "Agora isolamos H.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(2)
        self.play(FadeOut(texto))

        H = MathTex(
            r"H=\frac{h}{1-\sqrt{\frac{b}{B}}}"
        )

        self.play(Write(H))
        self.wait(4)

        texto = Text(
            "Substituindo H na expressão do volume...",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)
        self.play(FadeOut(texto))

        # ==========================================================
        # LIMPEZA DA TELA
        # ==========================================================

        self.play(
            FadeOut(relacao),
            FadeOut(relacao2),
            FadeOut(H),
            FadeOut(semelhanca),
            FadeOut(eq1)
        )

        # ==========================================================
        # EXPRESSÃO FINAL
        # ==========================================================

        texto = Text(
            "Após substituir H e simplificar a expressão, obtemos:",
            font_size=30
        )

        texto.to_edge(UP)

        self.play(Write(texto))
        self.wait(2)

        formula = MathTex(
            r"V=\frac{h}{3}\left(B+b+\sqrt{Bb}\right)"
        )

        formula.scale(1.3)

        self.play(Write(formula), run_time=3)

        self.wait(2)

        # ==========================================================
        # DESTAQUE
        # ==========================================================

        caixa = SurroundingRectangle(
            formula,
            color=YELLOW,
            buff=0.25
        )

        self.play(Create(caixa))

        self.play(
            Indicate(formula, scale_factor=1.15),
            run_time=2
        )

        self.wait(2)

        texto2 = Text(
            "Esta é a fórmula do volume do tronco de pirâmide.",
            font_size=30
        )

        texto2.next_to(formula, DOWN)

        self.play(Write(texto2))

        self.wait(3)

        # ==========================================================
        # RESUMO
        # ==========================================================

        self.play(
            FadeOut(texto),
            FadeOut(texto2)
        )

        resumo = VGroup(

            MathTex(r"\bullet\ \text{Base maior: } B"),

            MathTex(r"\bullet\ \text{Base menor: } b"),

            MathTex(r"\bullet\ \text{Altura: } h"),

            MathTex(
                r"\boxed{V=\frac{h}{3}(B+b+\sqrt{Bb})}"
            )

        )

        resumo.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.6
        )

        self.play(ReplacementTransform(formula, resumo))

        self.wait(5)

        fim = Text(
            "Fim da demonstração",
            font_size=38
        )

        fim.to_edge(DOWN)

        self.play(Write(fim))

        self.wait(3)

        self.play(
            FadeOut(resumo),
            FadeOut(fim),
            FadeOut(caixa)
        )

        self.wait()