# File name: samsungcalendar.py
"""
MIT License
Copyright (c) 2019 Samsung. n.herriot@samsung.com
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager

# Set Initial Window Size
Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '750')

# Load kivy files that describe the GUI
Builder.load_file('newmeetingstatus.kv')
Builder.load_file('schedulemeeting.kv')
Builder.load_file('calendarwidget.kv')
Builder.load_file('samsungcalendar.kv')
Builder.load_file('days.kv')
Builder.load_file('dates.kv')
Builder.load_file('months.kv')
Builder.load_file('select.kv')
Builder.load_file('calendar.kv')



class SamsungScreenManager(ScreenManager):
    pass


class SamsungScreenManagerApp(App):
    def build(self):
        return SamsungScreenManager()


if __name__ == "__main__":
    SamsungScreenManagerApp().run()
