import tkinter as tk  # imports the tkinter module
import tkinter.scrolledtext as tkst  # imports the scrolled-text function from tkinter as tkst

import item as lib


def set_text(text_area, content):  # Inserts content into the text_area
    text_area.delete("1.0", tk.END)  # The existing content is deleted
    text_area.insert(1.0, content)  # New content is then added


class CreateVideo:
    playlist = []

    def __init__(self, window):
        window.geometry("1400x500")
        window.title("Create Video List")

        enter_lbl = tk.Label(window, text="Enter Video Index:")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_btn = tk.Button(window, text="Add Video", command=self.add_video)
        add_btn.grid(row=0, column=2, sticky="E", padx=10, pady=10)

        play_list_btn = tk.Button(window, text="Play Playlist", command=self.increment_play_count)
        play_list_btn.grid(row=0, column=3, sticky="W", padx=10, pady=10)

        clear_btn = tk.Button(window, text="Clear Playlist", command=self.clear_playlist)
        clear_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=64, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(window, width=64, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=2, columnspan=2, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        set_text(self.playlist_txt, self.playlist)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def add_video(self):
        entry = self.input_txt.get()
        name = str(lib.get_name(entry))
        try:
            if (name != "Video Not Found." and name != "Invalid ID. Please enter a valid ID." and name.split('-')[0].strip()
                   + " - " + name.split('-')[1].strip() not in self.playlist):
                self.playlist.append(name.split('-')[0].strip() + " - " + name.split('-')[1].strip())
                set_text(self.playlist_txt, f"\n".join(self.playlist))
                print(self.playlist)
                self.status_lbl.configure(text="Movie added to playlist.")
            elif name.split('-')[0].strip() + " - " + name.split('-')[1].strip() in self.playlist:
                self.status_lbl.configure(text="Video is already inside the playlist!")
            elif name == "Invalid ID. Please enter a valid ID.":
                self.status_lbl.configure(text="Please enter a valid ID.")
            else:
                self.status_lbl.configure(text="Video not in Library.")
        except IndexError:
            self.status_lbl.configure(text="Invalid ID, please enter a valid ID.")

    def increment_play_count(self):
        for i in self.playlist:
            i = i.split('-')[0].strip()
            lib.add_views(int(i))
        self.status_lbl.configure(text="Playlist is played!")
        set_text(self.playlist_txt, f"\n".join(self.playlist))
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)

    def clear_playlist(self):
        self.playlist.clear()
        self.status_lbl.configure(text="Playlist cleared!")
        set_text(self.playlist_txt, self.playlist)
