from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class MedidaApp(App):

    def build(self):
        return RootWidget()


MedidaApp().run()
