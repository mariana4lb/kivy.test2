from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source='/Users/aluno.sesipaulista/Pictures/bela e afera.jpg')
    
if __name__ == '__main__':
    MinhaApp().run()
