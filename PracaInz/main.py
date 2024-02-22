import kivy
import backend
from backend import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

# tworzenie nowych okien
class Menu(Screen):
    pass
class Start(Screen):
    pass
class Raport(Screen):
    pass
class Dodaj(Screen):
    pass

class img(Image):
    pass




class MyApp(App):
    img_source = 'img.jpg'
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Start(name="start"))
        sm.add_widget(Raport(name="raport"))
        sm.add_widget(Dodaj(name="dodaj"))
        return sm
def pressed(self, instance):
    self.img_source = "bob.jpg"
    
if __name__ == '__main__':
    MyApp().run()


