
import yt_dlp
from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.title("YouTube Downloader")

Label(root, text='YouTube Downloader Install', font=('Arial', 15, 'bold')).pack()

link = StringVar()

Label(root, text="Paste link here", font=('Arial', 15, 'bold')).place(x = 160, y = 60)

link_Entry = Entry(root, width=70, textvariable=link)
link_Entry.place(x = 32, y = 90)

def download_video():
    url = str(link.get())
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    Label(root, text='DOWNLOADED!', font=('Arial', 15,)).place(x = 180, y = 210)

Button(root, text="Download Video", font=('Arial', 15), bg="#009688", padx=2, command=download_video).place(x = 180, y = 150)

root.mainloop()
