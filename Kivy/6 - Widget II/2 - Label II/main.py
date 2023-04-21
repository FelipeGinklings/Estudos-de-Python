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
        # ------------------------------------------#
        # txt = "Estudando a [b]classe[/b] Label"
        # txt = "Estudando a classe [i]Label[/i]"
        # txt = "[u]Estudando[/u] a classe Label"
        # txt = "[s]Estudando[/s] a classe Label"
        # txt = "Estudando [size=50]a [b]classe[/b][/size] Label"
        # txt = "[color=#ff3333]Estudando[/color] a classe Label"
        # txt = "Estudando [sup]classe[/sup] Label"
        txt = "Estudando [sub]classe[/sub] Label"
        self.add_lb(builder, markup=True).text = txt

        # ------------------------------------------#
        return builder

    def add_lb(self, builder, **args):
        lb = Label(size_hint_y=None, font_size=30, height=50, **args)
        builder.add_widget(lb)
        return lb


janela = JanelaApp()
janela.run()
