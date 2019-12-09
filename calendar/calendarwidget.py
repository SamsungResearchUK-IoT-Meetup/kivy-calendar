# File name: calendarwidget.py
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

import kivy
from kivy.uix.stacklayout import StackLayout
from kivy.properties import NumericProperty, ListProperty


class CalendarWidget(StackLayout):

    def view_final(self):
        print("**** Final view being exposed ****")

    def view_diagnostic(self):
        print("**** Diagnostic view being exposed ****")

    def color(self, instance):
        self.samsung_calendar.manager.current = 'colorscreen'
    def start(self):
        print("*********** colour function called **********")

#    def unselect_all(self):
#        for child in self.drawing_space.children:
#            child.unselect()

