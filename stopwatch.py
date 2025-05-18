from time import time

class Stopwatch:
    def __init__(self, stopwatch_label):
        self.stopwatch_label = stopwatch_label
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_stopwatch()

    def update_stopwatch(self):
        if self.running:
            current_time = time()
            elapsed = current_time - self.start_time + self.elapsed_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed % 1) * 100)
            time_string = f"{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
            self.stopwatch_label.config(text=time_string)
        self.stopwatch_label.after(10, self.update_stopwatch)

    def start(self):
        if not self.running:
            self.start_time = time()
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time += time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00.00")