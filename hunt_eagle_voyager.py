#!/usr/bin/env python3
"""Simple program to compute the distance Voyager 1 has traveled."""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):  # main app class for tkinter
    def __init__(self):
        """
        Initializer function for class.

        Args:
            self: instance of class

        Returns:
            None, init cannot return a value
            This initializes many important values
        """
        super().__init__()  # required for rendering Tkinter window

        # set required Instance Variables for Tkinter
        self.title('Voyager distance calculator')
        self.geometry('750x30')

        # set window's entry fields value as variables
        self.time_unit = tk.StringVar()
        self.time_value = tk.StringVar()

        # set class values for calculation
        self.VOYAGER_TRAVEL_SPEED_MPH = 38_241
        self.KM_IN_MILE = 1.609344
        self.MILES_IN_ONE_AU = 92_955_807.3
        self.INITIAL_DISTANCE_FROM_SUN = 16_637_000_000
        self.SPEED_OF_LIGHT_MPH = 670_616_629

        # create the widgets to be rendered
        self.__create_widgets()

    def __create_widgets(self):
        """
        Private function used to create gui widgets.

        Args: 
            self: instance of class

        Returns: 
            None. It sends user values to report_calculation function
        """

        # create labels, entry, and combobox for user input & place on grid
        ttk.Label(
            self,
            text="Find the Voyager's distance from the Sun",
            font=('calibre', 10, 'bold')
        ).grid(row=0, column=0)

        ttk.Entry(
            self,
            textvariable=self.time_value,
            width=12,
            font=('calibre', 10, 'normal')
        ).grid(row=0, column=1)

        ttk.Combobox(
            self,
            width=10,
            textvariable=self.time_unit,
            state="readonly",
            # values will be shown when user clicks combo box
            values=('Seconds',
                    'Minutes',
                    'Hours',
                    'Days',
                    'Months',
                    'Years')

        ).grid(row=0, column=2)

        ttk.Label(
            self,
            text="after September 25, 2009 12:00",
            font=('calibre', 10, 'bold')
        ).grid(row=0, column=3)

        ttk.Button(
            self,
            text='Calculate',
            command=self.__report_calculation  # when button is pressed, calculate
        ).grid(row=0, column=4, padx=(30, 10))

    def __report_calculation(self):
        """
        Private function used to calculate voyager's distance & radio comm time
        from user inputted values

        Args: 
            self: instance of class

        Returns:
            None.
            Formats values to a string then opens a report window
        """
        # get values from entry field and combobox
        value = int(self.time_value.get())
        time_unit = self.time_unit.get()

        # following coding standard 6, Symbolic Constants
        SECONDS_IN_HOUR = 3600
        MINUTES_IN_HOUR = 60
        HOURS_IN_DAY = 24
        HOURS_IN_MONTH = 730
        HOURS_IN_YEAR = 8760
        RADIO_COMMUNICATION_MULTIPLIER = 2
        ROUND_TO_4 = 4
        ROUND_TO_2 = 2

        # hashmap used for calculation.
        # the keys are the selectable items in the combobox.
        # the values contain the travel speed.
        # the travel speed given is in MPH, so we need to divide or multiply it
        # accordingly.

        time_conversions = {
            "Seconds": self.VOYAGER_TRAVEL_SPEED_MPH / SECONDS_IN_HOUR,
            "Minutes": self.VOYAGER_TRAVEL_SPEED_MPH / MINUTES_IN_HOUR,
            "Hours": self.VOYAGER_TRAVEL_SPEED_MPH,
            "Days": self.VOYAGER_TRAVEL_SPEED_MPH * HOURS_IN_DAY,
            "Months": self.VOYAGER_TRAVEL_SPEED_MPH * HOURS_IN_MONTH,
            "Years": self.VOYAGER_TRAVEL_SPEED_MPH * HOURS_IN_YEAR
        }

        distance = value * time_conversions[time_unit]

        # calculate the values to report
        distance_in_miles = round(
            (distance + self.INITIAL_DISTANCE_FROM_SUN), ROUND_TO_4)

        distance_in_km = round(
            (distance_in_miles * self.KM_IN_MILE), ROUND_TO_4)

        distance_in_au = round(
            (distance_in_miles / self.MILES_IN_ONE_AU), ROUND_TO_4)

        radio_communication_time = round(
            ((distance / self.SPEED_OF_LIGHT_MPH) * RADIO_COMMUNICATION_MULTIPLIER), ROUND_TO_2)

        showinfo(title='Results',
                 message=f"Distance from the Sun: \n{distance_in_miles} miles\n{distance_in_km} km \
        \n{distance_in_au} au\nRound trip radio communication: {radio_communication_time} hours")


# main app loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
