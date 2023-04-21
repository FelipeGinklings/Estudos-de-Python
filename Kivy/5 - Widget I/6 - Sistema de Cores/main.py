from kivy.app import App
from kivy.lang import Builder
# from kivy.utils import get_color_from_hex
import kivy

kivy.require('2.1.0')

kvcode = """
#:import C kivy.utils.get_color_from_hex

FloatLayout:
    Button:
        size_hint: .3, .3
        pos_hint: {'center_x':.5, 'center_y':.5}
        # background_color: 1, 1, .1, 1
        background_color: C("#ffffff")
        background_normal: ""
"""


class JanelaApp(App):

    def build(self):
        return Builder.load_string(kvcode)


janela = JanelaApp()
janela.run()
