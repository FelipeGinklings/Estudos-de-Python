from kivy.lang import Builder
from kivy.app import App
import kivy
kivy.require('2.1.0')

code = """
BoxLayout:
    Button:
        text: '1'
    Button:
        text: '2'
"""

# Builder.load_file()


class Estudo6App(App):
    def build(self):
        return Builder.load_string(code)


janela = Estudo6App()
janela.run()
