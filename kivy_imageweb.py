from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://www.otempo.com.br/content/dam/otempo/editorias/entretenimento/2022/1/entretenimento-ursinho-pooh-1709145396.jpeg')
    
if __name__ == "__main__":
    MinhaApp().run()
