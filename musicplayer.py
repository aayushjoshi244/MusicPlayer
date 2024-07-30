import os
import pygame
from pygame import mixer

# Initialize the mixer
mixer.init()

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_index = 0

    def add_song(self, song_path):
        if os.path.exists(song_path):
            self.playlist.append(song_path)
            print(f"Added {song_path} to playlist.")
        else:
            print(f"File {song_path} does not exist.")

    def remove_song(self, song_path):
        if song_path in self.playlist:
            self.playlist.remove(song_path)
            print(f"Removed {song_path} from playlist.")
        else:
            print(f"File {song_path} is not in the playlist.")

    def play(self):
        if self.playlist:
            song = self.playlist[self.current_index]
            mixer.music.load(song)
            mixer.music.play()
            print(f"Playing {song}")
        else:
            print("Playlist is empty.")

    def stop(self):
        mixer.music.stop()
        print("Music stopped.")

    def next_song(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()
        else:
            print("Playlist is empty.")

    def prev_song(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()
        else:
            print("Playlist is empty.")

def display_menu():
    print("\nMusic Player Menu:")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Play")
    print("4. Stop")
    print("5. Next song")
    print("6. Previous song")
    print("7. Display playlist")
    print("8. Exit")

def main():
    player = MusicPlayer()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            song_path = input("Enter the path to the song: ")
            player.add_song(song_path)
        elif choice == '2':
            song_path = input("Enter the path to the song to remove: ")
            player.remove_song(song_path)
        elif choice == '3':
            player.play()
        elif choice == '4':
            player.stop()
        elif choice == '5':
            player.next_song()
        elif choice == '6':
            player.prev_song()
        elif choice == '7':
            print("Playlist:")
            for index, song in enumerate(player.playlist):
                print(f"{index + 1}. {song}")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
