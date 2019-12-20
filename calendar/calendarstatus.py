import datetime
from calendar import monthrange
from datetime import date

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

# Create a dictionary to map a day to a column. Used to calculate when to print 'date' onto an event.
col_day = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}


class CalendarStatus(BoxLayout):

    def __init__(self, **kwargs):
        super(CalendarStatus, self).__init__(**kwargs)

        # Fetch current date when calendarstatus starts
        self.today = date.today()
        self.set_date = date.today()

        Clock.schedule_once(self.set_date_callback, 1)
        # self.set_date_callback(None)

    def set_date_callback(self, dt):
        print("Callback has been run")
        self._create_cal_view(self.today)

    def previous_month(self):
        print("You clicked the 'Previous Month' button")

        # Move the variable 'selected_date' into the previous month
        self.set_date = self.set_date.replace(day=1)  # Start of existing month
        self.set_date = self.set_date - datetime.timedelta(days=1)  # Back 1 month
        self.set_date = self.set_date.replace(day=1)  # Start of new month

        self._create_cal_view(self.set_date)

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
        self.set_date = self.set_date.replace(day=1)  # Start of existing month
        self.set_date = self.set_date + datetime.timedelta(days=32)  # Forward 1 month
        self.set_date = self.set_date.replace(day=1)  # Start of new month

        self._create_cal_view(self.set_date)

        # print(app_ref.root, app_ref.root.ids.e1.text)

    def _create_cal_view(self, selected_date):
        current_month = selected_date.strftime("%B")
        current_year = selected_date.strftime("%Y")

        monthlabel = "[size=24px][color=#37abc8ff] {} [/color]".format(current_month)
        self.cal_month.text = monthlabel

        yearlabel = "[size=18px][color=#37abc8ff][i] {} [/i][/color]".format(current_year)
        self.cal_year.text = yearlabel

        # Calculate First day of current month
        monthrange_tuple = monthrange(selected_date.year, selected_date.month)
        first_day_of_month_num = monthrange_tuple[0]
        num_of_days_in_month = monthrange_tuple[1]

        # Loop over all monthly events.
        # There are 42.
        # But we only place a date onto an event beginning on the first day of the Month and count upwards.
        for idx, event in enumerate(self.parent.parent.ids._events.ids):
            print("\nindex is: {}  Event is: {}".format(idx, event))
            if (idx >= first_day_of_month_num) & (idx <= (first_day_of_month_num + num_of_days_in_month - 1)):
                new_date_text = idx - first_day_of_month_num + 1
                print("**** Start populating events **** Date: {}".format(new_date_text))
                print(" Current event text is: {}.".format(self.parent.parent.ids._events.ids[event].text))

                self.parent.parent.ids._events.ids[event].text = \
                    "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(new_date_text)

                self.active_day_post_processing(date(selected_date.year, selected_date.month, new_date_text),
                                                self.parent.parent.ids._events.ids[event])
            else:
                self.parent.parent.ids._events.ids[event].text = \
                    "[size=10px][color=#37abc8ff][i]{}[/i][/color]".format(" ")

    def active_day_post_processing(self, day_date, event):
        # TODO: Override
        print("Day: {}; Event: {}".format(day_date, event))
