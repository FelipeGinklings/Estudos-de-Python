from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


def click():
    print(ed.text)

def build():
    layout = FloatLayout()
    
    global ed
    ed = TextInput(text="Felipe Ginklings")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text="Clique Aqui")
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.x = 170
    bt.y = 150
    bt.on_press = click
    
    layout.add_widget(ed)
    layout.add_widget(bt)
    return layout

janela = App()
janela.title = "Felipe Ginklings"

from kivy.core.window import Window
Window.size = 600, 600

janela.build = build
janela.run()