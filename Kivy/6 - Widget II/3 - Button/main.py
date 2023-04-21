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
        # self.add_bt(builder).font_size = 30
        # O meu ubuntu não possui nenhuma font
        # self.add_bt(builder).font_name = 'consola'
        # Bold
        # self.add_bt(builder).bold = True
        # Italic
        # self.add_bt(builder).italic = True
        # Cor
        # self.add_bt(builder).color = .9, .5, .3, .1
        # Formatação
        # bt = self.add_bt(builder)
        # bt.markup = True
        # bt.text = "Esse [b]texto[/b] possui formatação"
        # Quando pressionado
        def click(self):
            bt.text = 'on_press'
        # Quando solto
        def fim_click(self):
            bt.text = 'on_release'
        bt = self.add_bt(builder)
        bt.bind(on_press=click)  # type: ignore
        bt.bind(on_release=fim_click)  # type: ignore
        return builder

    def add_bt(self, builder, **args):
        bt = Button(text='Estudando a classe Label',
                    size_hint_y=None, height=50, font_size=22, markup=True, **args)
        builder.add_widget(bt)
        return bt


janela = JanelaApp()
janela.run()
