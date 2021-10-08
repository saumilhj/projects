import tkinter
from tkinter import Tk, ttk, Button, Label, Entry, filedialog, messagebox
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageFont


# Functions
def choose_file():
    global FILENAME, CHOSEN_FILE
    FILENAME = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Image files",
                                                      ["*.png*", "*.jpg*", "*.jpeg*"]),
                                                     ("All Files",
                                                      "*.*")))
    CHOSEN_FILE = Label(window, text=FILENAME)
    CHOSEN_FILE.grid(row=0, column=1, padx=6, pady=4, sticky="W")


def confirm_entries():
    global CHOSEN_FILE
    if CHOSEN_FILE == "":
        messagebox.showerror(title="Error", message="No file chosen!")
    else:
        answer = messagebox.askyesno(title="Confirmation", message=f"Do you wish to proceed?\n"
                                                                   f"These are your choices:\n"
                                                                   f"Text: {watermark_txt_area.get()}\n"
                                                                   f"Position: {watermark_pos_txt.get()}\n"
                                                                   f"Size: {watermark_size_txt.get()}\n"
                                                                   f"Fill: {watermark_color_text.get()}")
        if answer:
            put_mark()


def put_mark():
    global FILENAME
    font_size = int(watermark_size_txt.get())
    if watermark_color_text.get() == "Light":
        fill_color = (255, 255, 255, 128)
    else:
        fill_color = (66, 68, 68, 128)
    with Image.open(FILENAME).convert("RGBA") as img:
        width, height = img.size
        fnt = ImageFont.truetype("C:/Users/Admin/AppData/Local/Microsoft/Windows/Fonts/nasalization-rg.ttf", font_size)
        text_size = fnt.getsize(watermark_txt_area.get())
        txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        if watermark_pos_txt.get() == "Top-Left":
            draw.text((20, 20), watermark_txt_area.get(), font=fnt, fill=fill_color)
        elif watermark_pos_txt.get() == "Top-Right":
            draw.text((width - 20 - text_size[0], 20), watermark_txt_area.get(),
                      font=fnt, fill=fill_color)
        elif watermark_pos_txt.get() == "Bottom-Left":
            draw.text((20, height - 20 - text_size[1]), watermark_txt_area.get(),
                      font=fnt, fill=fill_color)
        else:
            draw.text((width - 20 - text_size[0], height - 20 - text_size[1]), watermark_txt_area.get(),
                      font=fnt, fill=fill_color)
        combined = Image.alpha_composite(img, txt)
        combined = combined.convert("RGB")
        combined.show()
        satisfied = messagebox.askyesno(title="Final Confirmation",
                                        message="Do you wish to save this file?")
        if satisfied:
            file = filedialog.asksaveasfile(mode="wb", filetypes=[("PNG Image", ".png"), ("JPEG Image", ".jpeg")],
                                            defaultextension=".png")
            if file:
                combined.save(file)


# Window configuration
FILENAME = ""
CHOSEN_FILE = ""
window = Tk()
style = Style(theme="yeti")
window.title("Image Watermarking")
window.geometry("600x225")
window.config(background="#FFFFFF", pady=20, padx=25)
window.resizable(0, 0)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=6)

# Select file button
browse = Button(window, text="Choose File", command=choose_file)
browse.grid(row=0, column=0, padx=6, pady=4, sticky="W")

# Watermark text entry
watermark_txt = Label(window, text="Enter text:")
watermark_txt.grid(row=1, column=0, padx=6, pady=4, sticky="W")
watermark_txt_area = Entry(window)
watermark_txt_area.grid(row=1, column=1, padx=6, pady=4, sticky="EW")

# Watermark position
watermark_pos = Label(window, text="Enter position: ")
watermark_pos.grid(row=2, column=0, padx=6, pady=4, sticky="W")
watermark_pos_txt = ttk.Combobox(window, textvariable=tkinter.StringVar())
watermark_pos_txt['values'] = ("Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right")
watermark_pos_txt.current(3)
watermark_pos_txt.grid(row=2, column=1, padx=6, pady=1, sticky="EW")

# Watermark size
watermark_size = Label(window, text="Enter text size: ")
watermark_size.grid(row=3, column=0, padx=6, pady=4, sticky="W")
watermark_size_txt = Entry(window)
watermark_size_txt.grid(row=3, column=1, padx=6, pady=4, sticky="EW")

# Watermark color
watermark_color = Label(window, text="Choose theme: ")
watermark_color.grid(row=4, column=0, padx=6, pady=4, sticky="W")
watermark_color_text = ttk.Combobox(window, textvariable=tkinter.StringVar())
watermark_color_text['values'] = ("Dark", "Light")
watermark_color_text.current(1)
watermark_color_text.grid(row=4, column=1, padx=6, pady=4, sticky="EW")

# Submit button
submit = Button(window, text="Submit", command=confirm_entries)
submit.grid(row=5, column=1, padx=6, pady=4, sticky="E")
window.mainloop()
