import os, sys, webbrowser
import tkinter
import customtkinter
from pytube import YouTube, Playlist
from PIL import Image



#Image Load..
file_path = os.path.dirname(os.path.realpath(__file__))
image_1 = customtkinter.CTkImage(Image.open(file_path + "/github.png"))
image_2 = customtkinter.CTkImage(Image.open(file_path + "/aperture.png"))

"""
#use this if you are going to turn this code into an .exe
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller '''
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
"""


def downstarter():
    try:
        ytlink = link.get()
        linkObj = YouTube(ytlink, on_progress_callback=progfunc)
        vid = linkObj.streams.get_by_resolution()
        vid_title = vid.title

        nametit2.configure(text=linkObj.title, text_color="white")
        os.path.join("downloads", f"{vid_title}.mp4")

        vid.download(output_path="downloads")

        finishLabel.configure(text="Download Completed")
        finishLabel.configure(text="")
        finishLabel.update()

    except:
        if len(ytlink) < 20:
            finishLabel.configure(text="Please Enter a Link", text_color="red")
        
        else:
            finishLabel.configure(text="Error Occured", text_color="red")
            finishLabel.update()



def downstarter_mp3():
    try:
        ytlink = link.get()
        linkObj = YouTube(ytlink, on_progress_callback=progfunc)
        vid = linkObj.streams.get_audio_only()
        
        nametit2.configure(text=linkObj.title, text_color="white")
        aud_title = vid.title

        nametit2.configure(text=linkObj.title, text_color="white")
        os.path.join("downloads", f"{aud_title}.mp3")

        vid.download()

        finishLabel.configure(text="Download Completed")
        finishLabel.configure(text="")
        finishLabel.update()

    except:
        if len(ytlink) < 20:
            finishLabel.configure(text="Please Enter a Link", text_color="red")
            finishLabel.update()

        else:
            finishLabel.configure(text="Error Occured", text_color="red")
            finishLabel.update()



def progfunc(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_done = total_size - bytes_remaining
    percent_done = bytes_done / total_size * 100 
    per = str(int(percent_done))

    progPercent.configure(text=per + "%")
    progPercent.update()

    progBar.set(float(percent_done) / 100) #updating bar



#system setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


#app frame
app = customtkinter.CTk()
app.geometry("610x310")
app.title("Fuck Google")
app.iconbitmap('myicon.ico')


# -- uı elements -- 

title = customtkinter.CTkLabel(app, text="Link : ")
title.pack(padx=10, pady=10)
title.place(x=35, y=47)

name_title = customtkinter.CTkLabel(app, text="Name : ")
name_title.pack(padx=10, pady=10)
name_title.place(x=35, y=7)

nametit2 = customtkinter.CTkLabel(app, text="")
nametit2.pack()
nametit2.place(x=100, y=7)



#link input
urlinput = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=420, height=30, textvariable=urlinput)
link.pack()
link.place(x=90, y=47)



#download end
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()
finishLabel.place(x=255, y=200)



#quality choice
quality_menu = customtkinter.CTkOptionMenu(app, values=["Quality", "360p", "480p", "720p", "Highest (Auto)" ],
                                    width=30, height=30, fg_color="blue", button_color="blue")

quality_menu.pack()
quality_menu.place(x = 515, y = 47)



#download-buttons
download = customtkinter.CTkButton(app, text="Download .mp4", command=downstarter)
download.pack()
download.place(x = 150, y = 109)

download_mp3 = customtkinter.CTkButton(app, text="Download Audio", command=downstarter_mp3)
download_mp3.pack()
download_mp3.place(x =320, y = 109)



#progress
progPercent = customtkinter.CTkLabel(app, text="%0")
progPercent.pack()
progPercent.place(x=95, y=180)

progBar = customtkinter.CTkProgressBar(app, width=420)
progBar.set(0)
progBar.pack(padx=10, pady=10)
progBar.place(x=95, y=177)


#advertisement
adver_title = customtkinter.CTkButton(app, image = image_1, text="Other Repositories", text_color="white", fg_color="gray")
adver_title.pack()
adver_title.bind("<Button-1>", lambda e, : webbrowser.open_new(r"https://github.com/OldKokoroz"))
adver_title.place(x=150, y=270)

adver_title2 = customtkinter.CTkButton(app, image = image_2, text="My Website", text_color="white", fg_color="gray")
adver_title2.pack()

adver_title2.bind("<Button-1>", lambda e, : webbrowser.open_new(r"https://crudelitas.com"))
adver_title2.place(x=320, y=270)


# thanks to James Burke/StackOverFlow --- webbrowser.open_new(r"file://c:\test\test.csv")

#run -- keep at the bottom
app.mainloop()
