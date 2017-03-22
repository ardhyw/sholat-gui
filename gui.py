from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class RootWidget(BoxLayout):
    presets = {
            'Aceh':{0.6, 117},
            'Jakarta':{0.6, 117},
            'Semarang':{0.6, 117},
            'Surabaya':{0.6, 117},
            'Makassar':{0.6, 117}
            }
    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        self.ids['preset'].values = sorted(self.presets.keys())

class Gui(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Gui().run()
