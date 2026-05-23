from pytubefix import YouTube
import tkinter as tk
import os 


class YtDownloader:
    def __init__(self, directory=None):
        self.directory = directory

    def select_location(self, directory):
        if not directory:
            self.directory = os.path.join(os.path.expanduser("~"), "Downloads")
            
            if not os.path.exists(self.directory):
                self.directory = os.path.join(os.path.expanduser("~"), "Desktop", "MyDownloads")
        else: 
            self.directory = directory

        print(f"Selected directory: {self.directory}")
        
    def link_handler(self, ytlink):
        self.ytlink = ytlink
        yt = YouTube(self.ytlink)
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        print(f"Starting download: {yt.title}")
        stream.download(output_path=self.directory)
        print(f"Saved to: {self.directory}")
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.yt = YtDownloader()
        self.title('YtDownloader')
        self.geometry('450x450')
        self.label = tk.Label(self, text='YT Downloader')
        self.label.pack()
        
        
        self.label = tk.Label(self, text='Insert Link')
        self.label.pack()

        self.entry = tk.Entry()
        self.entry.pack()

        self.label = tk.Label(self, text='Select Directory')
        self.label.pack()

        self.loc = tk.Entry()
        self.loc.pack()

        self.button = tk.Button(self, text='Select Location')
        self.button['command'] = self.select_location_button
        self.button.pack()

        self.button = tk.Button(self, text='Download')
        self.button['command'] = self.download_button
        self.button.pack()

    def download_button(self):
        ytlink = self.entry.get()
        self.yt.link_handler(ytlink)

    def select_location_button(self):
        directory = self.loc.get()
        self.yt.select_location(directory)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()