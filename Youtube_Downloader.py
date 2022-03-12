#Youtube Downloader GUI
#Itz_Smudge
#Limitations - no validation for invalid URLs but a fix will be coming soon
#Program will be reuploaded with more comments later
from tkinter import *
from pytube import YouTube as yt

root = Tk()
root.title("YouTube Video Downloader")
root.resizable(False, False)

def error():
	statusLabel["text"] = "DOWNLOAD UNSUCCESSFUL! INVALID URL!"

def download():
	url = urlEntry.get()
	#valid = requests.get(url)
	if url == "":
		error()
	else:
	    yt(url).streams.first().download()
	    statusLabel["text"] = "DOWNLOAD SUCCESSFUL! CHECK THE PROGRAM FOLDER"

url = StringVar()
#https://www.youtube.com/watch?v=BWqus0Yp3M8
instructionLabel = Label(root, font=("Agentcy FB",20,"bold"), text="Paste youtube url here:")
instructionLabel.grid(row=0, column=0, sticky=S+N+E+W )
urlEntry = Entry(root, font=("Agentcy FB",20,"bold"), textvariable=url, insertwidth=1, width=70)
urlEntry.grid(row=1, column=0, sticky=S+N+E+W )

downloadButton = Button(root, padx=16, pady=16, font=("Agentcy FB",20,"bold"), text="DOWNLOAD", command=lambda: download())
downloadButton.grid(row=2, column=0, sticky=S+N+E+W )

statusLabel = Label(root, font=("Agentcy FB",20,"bold"), text="")
statusLabel.grid(row=3, column=0, sticky=S+N+E+W )

root.mainloop()

