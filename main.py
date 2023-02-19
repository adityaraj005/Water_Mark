from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


# --------------------- ADDING WATERMARK -------------------
def watermark():
    # Opening Image
    path = file_path.get()
    image = Image.open(path).convert("RGBA")

    # Creating Text
    text = text_entry.get()
    font = ImageFont.truetype("arial.ttf", 40)

    # Creating Draw Object
    draw = ImageDraw.Draw(image)

    # Positioning Text
    width, height = image.size
    x = height / 2 + 50
    y = width / 2

    # Applying Text
    draw.text((x, y), text, fill="white", font=font)

    # Image with Text and Saving
    image.save(r"watermarked-image.png")
    image.show()


# ---------------- Choosing Image --------------------
def open_file():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select an Image",
                                          )

    file_path.insert(0, filename)


# ------------------ GUI -------------------------------
window = Tk()
window.title("Water Mark")
window.config(padx=50, pady=50)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="watermark_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Label
label2 = Label(text="File Path: ", height=4)
label2.grid(column=0, row=2)
label3 = Label(text="Add Text: ", height=4)
label3.grid(column=0, row=3)

# Entry
file_path = Entry(width=35)
file_path.grid(column=1, row=2, sticky="EW")
text_entry = Entry(width=35)
text_entry.grid(column=1, row=3, columnspan=2, sticky="EW")

# Button
button1 = Button(text="Browse Image", command=open_file)
button1.grid(column=1, row=1)

button2 = Button(text="Add Watermark", command=watermark)
button2.grid(column=1, row=4)


window.mainloop()













