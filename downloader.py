from tkinter import *
from tkinter import ttk
import tkinter as tk
from pytube import Playlist
from tqdm import tqdm
import os
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog

class videoDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Video Downloader")
        self.link      = None
        self.folderLoc = None
        
        self.tabs = ttk.Notebook(master)
        self.tabs.pack(fill=BOTH, expand=TRUE)
        self.frame1 = ttk.Frame(self.tabs)
        self.frame2 = ttk.Frame(self.tabs)
        self.tabs.add(self.frame1, text="Video Downloader")
        self.tabs.add(self.frame2, text="Playlist Downloader")
        
        self.name_var1=tk.StringVar()
        self.name_var2=tk.StringVar()
        name_label = tk.Label(root, text = 'Please copy the link in the text bar', font=('calibre',14, 'bold')).pack()
        self.address1=tk.Entry(self.frame1, textvariable = self.name_var1, font = ('calibre',10,'normal')).pack()
        self.address2=tk.Entry(self.frame2, textvariable = self.name_var2, font = ('calibre',10,'normal')).pack()
    
        self.label = Label(master, text="This product is created by Manvendra Singh")
        self.label.pack()

        self.greet_button = Button(self.frame1, text="Download", command=self.download_video)
        self.greet_button.pack()

        self.close_button = Button(self.frame2, text="Download", command=self.download_playlist)
        self.close_button.pack()

    def download_video(self):
        folder_selected = filedialog.askdirectory(title = 'Select the folder')
        try: 
            url =YouTube(str(self.name_var1.get()))
            video = url.streams.first()
            video.download(folder_selected) 
        except: 
            messagebox.showerror("showerror","Error") 
    
    def download_playlist(self):
        folder_selected = filedialog.askdirectory(title = 'Select the folder')
        playlist = Playlist(str(self.name_var2.get()))
        try:
            print('Number of downloadable videos in playlist: %s' % len(playlist.video_urls))

            for video in tqdm(playlist.videos):
                video.streams.first().download(folder_selected)
        except:
            messagebox.showerror("showerror","Invalid link, please try again")

root = Tk()
root.geometry("%dx%d" % (500, 500))
my_gui = videoDownloader(root)
root.mainloop()