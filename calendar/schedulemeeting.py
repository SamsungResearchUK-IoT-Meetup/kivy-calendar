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

from email.utils import parseaddr

from kivy.uix.stacklayout import StackLayout


def check_email(dirty_email_string):
    """
    Validate that the supplied string is a valid email address.

    Args:
        dirty_email_string: the string to check

    Returns:
        None if string is not valid, the cleaned string otherwise
    """
    email = dirty_email_string.strip()
    clean_email = parseaddr(email)
    if clean_email[1] == '':
        return None
    else:
        return clean_email[1]


def check_emails(dirty_emails_string):
    # Validate Num People. This is a list of emails separated via ';'. So we need split the text string into
    # a list, remove white space and then validate
    clean_list = []
    dirty_list = dirty_emails_string.split(';')

    for email in dirty_list:
        clean_email = check_email(email)
        if not clean_email:
            return False, dirty_list
        clean_list.append(clean_email)
    return True, clean_list


class ScheduleMeeting(StackLayout):
    def get_organiser(self):
        # TODO: Override
        return "Organiser"

    def process_calendar_event(self, calendar_event):
        # TODO: Override
        print(calendar_event)

    def start(self):
        validated = True
        calendarEvent = {
            "title": None,
            "location": None,
            "required_people": None,
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
        #calendarEvent['required_people'] = self.ids.required_people.text
        calendarEvent['optional_people'] = self.ids.optional_people.text
        calendarEvent['meeting_length'] = self.ids.slider_meeting_length.value
        calendarEvent['earliest_date'] = self.ids.earliest_date
        calendarEvent['latest_data'] = self.ids.latest_date
        calendarEvent['shedule_deadline'] = self.ids.schedule_deadline
        calendarEvent['priority'] = self.ids.slider_priority.value

        # Validate emails for 'required people' field
        cleaned_email = self.check_email(self.ids.required_people.text)
        if cleaned_email[0]:
            calendarEvent['required_people'] = cleaned_email[1]     # Place the cleaned list of emails into the dictionary
        else:
            self.ids.required_people.text = 'Illegal value, try: my.name@email.com'
            self.ids.required_people_label.text = '[color=#ff0000][b]Required people[/b][/color]'
            validated = False

        if validated:
            # Pass values to the agent to be calculated
            self.ids.required_people_label.text = '[b]Required people[/b]'
            print("Calculating best time for calendar invite...")
            #

        # TODO Pass this dictionary to the 'Calculate' event function
        # On response:  1) Capture output iCalendar events and place in a calendar event object.
        #               2) Allow the buttons to be activated in the calendarWidget.
