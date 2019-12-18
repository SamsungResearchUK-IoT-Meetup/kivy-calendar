from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import datetime
from datetime import date, timedelta
from events import Event
from calendar import monthrange

# Fetch current date when calendarstatus starts
today = date.today()
set_date = date.today()
# Create a dictionary to map a day to a column. Used to calculate when to print 'date' onto an event.
col_day = {'Monday':1,'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday': 7}

class CalendarStatus(BoxLayout):

    def __init__(self, **kwargs):
        super(CalendarStatus, self).__init__(**kwargs)
        Clock.schedule_once(self.set_date_callback, 1)

    def set_date_callback(self, dt):
        print("Callback has been run")
        current_month = today.strftime("%B")
        current_year = today.strftime("%Y")
        current_day = today.strftime("%A")

        monthlabel = "[size=24px][color=#37abc8ff] {} [/color]".format(current_month)
        yearlabel = "[size=18px][color=#37abc8ff][i] {} [/i][/color]".format(current_year)
        self.cal_year.text = yearlabel
        self.cal_month.text = monthlabel

        # Calculate First day of current month
        monthrange_tuple = monthrange(today.year, today.month)
        first_day_of_month_num = monthrange_tuple[0]
        num_of_days_in_month = monthrange_tuple[1]

        # Loop over all monthly events. There are 42. But we only place a date onto an event beginning on the first day of the Month and count upwards.
        for idx, event in enumerate(self.parent.parent.ids._events.ids):
            print("\nindex is: {}  Event is: {}".format(idx, event))
            if (idx>=first_day_of_month_num) & (idx <= (first_day_of_month_num + num_of_days_in_month-1)):
                new_date_text = idx - first_day_of_month_num + 1
                print( "**** Start populating events **** Date: {}".format(new_date_text))
                print(" Current event text is: {}.".format(self.parent.parent.ids._events.ids[event].text))

                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(new_date_text)
            else:
                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(" ")


    def previous_month(self):
        print("You clicked the 'Previous Month' button")

        # Move the variable 'selected_date' into the previous month
        global set_date
        selected_date = set_date.replace(day=1)
        selected_date = selected_date - datetime.timedelta(days=1)

        # Calculate First day of previous month
        monthrange_tuple = monthrange(selected_date.year, selected_date.month)
        first_day_of_month_num = monthrange_tuple[0]
        num_of_days_in_month = monthrange_tuple[1]

        # This sets the 'Month' and 'Year' Labels at the top of the calendar status GUI element to the previous month
        selected_month = selected_date.strftime("%B")
        selected_year = selected_date.strftime("%Y")
        monthlabel = "[size=24px][color=#37abc8ff] {} [/color]".format(selected_month)
        yearlabel = "[size=18px][color=#37abc8ff][i] {} [/i][/color]".format(selected_year)
        self.cal_year.text = yearlabel
        self.cal_month.text = monthlabel

        # TODO make this iterator a function or method of the class. It's exactly the same for the set_date_callback, previous_month and next_month
        # Loop over all monthly events. There are 42. But we only place a date onto an event beginning on the first day of the Month and count upwards.
        for idx, event in enumerate(self.parent.parent.ids._events.ids):
            print("\nindex is: {}  Event is: {}".format(idx, event))
            if (idx>=first_day_of_month_num) & (idx <= (first_day_of_month_num + num_of_days_in_month-1)):
                new_date_text = idx - first_day_of_month_num + 1
                print( "**** Start populating events **** Date: {}".format(new_date_text))
                print(" Current event text is: {}.".format(self.parent.parent.ids._events.ids[event].text))

                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(new_date_text)
            else:
                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(" ")

        # Make sure you set the new set date to the previous month
        set_date = selected_date


        # for widget in self.walk(restrict=False,loopback=False):
        #     if (type(widget)==Event):
        #         #print(type(widget))
        #         print("Widget ID's : {}".format(widget.ids))
        #         print("Widget ID: {} ".format(widget.id))
        #         print("Widget children: {}".format(widget.children))
        #         widget.text = "hello"


    def next_month(self):
        print("You clicked the 'next month' button")

        # Move the variable 'selected_date' into the next month
        global set_date
        selected_date = set_date.replace(day=1)
        selected_date = selected_date + datetime.timedelta(days=32)
        selected_date = selected_date.replace(day=1)

        # Calculate First day of previous month
        monthrange_tuple = monthrange(selected_date.year, selected_date.month)
        first_day_of_month_num = monthrange_tuple[0]
        num_of_days_in_month = monthrange_tuple[1]

        # This sets the 'Month' and 'Year' Labels at the top of the calendar status GUI element to the previous month
        selected_month = selected_date.strftime("%B")
        selected_year = selected_date.strftime("%Y")
        monthlabel = "[size=24px][color=#37abc8ff] {} [/color]".format(selected_month)
        yearlabel = "[size=18px][color=#37abc8ff][i] {} [/i][/color]".format(selected_year)
        self.cal_year.text = yearlabel
        self.cal_month.text = monthlabel

        # TODO make this iterator a function or method of the class. It's exactly the same for the set_date_callback, previous_month and next_month
        # Loop over all monthly events. There are 42. But we only place a date onto an event beginning on the first day of the Month and count upwards.
        for idx, event in enumerate(self.parent.parent.ids._events.ids):
            print("\nindex is: {}  Event is: {}".format(idx, event))
            if (idx>=first_day_of_month_num) & (idx <= (first_day_of_month_num + num_of_days_in_month-1)):
                new_date_text = idx - first_day_of_month_num + 1
                print( "**** Start populating events **** Date: {}".format(new_date_text))
                print(" Current event text is: {}.".format(self.parent.parent.ids._events.ids[event].text))

                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(new_date_text)
            else:
                self.parent.parent.ids._events.ids[event].text = "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(" ")

        # Make sure you set the new set date to the previous month
        set_date = selected_date



        #print(app_ref.root, app_ref.root.ids.e1.text)

