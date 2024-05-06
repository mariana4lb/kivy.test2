from kivy.app import App
from kivy.uix.label import Label 


class MinhaApp(App):
    def build(self):
        return Label(
        text='Olá, SENAI',
        haling='left', #alinha o texto á esquerda
        valing='top'  #alinha o texto no topo
        )
    
if __name__ == "__main__":
    MinhaApp().run()
