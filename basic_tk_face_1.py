# -===== Settings =====-
face_colour = "green3"
background_colour = "black"
face_font = "Small Fonts"
# Use "MV Boli" for a hand-drawn look,
# Use "Small Fonts" for a retro pixelated look,
# Use "Courier" or "DejaVu Sans Mono" for a regular font look.
# All Colours: https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html
# ALl Fonts: Run 'all_tkinter_fonts.py'


import tkinter as tk
import random


class RetroCompanion:
    def __init__(self, root):
        self.root = root
        self.root.title("Companion")
        # Make the window stay on top and remove the border for a 'sprite' look
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.geometry("200x200+1700+360") # Window size + Position offset

        # State variables
        self.mood = "Neutral"
        self.blink_state = False

        # UI Element (The Face)
        self.label = tk.Label(root, text="(=_=)", font=(face_font, 40), fg=face_colour, bg=background_colour)
        self.label.pack(expand=True, fill="both")

        # Start the "Brain"
        self.update_logic()
        self.blink_loop()

    def get_face(self):
        """The 'Component' Map: Returns a string based on current state"""

        faces = {
            "Neutral": "(o_o)",
            "Happy": "(^ V ^)",
            "Sad": "(;_;)",
            "Angry": "(>_<)",
            "Bored": "(~_~)",
            "Confused": "(o.o)",
            "Shocked": "(0.0)",
            "Tweaked": "(o.0)",
            "Pleased": "(ouo)",
            "Gay": "(uwu)",
            "More_Gay": "(owo)",
            "Tired": "(=_=)",
            "Excited": "(*o*)",
            "Stare": "(o  o)"
        }

        faces_blink = {
            "Neutral": "(-_-)",
            "Happy": "(-v-)",
            "Sad": "(-_-)",
            "Angry": "(-_-)",
            "Bored": "(-_-)",
            "Confused": "(-.-)",
            "Shocked": "(-.-)",
            "Tweaked": "(o.-)",
            "Pleased": "(-u-)",
            "Gay": "(-w-)",
            "More_Gay": "(-w-)",
            "Tired": "(- , -)",
            "Excited": "(-o-)",
            "Stare": "(-  -)"
        }

        # If in blink state, return face derived from mood,
        # but from the faces_blink list,
        # or return "(-_-)" as default in case of failure
        if self.blink_state:
            return faces_blink.get(self.mood, "(-_-)")

        # Else, Just return corresponding face to mood,
        # or return "(o_o)" as default in case of failure
        return faces.get(self.mood, "(o_o)")

    def update_logic(self):
        """Simulates the companion 'thinking' and changing moods"""
        # Pick a random mood every 5 seconds
        self.mood = random.choice(["Neutral", "Happy", "Sad", "Angry", "Bored", "Confused", "Shocked", "Tweaked", "Pleased", "Gay", "More_Gay", "Tired", "Excited", "Stare"])
        self.label.config(text=self.get_face())

        # Run again in 5 seconds
        self.root.after(5000, self.update_logic)

    def blink_loop(self):
        """Handles the 'Procedural' animation of blinking"""
        self.blink_state = not self.blink_state
        self.label.config(text=self.get_face())

        # If just closed eyes, open them fast (200ms)
        # If open, stay open for a random longer time (2-4s)
        duration = 200 if self.blink_state else random.randint(2000, 4000)
        self.root.after(duration, self.blink_loop)


# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = RetroCompanion(root)
    root.mainloop()