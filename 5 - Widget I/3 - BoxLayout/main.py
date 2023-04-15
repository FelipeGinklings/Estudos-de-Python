from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import kivy
kivy.require('2.1.0')

kvcode = """
BoxLayout:
    orientation: "vertical"
    spacing: 50
    padding: 20
    Button:
        size_hint: 1., 1.
        text: "A"
    Button:
        size_hint: 1., 1.
        text: "B"
    Button:
        size_hint: 1., 1.
        text: "C"
"""


class JanelaApp(App):

    def build(self):
        builder = Builder.load_string(kvcode)
        builder.add_widget(  # type: ignore
            Button(text="X", size_hint=(1., 1.)))
        # if builder.orientation == 'horizontal': # type: ignore
        #     builder.orientation = 'vertical' # type: ignore
        # else:
        #     builder.orientation = 'horizontal ' # type: ignore
        return builder


janela = JanelaApp()
janela.root = glayout = Builder.load_string(kvcode)


# glayout.add_widget(Button(text="X", size_hint=(1., 1.))) # type: ignore

janela.run()
