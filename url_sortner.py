import pyperclip
import pyshorteners
from tkinter import *


root = Tk()
root.geometry("400x200")
root.title("url shortener")
root.configure(bg="white")
url = StringVar()
url_address = StringVar()
def urlshortener():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="Url Shortener",font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Shortern",command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy",command=copyurl).pack(pady=5)

root.mainloop()



