import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    """
    for adding widgets into the frame use .scrollable_frame, do NOT add widgets directly.
    use width and height to enforce size. for modifing the forced size use change_size.
    """
    #borroved from "https://blog.tecladocode.com/tkinter-scrollable-frames/" and modified a little bit.
    def __init__(self, container, *args, y_scroll=True, x_scroll=True, **kwargs):
        super().__init__(container, *args, **kwargs)
        forced_width = kwargs.pop("width", None)
        forced_height = kwargs.pop("height", None)
        canvas = tk.Canvas(self, width=forced_width, height=forced_height)
        self.canvas = canvas
        if y_scroll:
            scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        if x_scroll:
            scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if x_scroll and y_scroll:
            canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        elif x_scroll:
            canvas.configure(xscrollcommand=scrollbar_x.set)
        elif y_scroll:
            canvas.configure(yscrollcommand=scrollbar_y.set)

        if x_scroll:
            scrollbar_x.pack(side="bottom", fill="x")
        
        canvas.pack(side="left", fill="both", expand=True)
        
        if y_scroll:
            scrollbar_y.pack(side="right", fill="y")
        

    def change_size(self, width=None, height=None):
        """
        Changes the enforced size of the ScrollableFrame
        """
        if width is not None:
            #self.forced_width = width
            super().configure(width=width)
            self.canvas.configure(width=width)
        if height is not None:
            #self.forced_height = height
            super().configure(height=height)
            self.canvas.configure(height=height)
    


if __name__ == "__main__":
    root = tk.Tk()

    #ScrollableFrame
    frame = ScrollableFrame(root, width=150, height=400, x_scroll=False)
    frame.change_size(height=200)
    for i in range(50):
        ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

    frame.pack()


    root.mainloop()