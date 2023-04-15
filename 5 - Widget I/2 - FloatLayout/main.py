from typing import Dict, Tuple
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import kivy
kivy.require('2.1.0')


def button(size_hint: Tuple, pos_hint: Dict, text: str = ''):
    bt = f"""
    Button:
        size_hint: {size_hint}
        pos_hint: {pos_hint}
        text: "{text}"
    """
    return bt


kvcode = """
FloatLayout:
    Button:
        size_hint: (.1, .1)
        pos_hint: {'x': 0, 'top': 1.}
        text: "A"
    Button:
        size_hint: (.2, .2)
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: "B"
    Button:
        size_hint: (.1,.1)
        pos_hint: {'y': 0, 'right': 1.}
        text: "C"
    Button:
        size_hint: None, None
        pos_hint: {'center_y': .7}
        x: 150
        width: 200
        height: 100
        text: "Absoluto"
"""


class JanelaApp(App):

    def build(self):
        return Builder.load_string(kvcode)


janela = JanelaApp()
janela.run()
