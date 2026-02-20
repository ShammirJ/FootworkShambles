"""
THE CHATGPT REFERENCE, DO NOT USE.
"""



import tkinter as tk
import random
import threading
import time
import tkinter.font as tkfont


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Timer")
        self.root.geometry("1920x1080")

        self.running = False
        self.default_bg = root.cget("bg")
        self.corners = [1, 2, 3, 4, 5, 6]

        self.flash_done = threading.Event()

        # ONE shared font object
        self.display_font = tkfont.Font(family="Arial", size=120, weight="bold")

        # ONE label
        self.label = tk.Label(
            root,
            text="Press Start",
            font=self.display_font,
            bg=self.default_bg
        )
        self.label.pack(expand=True, fill="both")

        self.start_button = tk.Button(
            root, text="Start", command=self.start, font=("Arial", 120)
        )
        self.start_button.pack(side="left", padx=20, pady=10)

        self.stop_button = tk.Button(
            root, text="Stop", command=self.stop, state="disabled", font=("Arial", 120)
        )
        self.stop_button.pack(side="right", padx=20, pady=10)

    def start(self):
        if self.running:
            return

        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.display_font.config(size=120)
        self.label.config(text="Waiting...", bg=self.default_bg)

        threading.Thread(target=self.run_loop, daemon=True).start()

    def stop(self):
        self.running = False
        self.flash_done.set()
        self.root.after(0, self.reset_ui)

    def run_loop(self):
        start_time = time.time()
        duration = 120  # seconds

        while self.running and (time.time() - start_time) < duration:
            time.sleep(random.uniform(0.5, 3.0))
            if not self.running:
                break

            self.flash_done.clear()
            self.root.after(0, self.flash_green)
            self.flash_done.wait()

        self.running = False
        self.root.after(0, self.reset_ui)

    def flash_green(self):
        corner = random.choice(self.corners)

        # BIG font during flash
        self.display_font.config(size=300)
        self.label.config(text=str(corner), bg="green")

        self.root.bell()
        self.root.after(2000, self.reset_background)  # EXACT 2s flash

    def reset_background(self):
        # Smaller font after flash
        self.display_font.config(size=120)
        self.label.config(text="Waiting...", bg=self.default_bg)
        self.flash_done.set()

    def reset_ui(self):
        self.display_font.config(size=120)
        self.label.config(text="Press Start", bg=self.default_bg)
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
