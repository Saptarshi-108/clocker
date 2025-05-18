import tkinter as tk
from ui_components import UIComponents
from clock import Clock
from stopwatch import Stopwatch

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clocker")
        self.root.geometry("400x400")

        self.ui = UIComponents(self.root, self.start_stopwatch, self.stop_stopwatch, self.reset_stopwatch)

        self.clock = Clock(self.ui.clock_label)
        self.stopwatch = Stopwatch(self.ui.stopwatch_label)

    def start_stopwatch(self):
        self.stopwatch.start()

    def stop_stopwatch(self):
        self.stopwatch.stop()

    def reset_stopwatch(self):
        self.stopwatch.reset()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()