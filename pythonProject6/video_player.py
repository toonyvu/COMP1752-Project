import tkinter as tk
import font_manager as font
from check_videos import CheckVideos
from create_video_list import CreateVideo
from update_videos import UpdateVideo


def check_videos_clicked():
    status_lbl.configure(text="Check Videos Button clicked!")
    CheckVideos(tk.Toplevel(window))


def create_playlist_clicked():
    status_lbl.configure(text="Create Playlist Button clicked!")
    CreateVideo(tk.Toplevel(window))


def update_playlist_clicked():
    status_lbl.configure(text="Update Playlist Button clicked!")
    UpdateVideo(tk.Toplevel(window))


window = tk.Tk()
window.geometry("550x150")
window.title("Video Player")

font.configure()

header_lbl = tk.Label(window, text="Select one of the options below:")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_playlist_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_playlist_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
