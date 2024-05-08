from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video(source='/Users/maria/OneDrive/Mel.mp4')
    
if __name__ == "__main__":
    MinhaApp().run()
