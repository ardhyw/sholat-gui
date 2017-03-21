from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class RootWidget(BoxLayout):
    pass

class Gui(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Gui().run()
