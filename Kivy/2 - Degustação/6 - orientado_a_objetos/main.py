from kivy.app import App
from kivy.uix.label import Label


class MeuPrograma(App):

    def build(self):
        return Label(text='Meu Programa')


MeuPrograma().run()
