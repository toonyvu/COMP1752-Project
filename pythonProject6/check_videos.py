import tkinter as tk  # imports the tkinter module
import tkinter.scrolledtext as tkst  # imports the scrolled-text function from tkinter as tkst
from PIL import Image, ImageTk
import item as lib
import os


def set_text(text_area, content):  # Inserts content into the text_area
    text_area.delete("1.0", tk.END)  # The existing content is deleted
    text_area.insert(1.0, content)  # New content is then added


class CheckVideos:  # Creates
    def __init__(self, window):
        window.geometry("800x550")
        window.title("Check Videos")

        enter_lbl = tk.Label(window, text="Enter Video ID")
        enter_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=1, column=1, sticky="E", padx=10, pady=10)

        check_videos_btn = tk.Button(window, text="Check Video", command=self.check_videos_clicked)
        check_videos_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.movie_txt = tkst.ScrolledText(window, width=24, height=4, wrap="none")
        self.movie_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.img = Image.open("Images\\Placeholder.png")
        self.photo = ImageTk.PhotoImage(self.img)

        self.img_lbl = tk.Label(window, image=self.photo)
        self.img_lbl.grid(row=0, column=3, sticky="S", pady=30)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def check_videos_clicked(self):
        entry = self.input_txt.get()
        name = str(lib.get_name(entry))
        try:
            name_id = name.split('-')[0].strip()
            name_title = name.split('-')[1].strip()
            name_author = name.split('-')[2].strip()
            name_rating = name.split('-')[3].strip()
            name_views = name.split('-')[4].strip()
            item = f"ID: {name_id}\nName: {name_title}\nAuthor(s): {name_author}\nRating: {name_rating}\nViews: {name_views}"
            set_text(self.movie_txt, item)
            self.img = Image.open(name.split('-')[-1].strip())
            self.photo = ImageTk.PhotoImage(self.img)
            self.img_lbl.configure(image=self.photo)

            self.status_lbl.configure(text="Check video button clicked!")
        except IndexError:
            self.status_lbl.configure(text="Movie ID not inside the library or ID is not valid.")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
