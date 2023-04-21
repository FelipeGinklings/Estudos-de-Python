from kivy.app import App
from kivy.lang import Builder
import kivy
kivy.require('2.1.0')

kvcode = """
BoxLayout:
    Button:
        size_hint: (0.1, 0.1)
        # pos_hint: {'x': 0.3, 'top': 1.}
        text: 'A'
    Button:
        size_hint: (0.1, 0.1)
        # pos_hint: {'x': 0.3, 'top': 1.}
        text: 'A'
    Button:
        size_hint: (0.1, 0.1)
        # pos_hint: {'x': 0.3, 'top': 1.}
        text: 'A'
"""


class JanelaApp(App):

    def build(self):
        return Builder.load_string(kvcode)


janela = JanelaApp()
janela.run()
