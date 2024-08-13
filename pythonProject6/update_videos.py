import tkinter as tk  # imports the tkinter module
import tkinter.scrolledtext as tkst  # imports the scrolled-text function from tkinter as tkst
import font_manager as font
import item as lib


def set_text(text_area, content):  # Inserts content into the text_area
    text_area.delete("1.0", tk.END)  # The existing content is deleted
    text_area.insert(1.0, content)  # New content is then added


class UpdateVideo:
    def __init__(self, window):
        window.title("Update Videos")
        window.geometry("1000x700")
        font.configure()

        enter_lbl = tk.Button(window, text="Enter video ID:")
        enter_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        rating_lbl = tk.Button(window, text="Enter new rating:")
        rating_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        self.rating_entry = tk.Entry(window, width=5)
        self.rating_entry.grid(row=2, column=0, padx=10, pady=15, sticky="N")

        self.input_entry = tk.Entry(window, width=5)
        self.input_entry.grid(row=1, column=0, padx=10, pady=15, sticky="N")

        self.playlist_txt = tkst.ScrolledText(window, width=64, height=12, wrap="none")
        self.playlist_txt.grid(row=0, column=0, padx=10, pady=10)

        new_rating_btn = tk.Button(window, text="Video name and new Rating:")
        new_rating_btn.grid(row=0, column=1, padx=10, pady=10, sticky="N")

        self.new_movie_txt = tkst.ScrolledText(window, width=24, height=5, wrap="none")
        self.new_movie_txt.grid(row=0, column=1, padx=10, pady=10, sticky="S")

        submit_btn = tk.Button(window, text="Submit", command=self.check_rating)
        submit_btn.grid(row=1, column=0, padx=10, pady=0, sticky="E", rowspan=2)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.playlist_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def check_rating(self):
        try:
            entry = int(self.input_entry.get())
            n_rating = float(self.rating_entry.get())
            if entry != "Video Not Found." and entry != "Invalid ID. Please enter a valid ID.":
                if n_rating < 0 or n_rating > 10:
                    self.status_lbl.configure(text="Invalid Rating!, please enter a rating from 1-10.")
                else:
                    lib.update_rating(entry, n_rating)
                    name = str(lib.get_name(entry))
                    name_title = name.split('-')[1].strip()
                    name_rating = name.split('-')[3].strip()
                    name_views = name.split('-')[4].strip()
                    item = f"Name: {name_title}\nRating: {name_rating}\nViews: {name_views}"
                    set_text(self.new_movie_txt, item)
                    video_list = lib.list_all()
                    set_text(self.playlist_txt, video_list)
                    self.status_lbl.configure(text="Video rating updated.")
        except TypeError:
            self.status_lbl.configure(text="Please enter a valid ID/Rating.")
        except IndexError:
            self.status_lbl.configure(text="Video not found/does not exist.")
        except ValueError:
            self.status_lbl.configure(text="Field must be a number!")
