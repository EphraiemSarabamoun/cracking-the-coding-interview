import time

class Jukebox:
    def __init__(self, songs):
        self.songs = set(songs)
        self.playing = False
    def play(self):
        self.playing = True
        time.sleep(1)
        return
    def pick_song(self):
        response = input("Pick a song from the list: " + ", ".join(self.songs) + "\n")
        if response in self.songs:
            self.play()
        else:
            print("Song not found")
        return


if __name__ == "__main__":
    jukebox = Jukebox(["song1", "song2", "song3"])
    jukebox.pick_song()