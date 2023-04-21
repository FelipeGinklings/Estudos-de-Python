from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
kivy.require('2.1.0')


class Tela1(BoxLayout):

    def on_press_bt(self):
        # Remove o widget que está na raiz da janela da raiz da janela
        janela.root_window.remove_widget(janela.root) # type: ignore
        # Adiciona o widget a raiz da janela
        janela.root_window.add_widget(Tela2()) # type: ignore


class Tela2(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root) # type: ignore
        janela.root_window.add_widget(Tela1()) # type: ignore


class KVvsPY2(App):
    pass
    # def build(self):
    #     return Tela1()


janela = KVvsPY2()
janela.run()
