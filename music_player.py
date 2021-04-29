import tkinter as tk, re
from tkinter import filedialog
from pygame import mixer
from PIL import ImageTk, Image

class MusicPlayer:

    def __init__(self, master):
        self.master = master
        Play = tk.Button(self.master, text='Play', width=10, font=('Times', 10), bg='green', fg='white', command=self.play)
        Pause = tk.Button(self.master, text='Pause', width=10, font=('Times', 10), bg='brown', fg='white', command=self.pause)
        Stop = tk.Button(self.master, text='Stop', width=10, font=('Times', 10), bg='red', fg='white', command=self.stop)
        Play_list = tk.Button(self.master, text='Play List', width=10, font=('Times', 10), bg='green', fg='white',
                         command=self.play_list)
        Play.place(x=20, y=50), Pause.place(x=110, y=50), Stop.place(x=210, y=50), Play_list.place(x=110, y=90)
        self.music_file = False
        self.playing_state = False

    def play(self):
        self.music_file = filedialog.askopenfilename()
        print(type(self.music_file))
        file = self.music_file.split('/')
        # print(file)
        music_name = ''
        for n in file:
            if '.mp3' in n:
                music_name = n
        mixer.init()
        mixer.music.load(self.music_file)
        mixer.music.play()
        song_tag = tk.Label(self.master, text=f'Now Playing:\t{music_name}', fg='black', bg='gold')
        song_tag.place(x=0, y=0)

    def play_list(self):

        self.music_file = filedialog.askopenfilenames()
        print(self.music_file)
        names = []
        song_tag = None
        for m in self.music_file:
            for f in m.split('/'):
                if '.mp3' in f:
                    names.append(f)
        # print(names)
        mixer.init()
        for ind in range(len(self.music_file)):
            muse = self.music_file[ind]
            print(muse)
            mixer.music.load(muse)
            mixer.music.play()
        if song_tag:
            song_tag.place_forget()

        song_tag = tk.Label(self.master, text=f'Now Playing:\t{names[ind]}', fg='black', bg='gold')
        song_tag.place(x=0, y=0)

        tk.Button(self.master, text='Next', bg='black', fg='white',
                  command=self.next_muse(current_position=ind, song_list=names)).place(x=20, y=80)

    def next_muse(self, current_position, song_list):
        for num in range(len(self.music_file)):
            if num <= current_position:
                continue
            mixer.init()
            mixer.music.load(self.music_file[num])
            mixer.music.play()

            tk.Label(self.master, text=f'Now Playing:\t{song_list[num]}', fg='black', bg='gold').place(x=0, y=0)

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


root = tk.Tk()
# print(dir(root))

# file = 'C:\\Users\\welcome\\Desktop\\Logo\\PR_logo.png'
# img = ImageTk.PhotoImage(Image.open(file))
#
# root.iconphoto(file)

root.geometry('1200x200')
root.title('Beegie Player')
root.resizable(0, 0)
music_player = MusicPlayer(root)
root.mainloop()