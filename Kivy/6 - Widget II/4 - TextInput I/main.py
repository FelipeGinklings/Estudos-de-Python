from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
import kivy
kivy.require('2.1.0')

kvcode = """
FloatLayout:
    TextInput:
        id: text_input
        size_hint: None, None
        width: root.width
        height: root.height
"""


class JanelaApp(App):

    def build(self):
        builder = Builder.load_string(kvcode)
        ti = builder.ids.text_input # type: ignore
        ti.text = 'Linha1\nLinha2\nLinha3'
        # Somente leitura
        # ti.readonly = True
        #Fonte
        # ti.font_name = 'Arial'
        # Tamanho da fonte
        ti.font_size = 30
        # ti.foreground_color = .2,.5,.1,1
        # Tamanho horizontal da tecla tab
        # ti.tab_width = 4
        # Tecla tab desabilitada
        # ti.write_tab = False
        # Padding
        # ti.padding_x = 15
        # ti.padding_y = 30
        return builder 


janela = JanelaApp()
janela.run()