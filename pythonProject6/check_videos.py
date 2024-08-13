import tkinter as tk  # imports the tkinter module
import tkinter.scrolledtext as tkst  # imports the scrolled-text function from tkinter as tkst
from PIL import Image, ImageTk  # Imports Image and ImageTk function from Pillow.
import item as lib  # Import the file item.py as item.


def set_text(text_area, content):  # Inserts content into the text_area
    text_area.delete("1.0", tk.END)  # The existing content is deleted
    text_area.insert(1.0, content)  # New content is then added


class CheckVideos:  # Creates a class called CheckVideos
    def __init__(self, window):  # Initiates a Top-Level widget.
        window.geometry("800x550")  # Sets the size of the window to 800x550
        window.title("Check Videos")  # Sets the title of the widget to Check Videos

        enter_lbl = tk.Label(window, text="Enter Video ID")  # Creates a label that has the text "Enter Video ID"
        enter_lbl.grid(row=1, column=0, padx=10, pady=10)  # Determines the position of the label at row=1, column=0
        # in the grid.

        self.input_txt = tk.Entry(window, width=5)  # Creates an entry field that is 5 characters long.
        self.input_txt.grid(row=1, column=1, sticky="E", padx=10, pady=10)  # Places the entry at row 1, col 1 of the
        # grid, the entry will also be sticked to the right side of the grid.

        check_videos_btn = tk.Button(window, text="Check Video", command=self.check_videos_clicked)  # Creates a
        # button with text "Check Videos". When the button is clicked, the function check_videos_clicked is called.
        check_videos_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Places this button at row 2, column
        # 0 of the grid and the button will span 2 columns.

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")  # Creates a Scrolled Textbox that
        # is 48 characters long horizontally and 12 characters vertically.
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Places the scrolled-text at
        # row 0, column = 0 of the grid. The object wil lspan 3 columns, and stick to the left side of the grid.

        self.movie_txt = tkst.ScrolledText(window, width=24, height=4, wrap="none")  # Creates a scrolled-text object
        # that is 24 characters long horizontally and 4 lines long vertically. wrap=none makes sure that a new line
        # isn't created when it exceeds 24 characters.
        self.movie_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # Places the element at row 1, column 3
        # of the grid. The element will stick to the top-left of the grid.

        self.img = Image.open("Images\\Placeholder.png")  # Opens a placeholder image before the user searches for a
        # particular video.
        self.photo = ImageTk.PhotoImage(self.img)  # Creates a photo-image object with the placeholder image.

        self.img_lbl = tk.Label(window, image=self.photo)  # Creates a Label for the image.
        self.img_lbl.grid(row=0, column=3, sticky="S", pady=30)  # Places the element at row 0, column 3 of the grid.
        # The element will stick to the bottom of the grid.

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))  # Creates the status label object with no
        # text at first, Helvetica with size 10 as the font.
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Places the element at row
        # 3, column 0 of the grid. The label wil span 3 columns and stick to the left edge of the grid.

        self.list_videos_clicked()  # Calls the list_videos_clicked() function.

    def check_videos_clicked(self):  # Defines the check_videos_clicked function.
        entry = self.input_txt.get()  # Gets the entry that the user inputted in self.input_txt.
        name = str(lib.get_name(entry))  # Returns the movie element based on the user's inputted ID by calling the
        # get_name function in lib.
        try:  # Tests the block of code if there are any input errors.
            name_id = name.split('-')[0].strip()  # Returns the movie ID from the string with no spaces.
            name_title = name.split('-')[1].strip()  # Returns the movie name from the string with no spaces.
            name_author = name.split('-')[2].strip()  # Returns the movie author from the string with no spaces.
            name_rating = name.split('-')[3].strip()  # Returns the movie rating from the string with no spaces.
            name_views = name.split('-')[4].strip()  # Returns the movie views from the string with no spaces.
            item = f"ID: {name_id}\nName: {name_title}\nAuthor(s): {name_author}\nRating: {name_rating}\nViews: {name_views}"
            # Returns the movie ID from the string with no spaces.
            set_text(self.movie_txt, item)  # Sets the text of the movie_txt to the item string.
            self.img = Image.open(name.split('-')[-1].strip())  # Changes the Image filepath to the Image of the movie
            # element based on the user's inputted ID.
            self.photo = ImageTk.PhotoImage(self.img)  # Changes the photo to the new Image.
            self.img_lbl.configure(image=self.photo)  # Changes the image displayed to the new one.

            self.status_lbl.configure(text="Check video button clicked!")  # Updates the status label.
        except IndexError:  # Raises an error if there is an invalid ID ("ID is not in library or invalid characters")
            self.status_lbl.configure(text="Movie ID not inside the library or ID is not valid.")  # Changes the
            # status label to inform the user that the ID inputted is invalid.

    def list_videos_clicked(self):  # Defines the list_videos_clicked function.
        video_list = lib.list_all()  # Returns everything inside the library
        set_text(self.list_txt, video_list)  # Sets the left textbox to the text in video_list
        self.status_lbl.configure(text="List Videos button was clicked!")  # Updates the status label.
