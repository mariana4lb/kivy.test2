from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Button(text='Clique aqui', background_color=get_color_from_hex)

if __name__ == "__main__":
    MinhaApp().run()
