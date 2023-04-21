from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import string
import kivy
kivy.require('2.1.0')

kvcode = """
FloatLayout:
    Button:
        size_hint: 1., None
        height: 50
        pos_hint: {'x': 0, 'top': 1.}
        text: 'Adicionar letra'
        on_press: app.add_button()
    GridLayout:
        id: grid
        cols: 3
        rows: None
        row_default_height: 50
        row_force_default: True
        # col_default_width: 50
        # col_force_default: True
        pos_hint: {'x': 0, 'top': .90}
"""

alfabeto = list(string.ascii_lowercase)


class JanelaApp(App):
    proximo = 0

    def build(self):
        return Builder.load_string(kvcode)

    def add_button(self):
        self.root.ids.grid.add_widget(  # type: ignore
            Button(text=f"{alfabeto[self.proximo]}"))
        self.proximo += 1
        if self.proximo == len(alfabeto):
            self.proximo = 0


janela = JanelaApp()
janela.run()
