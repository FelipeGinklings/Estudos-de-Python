from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    ti = TextInput()
    ti.text = 'Hello'
    return ti

janela = App()
janela.build = build
janela.run()