from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import date
from events import Event

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
        # Iterate through all widgets in events which is inside RelativeLayout calendar

        for widget in self.walk(restrict=False,loopback=False):
            if (type(widget)==Event):
                #print(type(widget))
                print("Widget ID's : {}".format(widget.ids))
                print("Widget ID: {} ".format(widget.id))
                print("Widget children: {}".format(widget.children))
                widget.text = "hello"
        # Place the days date into the correct widget based on the current month we are in. e.g. if we are in December 2019 then the 1st is on a Sunday which is widget number 7 in the grid layout.



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

        label_text = self.ids.month.text
        print("CalendarStatus month text: {}".format(label_text))

        label_text = self.parent.name
        print("CalendarStatus name: {}".format(label_text))

        label_text = self.parent.parent.ids._events.ids._e1.text
        print("CalendarStatus ids: {}".format(label_text))

        # using App.get_running_app()
        #app_ref = App.get_running_app()
        #print(app_ref.root, app_ref.root.ids.e1.text)

