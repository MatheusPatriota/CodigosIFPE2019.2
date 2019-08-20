from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class  Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='botao 1', font_size=30 )
        label = Label(text="texto 1", font_ize=30)
        box.add_widget(button)
        box.add_widget(label)
        return box


Test().run()