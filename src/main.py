import os
import git
import tkinter as tk
from configparser import ConfigParser
from tkinter import filedialog
import time
import subprocess
from PIL import ImageTk, Image

repo_url = "https://github.com/freedoom-badass-edition/freedoom-badass-edition.git"

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

root = tk.Tk()
root.title('bad*ss launcher')
root.geometry('800x600')
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
photo = tk.PhotoImage(file='./assets/favicon.png')
root.iconphoto(False, photo)

config = ConfigParser()
config.read('config.ini')

directory = os.getcwd()+"/freedoom-badass-edition"
sourceport = ""
if config.get('badass', 'directory'):
    directory = config.get('badass', 'directory')
if config.get('badass', 'sourceport'):
    sourceport = config.get('badass', 'sourceport')
if not config.has_section('badass'):
    config.add_section('badass')
config.set('badass', 'directory', directory)
config.set('badass', 'sourceport', sourceport)
with open('config.ini', 'w') as f:
    config.write(f)

img = Image.open("./assets/launcher_logo.png")
img = img.resize((240, 144), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
title_label = tk.Label(root, image=img)

directory_title_label = tk.Label(root, text="install directory: ", font=("Comic Sans MS", 12, 'bold'))
directory_label = tk.Label(root, text=directory, font=("Comic Sans MS", 10))
download_status_label = tk.Label(root, text="ready and waiting", font=("Comic Sans MS", 16, 'bold'))
sourceport_title_label = tk.Label(root, text="selected sourceport: ", font=("Comic Sans MS", 12, 'bold'))
sourceport_label = tk.Label(root, text=sourceport, font=("Comic Sans MS", 10))

def itstimetochoose():
    directory = filedialog.askdirectory()+"/freedoom-badass-edition"
    directory_label['text'] = directory
    config.set('badass', 'directory', directory)
    with open('config.ini', 'w') as f:
        config.write(f)
def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False
def download():
    if not is_git_repo(directory):
        download_status_label['text'] = "downloading..."
        root.update()
        repo = git.Repo.clone_from(repo_url, directory)
        download_status_label['text'] = "download finished"
    else:
        download_status_label['text'] = "fdb*e is already installed"
def update():
    if is_git_repo(directory):
        download_status_label['text'] = "updating..."
        root.update()
        o = git.Repo(directory).remotes.origin
        o.pull()
        download_status_label['text'] = "update finished"
    else:
        download_status_label['text'] = "fdb*e is not installed"
        o.pull()
def start_game():
    if is_git_repo(directory):
        if sourceport != "":
            download_status_label['text'] = "launching game..."
            root.update()
            subprocess.run([sourceport, '-iwad', 'freedoom2.wad', '-file', directory])
        else:
            download_status_label['text'] = "sourceport isn't selected'"
    else:
        download_status_label['text'] = "fdb*e is not installed"
def set_sourceport():
    sourceport = filedialog.askopenfilename()
    sourceport['text'] = sourceport
    config.set('badass', 'sourceport', sourceport)
    with open('config.ini', 'w') as f:
        config.write(f)
def quit():
    root.destroy()

download_button = tk.Button(root, text='download fdb*e', command=download)
update_button = tk.Button(root, text='update fdb*e', command=update)
pick_button = tk.Button(root, text='set install directory',command=itstimetochoose)
sourceport_button = tk.Button(root, text='select sourceport',command=set_sourceport)
start_button = tk.Button(root, text='start game',command=start_game)
quit_button = tk.Button(root, text='exit launcher',command=quit)

title_label.pack(side='top')

quit_button.pack(ipadx=5,ipady=5,side='bottom')
start_button.pack(ipadx=5,ipady=5,side='bottom')
sourceport_button.pack(ipadx=5,ipady=5,side='bottom')
pick_button.pack(ipadx=5,ipady=5,side='bottom')
update_button.pack(ipadx=5,ipady=5,side='bottom')
download_button.pack(ipadx=5,ipady=5,side='bottom')
download_status_label.pack(ipadx=5,ipady=5,side='bottom')
sourceport_label.pack(ipadx=5,ipady=5,side='bottom')
sourceport_title_label.pack(ipadx=5,ipady=5,side='bottom')
directory_label.pack(ipadx=5,ipady=5,side='bottom')
directory_title_label.pack(ipadx=5,ipady=5,side='bottom')

root.mainloop()

