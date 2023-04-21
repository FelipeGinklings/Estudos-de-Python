import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    atual = 0
    def textos(self):
        if self.atual == 1:
            self.text1 = self.ids.lb1.text
            self.text2 = self.ids.lb2.text
        
    def click(self):
        self.atual += 1
        if self.atual == 1:
            self.textos()
            self.ids.lb1.text = ''
            self.ids.lb2.text = '10'
        elif self.atual == 2:
            self.ids.lb1.text = self.text1
            self.ids.lb2.text = self.text2
            self.atual = 0

class Estudo4App(App):
    pass

janela = Estudo4App()
janela.run()