from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text=" Menig ilk dasturlarim Odiljonov, matn ustiga bosing!  ")
       

TestApp().run()
