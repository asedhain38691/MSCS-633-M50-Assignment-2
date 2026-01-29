import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qr_code():
    # This generates a QR code from the entered URL and display it.
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Input Error", "Please enter a valid URL.")
        return

    qr = qrcode.make(url)
    qr.save("final_qr_code.png")

    display_qr_code()


def display_qr_code():

    # This displays the generated QR code in a new window.

    qr_window = tk.Toplevel(root)
    qr_window.title("img")

    img = Image.open("final_qr_code.png")
    img = img.resize((400, 400))
    qr_img = ImageTk.PhotoImage(img)

    label = tk.Label(qr_window, image=qr_img)
    label.image = qr_img
    label.pack(padx=10, pady=10)


# Main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x250")

tk.Label(root, text="Enter your URL:", font=("Arial", 18)).pack(pady=5)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr_code
)
generate_button.pack(pady=10)

root.mainloop()