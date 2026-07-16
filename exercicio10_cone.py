from manim import *
import numpy as np

class Exercicio10(Scene):
    def construct(self):

        titulo = Text(
            "Exercício 10 - Cone com Água e Óleo",
            font_size=38
        )

        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # -------------------------
        # Vértices do cone
        # -------------------------

        topo_esq = np.array([-2.5, 2.5, 0])
        topo_dir = np.array([2.5, 2.5, 0])
        vertice = np.array([0, -2.5, 0])

        # Borda superior

        boca = Arc(
            radius=2.5,
            start_angle=0,
            angle=PI,
            arc_center=np.array([0,2.5,0])
        )

        # Laterais

        lado1 = Line(topo_esq, vertice)
        lado2 = Line(topo_dir, vertice)

        cone = VGroup(
            boca,
            lado1,
            lado2
        )

        self.play(Create(cone))

        self.wait()

        # -------------------------
        # Água
        # -------------------------

        agua = Polygon(
            vertice,
            np.array([-1,0,0]),
            np.array([1,0,0]),
            fill_color=BLUE,
            fill_opacity=0.6,
            stroke_width=0
        )

        # -------------------------
        # Óleo
        # -------------------------

        oleo = Polygon(
            np.array([-2.5,2.5,0]),
            np.array([2.5,2.5,0]),
            np.array([1,0,0]),
            np.array([-1,0,0]),
            fill_color=YELLOW,
            fill_opacity=0.5,
            stroke_width=0
        )

        self.play(
            FadeIn(agua),
            FadeIn(oleo)
        )

        self.wait()

        # Linha divisória

        divisao = DashedLine(
            np.array([-1,0,0]),
            np.array([1,0,0]),
            color=WHITE
        )

        self.play(Create(divisao))

        # -------------------------
        # Textos
        # -------------------------

        txt_agua = Text(
            "Água",
            font_size=26,
            color=BLUE
        )

        txt_agua.move_to([0,-1.2,0])

        txt_oleo = Text(
            "Óleo",
            font_size=26,
            color=YELLOW
        )

        txt_oleo.move_to([0,1.2,0])

        self.play(
            Write(txt_agua),
            Write(txt_oleo)
        )

        self.wait()

        # -------------------------
        # Altura h
        # -------------------------

        altura = DoubleArrow(
            np.array([-3,-2.5,0]),
            np.array([-3,2.5,0]),
            color=RED
        )

        h = MathTex("h", color=RED)

        h.next_to(altura,LEFT)

        self.play(
            Create(altura),
            Write(h)
        )

        self.wait()

        # -------------------------
        # Raio R
        # -------------------------

        raio = DoubleArrow(
            np.array([0,2.8,0]),
            np.array([2.5,2.8,0]),
            color=GREEN
        )

        R = MathTex("R",color=GREEN)

        R.next_to(raio,UP)

        self.play(
            Create(raio),
            Write(R)
        )

        self.wait(2)

        explicacao = Text(
            "Inicialmente a água ocupa metade da altura do cone.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(explicacao))

        self.wait(3)

        self.play(FadeOut(explicacao))

        # ==================================================
        # TORNEIRA
        # ==================================================

        torneira = VGroup(

            Line(
                np.array([-0.2,-2.8,0]),
                np.array([0.5,-2.8,0])
            ),

            Line(
                np.array([0.5,-2.8,0]),
                np.array([0.5,-2.5,0])
            ),

            Circle(radius=0.08).move_to([0.5,-2.65,0])

        )

        self.play(Create(torneira))

        texto = Text(
            "Abrindo a torneira...",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(2)

        self.play(FadeOut(texto))

        # ==================================================
        # ÁGUA ESCOANDO
        # ==================================================

        jato = Line(
            vertice,
            vertice + DOWN*1.5,
            color=BLUE
        )

        self.play(Create(jato))

        self.wait()

        # ==================================================
        # NOVO NÍVEL DO ÓLEO
        # ==================================================

        novo_nivel = -0.8

        novo_oleo = Polygon(
            np.array([-2.5,2.5,0]),
            np.array([2.5,2.5,0]),
            np.array([0.65,novo_nivel,0]),
            np.array([-0.65,novo_nivel,0]),
            fill_color=YELLOW,
            fill_opacity=0.5,
            stroke_width=0
        )

        nova_divisao = DashedLine(
            np.array([-0.65,novo_nivel,0]),
            np.array([0.65,novo_nivel,0]),
            color=WHITE
        )

        self.play(

            agua.animate.set_opacity(0.15),

            ReplacementTransform(
                oleo,
                novo_oleo
            ),

            ReplacementTransform(
                divisao,
                nova_divisao
            ),

            run_time=4

        )

        self.wait()

        # Água desaparece completamente

        self.play(

            FadeOut(agua),
            FadeOut(jato),

            run_time=2

        )

        texto = Text(
            "Toda a água saiu do recipiente.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))
        self.wait(3)

        self.play(FadeOut(texto))

        texto = Text(
            "Agora resta apenas o óleo.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))

        self.wait(3)

        self.play(FadeOut(texto))

        self.play(

            Indicate(novo_oleo),

            run_time=2

        )

        self.wait()

        # ==================================================
        # RESOLUÇÃO MATEMÁTICA
        # ==================================================

        self.play(
            FadeOut(
                altura,
                h,
                raio,
                R,
                txt_agua,
                txt_oleo,
                torneira
            )
        )

        titulo = Text(
            "Resolução",
            font_size=38
        ).to_edge(UP)

        self.play(Write(titulo))

        # Volume inicial da água

        eq1 = MathTex(
            r"V=\frac{1}{3}\pi r^2h"
        )

        self.play(Write(eq1))
        self.wait(2)

        self.play(eq1.animate.shift(UP*0.8))

        eq2 = MathTex(
            r"V_{agua}=\frac{1}{8}V_{cone}"
            )

        self.play(Write(eq2))

        self.wait(3)

        self.play(
            FadeOut(eq1),
            FadeOut(eq2)
        )

        # Semelhança

        semelhanca = MathTex(
            r"\frac{r}{R}=\frac{x}{h}"
        )

        self.play(Write(semelhanca))

        self.wait(2)

        self.play(
            semelhanca.animate.shift(UP*0.8)
        )

        eq3 = MathTex(
            r"r=\frac{Rx}{h}"
        )

        self.play(Write(eq3))

        self.wait(3)

        self.play(
            FadeOut(eq3)
        )

        # Substituição

        eq4 = MathTex(
            r"V=\frac13\pi\left(\frac{Rx}{h}\right)^2x"
        )

        self.play(Write(eq4))

        self.wait(3)

        self.play(
            eq4.animate.shift(UP*0.8)
        )

        eq5 = MathTex(
            r"V=\frac13\pi R^2\frac{x^3}{h^2}"
        )

        self.play(Write(eq5))

        self.wait(3)

        self.play(
            FadeOut(eq5)
        )

        # Igualando os volumes

        eq6 = MathTex(
            r"\frac{x^3}{h^3}=\frac18"
        )

        self.play(Write(eq6))

        self.wait(3)

        self.play(
            eq6.animate.shift(UP*0.8)
        )

        eq7 = MathTex(
            r"x=\frac{h}{2}"
        )

        self.play(Write(eq7))

        self.wait(4)

        texto = Text(
            "Assim, inicialmente a água ocupa metade da altura.",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(texto))

        self.wait(3)

        self.play(FadeOut(texto))

        # ==================================================
        # CONCLUSÃO
        # ==================================================

        self.play(
            FadeOut(semelhanca),
            FadeOut(eq6),
            FadeOut(eq7)
        )

        resposta = MathTex(
            r"\text{Após a saída da água, o óleo ocupa uma nova altura.}"
        )

        resposta.scale(0.8)

        self.play(Write(resposta))

        self.wait(2)

        self.play(
            resposta.animate.to_edge(UP)
        )

        eq8 = MathTex(
            r"V_{\text{óleo}}=\frac12V_{\text{cone}}"
        )

        self.play(Write(eq8))

        self.wait(2)

        self.play(
            eq8.animate.shift(UP*0.8)
        )

        eq9 = MathTex(
            r"\boxed{x\approx0,79\,h}"
        )

        eq9.scale(1.4)

        self.play(Write(eq9), run_time=2)

        self.wait(2)

        caixa = SurroundingRectangle(
            eq9,
            color=YELLOW,
            buff=0.3
        )

        self.play(Create(caixa))

        self.play(
            Indicate(eq9),
            run_time=2
        )

        texto = Text(
            "Altura final do nível do óleo.",
            font_size=30
        ).next_to(eq9, DOWN)

        self.play(Write(texto))

        self.wait(4)

        self.play(
            FadeOut(eq8),
            FadeOut(resposta),
            FadeOut(texto)
        )

        resumo = VGroup(

            MathTex(r"\bullet\ \text{Cone de altura } h"),

            MathTex(r"\bullet\ \text{Água escoa completamente}"),

            MathTex(r"\bullet\ \text{O óleo ocupa o espaço restante}"),

            MathTex(r"\boxed{x\approx0,79h}")

        )

        resumo.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.6
        )

        self.play(
            ReplacementTransform(eq9, resumo)
        )

        self.wait(5)

        fim = Text(
            "Fim da resolução",
            font_size=36
        ).to_edge(DOWN)

        self.play(Write(fim))

        self.wait(3)

        self.play(
            FadeOut(resumo),
            FadeOut(fim),
            FadeOut(caixa),
            FadeOut(cone),
            FadeOut(novo_oleo),
            FadeOut(nova_divisao),
            FadeOut(titulo)
        )

        self.wait()