import tkinter as tk

class UIComponents:
    def __init__(self, root, start_command, stop_command, reset_command):
        self.root = root
        self.root.configure(bg="black")
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-transparentcolor", "black")  # Set black as transparent

        self.main_canvas.pack()
        # Inner frame for UI elements
        self.inner_frame = tk.Frame(
            self.main_canvas,
            bg="#2A2E2F"
        )
        self.main_canvas.create_window(
            self.window_size/2, self.window_size/2,
            window=self.inner_frame,
            width=self.window_size-40,
            height=self.window_size-40
        )

        # Clock Label
        self.clock_label = tk.Label(
            self.inner_frame,
            font=("Arial", 30, "bold"),
            fg="red",
            bg="#2A2E2F",
            pady=5
        )
        self.clock_label.pack(pady=20)

        # Stopwatch Label
        self.stopwatch_label = tk.Label(
            self.inner_frame,
            text="00:00:00.00",
            font=("Arial", 24, "bold"),
            fg="spring green",
            bg="#2A2E2F",
            pady=5
        )
        self.stopwatch_label.pack(pady=20)

        # Buttons Frame
        self.button_frame = tk.Frame(self.inner_frame, bg="#2A2E2F")
        self.button_frame.pack(pady=10)

        # Button styles
        self.button_width = 70
        self.button_height = 35
        self.button_radius = 10
        self.normal_color = "#3A4F50"
        self.hover_color = "#5E7677"
        self.click_color = "#A3BFFA"

        # Stopwatch Buttons
        self.create_rounded_button(
            self.button_frame, "Start", start_command, 0, 0
        )
        self.create_rounded_button(
            self.button_frame, "Stop", stop_command, 0, 1
        )
        self.create_rounded_button(
            self.button_frame, "Reset", reset_command, 0, 2
        )

        # Make window draggable
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.main_canvas.bind("<Button-1>", self.start_drag)
        self.main_canvas.bind("<B1-Motion>", self.on_drag)

    def start_drag(self, event):
        self.drag_start_x = event.x_root - self.root.winfo_x()
        self.drag_start_y = event.y_root - self.root.winfo_y()

    def on_drag(self, event):
        x = event.x_root - self.drag_start_x
        y = event.y_root - self.drag_start_y
        self.root.geometry(f"+{x}+{y}")

    def create_rounded_button(self, parent, text, command, row, column):
        # Canvas for rounded button
        canvas = tk.Canvas(
            parent,
            width=self.button_width,
            height=self.button_height,
            bg="#2A2E2F",
            highlightthickness=0
        )
        canvas.grid(row=row, column=column, padx=8)

        # Draw rounded rectangle
        button_id = self.create_rounded_rect(
            canvas, 5, 5, self.button_width-5, self.button_height-5,
            radius=self.button_radius, fill=self.normal_color, outline=""
        )

        # Button text
        text_id = canvas.create_text(
            self.button_width/2, self.button_height/2,
            text=text, font=("Arial", 12, "bold"), fill="white"
        )

        # Animation states
        canvas.is_hovered = False
        canvas.is_clicked = False

        def on_enter(event):
            if not canvas.is_hovered:
                canvas.is_hovered = True
                canvas.itemconfig(button_id, fill=self.hover_color)
                canvas.scale(button_id, self.button_width/2, self.button_height/2, 1.05, 1.05)
                canvas.scale(text_id, self.button_width/2, self.button_height/2, 1.05, 1.05)

        def on_leave(event):
            if canvas.is_hovered:
                canvas.is_hovered = False
                canvas.itemconfig(button_id, fill=self.normal_color)
                canvas.scale(button_id, self.button_width/2, self.button_height/2, 1/1.05, 1/1.05)
                canvas.scale(text_id, self.button_width/2, self.button_height/2, 1/1.05, 1/1.05)

        def on_click(event):
            if not canvas.is_clicked:
                canvas.is_clicked = True
                canvas.itemconfig(button_id, fill=self.click_color)
                command()
                canvas.after(100, lambda: canvas.itemconfig(button_id, fill=self.hover_color if canvas.is_hovered else self.normal_color))
                canvas.after(100, lambda: setattr(canvas, 'is_clicked', False))

        # Bind events
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        canvas.bind("<Button-1>", on_click)

    def create_rounded_rect(self, canvas, x1, y1, x2, y2, radius, **kwargs):
        # Create a rounded rectangle using polygon points
        points = [
            x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1,
            x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius,
            x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2,
            x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)