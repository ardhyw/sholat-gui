from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from datetime import date
from praytimes import PrayTimes
from kivy.clock import Clock

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
        self.ids['tanggal'].text = date.strftime(date.today(), "%a, %d %b %Y")
        Clock.schedule_once(self._do_hisab, 2)

    def _do_hisab(self, dt):
        self.do_hisab()

    def do_hisab(self):
        pt = PrayTimes(self.metode.text)

        # set offset jika ada
        if self.offset.text:
            offset = {}
            for name in PrayTimes.timeNames.keys():
                offset[name] = int(self.offset.text)
            pt.tune(offset)

        # dapatkan waktu sholat
        times = pt.getTimes(
                date.today(),
                (float(self.lgt.text), float(self.lat.text)),
                int(self.timezone.text)
                )

        # clear all children
        self.perhitungan.clear_widgets()
        self.perhitungan.add_widget(Label(text='Imsyak'))
        self.perhitungan.add_widget(Label(text='Subuh'))
        self.perhitungan.add_widget(Label(text='Terbit'))
        self.perhitungan.add_widget(Label(text='Dzuhur'))
        self.perhitungan.add_widget(Label(text='Ashar'))
        self.perhitungan.add_widget(Label(text='Maghrib'))
        self.perhitungan.add_widget(Label(text='Isya'))
        self.perhitungan.add_widget(Label(text=times['imsak']))
        self.perhitungan.add_widget(Label(text=times['fajr']))
        self.perhitungan.add_widget(Label(text=times['sunrise']))
        self.perhitungan.add_widget(Label(text=times['dhuhr']))
        self.perhitungan.add_widget(Label(text=times['asr']))
        self.perhitungan.add_widget(Label(text=times['maghrib']))
        self.perhitungan.add_widget(Label(text=times['isha']))

class Gui(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Gui().run()
