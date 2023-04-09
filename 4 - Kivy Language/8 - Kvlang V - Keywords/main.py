import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print('funcSelf')
Button.funcSelf = funcSelf  # type: ignore

class MinhaTela(BoxLayout):
        
    def funcRoot(self):
        print('funcRoot')

class Estudo5App(App):
    
    def funcApp(self):
        print('funcApp')

janela = Estudo5App()
janela.run()