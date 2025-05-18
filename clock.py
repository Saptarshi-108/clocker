from time import strftime

class Clock:
    def __init__(self, clock_label):
        self.clock_label = clock_label
        self.update_clock()

    def update_clock(self):
        time_string = strftime("%H:%M:%S")
        self.clock_label.config(text=time_string)
        self.clock_label.after(1000, self.update_clock)