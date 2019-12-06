# File name: schedulemeeting.py
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

from kivy.uix.stacklayout import StackLayout

class ScheduleMeeting(StackLayout):

    def start(self):
        calendarEvent = {
            "title": None,
            "location": None,
            "num_people": None,
            "optional_people": None,    # TODO make this a list of email addresses that are checked and formatted
            "meeting_length": 0,
            "earliest_date": 0,         # TODO Make this a time date object
            "latest_date": 0,           # TODO Make this a time date object
            "schedule_deadline": 0,
            "priority": 0
        }

        print("You clicked the 'Start Schedule' button")
        calendarEvent['title'] = self.ids.title.text
        calendarEvent['location'] = self.ids.location.text
        calendarEvent['num_people'] = self.ids.num_people.text
        calendarEvent['optional_people'] = self.ids.optional_people.text
        calendarEvent['meeting_length'] = self.ids.slider_meeting_length.value
        calendarEvent['earliest_date'] = self.ids.earliest_date
        calendarEvent['latest_data'] = self.ids.latest_date
        calendarEvent['shedule_deadline'] = self.ids.schedule_deadline
        calendarEvent['priority'] = self.ids.slider_priority.value
        print("The calendar event for the title is now set to: {}".format(calendarEvent))

        # TODO Pass this dictionary to the 'Calculate' event function
        # On response:  1) Capture output iCalendar events and place in a calendar event object.
        #               2) Allow the buttons to be activated in the calendarWidget.



