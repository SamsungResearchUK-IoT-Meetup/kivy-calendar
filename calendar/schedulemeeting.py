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
from datetime import timedelta
from email.utils import parseaddr

import arrow
from kivy.uix.stacklayout import StackLayout

TD_15MIN = timedelta(minutes=15)


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


def validate_datetime_field(dt_field):
    try:
        return arrow.get(dt_field.text)
    except arrow.arrow.parser.ParserError as pe:
        dt_field.text = "Invalid ISO DateTime String"
        raise pe


class ScheduleMeeting(StackLayout):
    def get_organiser(self):
        # TODO: Override
        return "Organiser"

    def process_calendar_event(self, calendar_event):
        # TODO: Override
        print(calendar_event)

    def start(self):
        validated = True

        calendar_event = {
            # Required
            "title": None,
            "length": None,
            "earliest": None,  # TODO Make this a time date object
            "latest": None,  # TODO Make this a time date object
            "required_attendees": None,
            "organiser": None,  # TODO make this a single email address that is checked and formatted

            # Optional
            "scheduling_deadline": None,  # TODO Make this a time date object
            "location": "",
            "optional_attendees": [],  # TODO make this a list of email addresses that are checked and formatted
            "priority": 0
        }

        print("You clicked the 'Start Schedule' button")
        ###################
        # Required fields #
        ###################
        calendar_event['title'] = self.ids.title.text
        calendar_event['length'] = self.ids.slider_meeting_length.value
        try:
            calendar_event['earliest'] = validate_datetime_field(self.ids.earliest_date)
        except arrow.arrow.parser.ParserError:
            validated = False
        try:
            calendar_event['latest'] = validate_datetime_field(self.ids.latest_date)
        except arrow.arrow.parser.ParserError:
            validated = False
        # Validate emails for 'required people' field
        valid, cleaned_emails = check_emails(self.ids.required_people.text)
        if valid:
            # Place the cleaned list of emails into the dictionary
            calendar_event['required_attendees'] = cleaned_emails
        else:
            self.ids.required_people.text = 'Illegal value, try: my.name@email.com'
            self.ids.required_people_label.text = '[color=#ff0000][b]Required people[/b][/color]'
            validated = False
        calendar_event["organiser"] = self.get_organiser()

        ###################
        # Optional fields #
        ###################
        if self.ids.schedule_deadline.text:
            try:
                calendar_event['scheduling_deadline'] = validate_datetime_field(self.ids.schedule_deadline)
            except arrow.arrow.parser.ParserError:
                validated = False
        calendar_event['location'] = self.ids.location.text
        # Validate emails for 'optional people' field if supplied
        if self.ids.optional_people.text:
            valid, cleaned_emails = check_emails(self.ids.optional_people.text)
            if valid:
                # Place the cleaned list of emails into the dictionary
                calendar_event['optional_attendees'] = cleaned_emails
            else:
                self.ids.optional_people.text = 'Illegal value, try: my.name@email.com'
                self.ids.optional_people_label.text = '[color=#ff0000][b]Optional people[/b][/color]'
                validated = False
        calendar_event['priority'] = self.ids.slider_priority.value

        ###########################
        # Sanity check validation #
        ###########################
        # Check earliest/latest times make sense
        if calendar_event['latest'] < calendar_event['earliest']:
            validated = False
            self.ids.latest_date.text = "Latest cannot come before earliest"
        # Check scheduling deadline is not after the latest date
        # TODO: Smarter check taking length of meeting into account
        if calendar_event['scheduling_deadline'] and calendar_event['latest'] < calendar_event['scheduling_deadline']:
            validated = False
            self.ids.schedule_deadline.text = "Scheduling deadline must be before latest"

        if validated:
            # Reset field labels
            self.ids.required_people_label.text = '[b]Required people[/b]'
            self.ids.optional_people_label.text = '[b]Optional people[/b]'

            # Pass values to the agent to be calculated
            print("Calculating best time for calendar invite...")
            self.process_calendar_event(calendar_event)

        # TODO Pass this dictionary to the 'Calculate' event function
        # On response:  1) Capture output iCalendar events and place in a calendar event object.
        #               2) Allow the buttons to be activated in the calendarWidget.
