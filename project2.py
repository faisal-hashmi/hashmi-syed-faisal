import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

pygame.mixer.init()

root = tk.Tk()
root.title("🎵 Naat Player")
root.geometry("600x600")
root.configure(bg="black")

def play_naat(file_path, title):
    """Play the selected naat"""
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        now_playing.config(text=f"▶ Now Playing: {title}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not play file:\n{e}")

def load_image(path, size=(80, 80)):
    """Load and resize an image safely"""
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Image not found:\n{path}")
        return None
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


naats = [
    ("Hasbi Rabbi", 
     r"C:\\Users\\faisa\\OneDrive\\Desktop\\mp3.py\\naat.png",
     r"C:\Users\faisa\OneDrive\Desktop\Naat.py\Hasbi-Rabbi-(HamariWeb.Com).mp3"),

    ("Faslon Ko Takaluf", 
     r"C:\Users\faisa\OneDrive\\Desktop\mp3.py\naat1.png", 
     r"C:\Users\faisa\OneDrive\\Desktop\Naat.py\faslon-ko-takkaluf.mp3"),

    ("Muhammad Nabina", 
     r"C:\Users\faisa\OneDrive\\Desktop\mp3.py\naat2.png", 
     r"C:\Users\faisa\OneDrive\\Desktop\Naat.py\muhammad-nabina.mp3"),

    ("Allah Humma Salli Ala", 
     r"C:\Users\faisa\OneDrive\\Desktop\mp3.py\naat3.png", 
     r"C:\Users\faisa\OneDrive\\Desktop\Naat.py\allah-humma-sallay-ala.mp3"),

    ("Maula Ya Salli Wa Sallim", 
     r"C:\Users\faisa\OneDrive\\Desktop\mp3.py\naat4.png", 
     r"C:\Users\faisa\OneDrive\\Desktop\Naat.py\maula-ya-salli-wa-sallim.mp3")
]

tk.Label(root, text="🎶 My Naat Playlist", font=("Arial", 20, "bold"), fg="white", bg="black").pack(pady=10)

songs_frame = tk.Frame(root, bg="black")
songs_frame.pack(pady=10)

images = []

#  Create rows (like Spotify style)
for title, img_path, file_path in naats:
    frame = tk.Frame(songs_frame, bg="#121212", padx=10, pady=5)
    frame.pack(fill="x", pady=5)

    img = load_image(img_path)
    if img:  # Only add if image exists
        images.append(img)
        tk.Label(frame, image=img, bg="#121212").pack(side="left")

    tk.Label(frame, text=title, font=("Arial", 14, "bold"), fg="white", bg="#121212").pack(side="left", padx=15)

    tk.Button(frame, text="▶ Play", font=("Arial", 12), bg="green", fg="white",
              command=lambda f=file_path, t=title: play_naat(f, t)).pack(side="right")


now_playing = tk.Label(root, text="▶ Now Playing: None", font=("Arial", 14), fg="yellow", bg="black")
now_playing.pack(pady=15)

root.mainloop()
 # some changes
