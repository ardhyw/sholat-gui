from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from datetime import date
from praytimes import PrayTimes
from kivy.clock import Clock
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.properties import NumericProperty

class ListItemBtn(ListItemButton):
    index = NumericProperty()

    def __init__(self, **kw):
        super(ListItemBtn, self).__init__(**kw)
        self.index = kw['index']

class RootWidget(BoxLayout):
    presets = {
            'Aceh':(0.6, 117),
            'Jakarta':(0.6, 117),
            'Semarang':(0.6, 117),
            'Surabaya':(0.6, 117),
            'Makassar':(0.6, 117),
            'Depok':(-6.3949, 106.7982)
            }

    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)

        # preset data
        self.ids['preset'].values = sorted(self.presets.keys())

        # tanggal hari ini
        self.ids['tanggal'].text = date.strftime(date.today(), "%a, %d %b %Y")

        # auto load hisab for the first time
        Clock.schedule_once(self._do_hisab, 2)

        # prepare listview utk running text profile
        args_converter = lambda rowindex, value: {'text':value, 'index':rowindex}
        self.list_adapter = ListAdapter(
                data=['tes':{},'2','3','4','5','6','7','8','9','10'],
                args_converter=args_converter,
                selection_mode='single',
                cls=ListItemBtn
                )
        self.list_adapter.bind(on_selection_change=self.do_show_profile)
        list_view = ListView(adapter=self.list_adapter)
        self.listview_container.add_widget(list_view)

    def do_show_profile(self, adapter):
        selected = adapter.selection[0].index
        data = adapter.data[]

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
        if self.lgt.text and self.lat.text:
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

    def do_preset(self):
        pos = self.presets[self.preset.text]
        self.lgt.text = str(pos[0])
        self.lat.text = str(pos[1])
        self.do_hisab()

class Gui(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Gui().run()
