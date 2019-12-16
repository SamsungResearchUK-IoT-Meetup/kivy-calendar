
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import date

# Fetch current date when calendarstatus starts
today = date.today()

class CalendarStatus(BoxLayout):

    def __init__(self, **kwargs):
        super(CalendarStatus, self).__init__(**kwargs)
        Clock.schedule_once(self.set_date_callback, 1)

    def set_date_callback(self, dt):
        print("Callback has been run")
        current_month = today.strftime("%B")
        current_year = today.strftime("%Y")

        monthlabel = "[size=24px][color=#37abc8ff] {} [/color]".format(current_month)
        yearlabel = "[size=18px][color=#37abc8ff][i] {} [/i][/color]".format(current_year)
        self.cal_year.text = yearlabel
        self.cal_month.text = monthlabel



    def previous_month(self):
        print("You clicked the 'Previous Month' button")


        # TODO call functions to redraw Labels of the calendar widget for the previous month.
        # calendarEvent['title'] = self.ids.title.text
        # calendarEvent['location'] = self.ids.location.text
        # calendarEvent['num_people'] = self.ids.num_people.text
        # calendarEvent['optional_people'] = self.ids.optional_people.text
        # calendarEvent['meeting_length'] = self.ids.slider_meeting_length.value
        # calendarEvent['earliest_date'] = self.ids.earliest_date
        # calendarEvent['latest_data'] = self.ids.latest_date
        # calendarEvent['shedule_deadline'] = self.ids.schedule_deadline
        # calendarEvent['priority'] = self.ids.slider_priority.value

    def next_month(self):
        print("You clicked the 'next month' button")
        # TODO call functions to redraw Labesl of the calendar widget for the next month.