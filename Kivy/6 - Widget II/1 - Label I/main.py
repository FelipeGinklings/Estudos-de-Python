from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

import kivy
kivy.require('2.1.0')

kvcode = """
StackLayout:
    orientation: 'tb-lr'
    padding: 50
"""


class JanelaApp(App):

    def build(self):
        builder = Builder.load_string(kvcode)
        # Tamanho da fonte
        # self.add_lb(builder).font_size = 10
        # O meu ubuntu não possui nenhuma font
        # self.add_lb(builder).font_name = "Helvetica"
        # Bold
        # self.add_lb(builder).bold = True
        # Italic
        # self.add_lb(builder).italic = True
        # Cor
        # self.add_lb(builder, font_size=20).color = (.1, .2, .3, 1)
        # Disabled
        # self.add_lb(builder, font_size=30).disabled = True
        # Altura da linha
        txt = \
            """1 - aaa bbb ccc ddd
        2 - aaa bbb ccc ddd
        3 - aaa bbb ccc ddds
        4 - aaa bbb ccc ddd"""
        # x = self.add_lb(builder)
        # x.text = txt
        # x.line_height = 3
        # Número máximo de linhas (de baixo para cima)
        lb = self.add_lb(builder)
        lb.text = txt
        lb.color = (.9, .9, .1, 1)
        lb.max_lines = 3

        return builder

    def add_lb(self, builder, **args):
        lb = Label(text='Estudando a classe Label',
                   size_hint_y=None, height=50, markup=True, **args)
        builder.add_widget(lb)
        return lb


janela = JanelaApp()
janela.run()
