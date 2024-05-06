from kivy.app import App
from kivy.uix.label import Label 


class MinhaApp(App):
    def build(self):
        return Label(
        text='Olá, SENAI',
        haling='left',  #Alinha o texto á esquerda
        valing='top'    #Alinha o texto no topo
        size_hint=(None,None),  #Desativa ajuste automatico
        seise=(150, 50),     #Define o tamanho do rotulo
        text_size=(150,None) #Define a largura máxima do texto
        )
    
if __name__ == "__main__":
    MinhaApp().run()
