from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import kivy


kivy.require('2.1.0')

kvcode = """
StackLayout:
    orientation: 'tb-lr'
    Button:
        size_hint: .33, .1
        text: 'Add Stack'
        on_press: app.add_button()
"""


class JanelaApp(App):

    def build(self):
        return Builder.load_string(kvcode)
    
    def add_button(self):
        new_button = Button(text="New Stack", size_hint=(.33, .1), on_press=self.delete_it_self)
        self.root.add_widget(new_button) # type: ignore

    def delete_it_self(self, *args):
        self.root.remove_widget(self.root.children[0]) # type: ignore
        print('Is Working')

janela = JanelaApp()
janela.run()