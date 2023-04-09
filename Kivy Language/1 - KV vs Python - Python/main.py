from kivy.uix.button import Button
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

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt1 = Button(text='Clique')
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text='bt2'))
        self.add_widget(Button(text='bt3'))


class Tela2(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root) # type: ignore
        janela.root_window.add_widget(Tela1()) # type: ignore

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text='Clique')
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPY(App):

    def build(self):
        return Tela1()


janela = KVvsPY()
janela.run()
