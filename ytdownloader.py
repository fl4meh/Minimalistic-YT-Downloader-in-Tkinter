from pytubefix import YouTube
import tkinter as tk
import os 


class YtDownloader:
    def __init__(self, ytlink):
        self.ytlink = ytlink
        
    def link_handler(self):
        target_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        if not os.path.exists(target_folder):
            target_folder = os.path.join(os.path.expanduser("~"), "Desktop", "MyDownloads")

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        YouTube(self.ytlink).streams.first().download()
        yt = YouTube(self.ytlink)
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        print(f"Starting download: {yt.title}")
        stream.download(output_path=target_folder)
        print(f"Saved to: {target_folder}")
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('YtDownloader')
        self.geometry('450x450')
        self.label = tk.Label(self, text='YT Downloader')
        self.label.pack()
        
        
        self.label = tk.Label(self, text='Insert Link')
        self.label.pack()

        self.entry = tk.Entry()
        self.entry.pack()

        self.button = tk.Button(self, text='Download')
        self.button['command'] = self.download_button
        self.button.pack()

    def download_button(self):
        ytlink = self.entry.get()
        yt = YtDownloader(ytlink)
        yt.link_handler()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()