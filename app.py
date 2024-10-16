import tkinter as tk
from tkinter import scrolledtext
import subprocess
from dotenv import load_dotenv
import os
import base64
from requests import post, get
from pytube import Search

# Load environment variables
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
youtube_api = os.getenv("YOUTUBE_API")

# Spotify functions
def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "playlist-modify-public"
    }

    response = post(url, headers=headers, data=data)
    response_data = response.json()

    return response_data["access_token"]

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def get_playlist_id_from_spotify_URL(Playlist_URL):
    split_1 = Playlist_URL.split("playlist/")[1]
    split_2 = split_1.split("?")[0]
    return split_2

def get_song_names_from_spotify_playlist(spotify_playlist_url, token):
    final_playlist_ID = get_playlist_id_from_spotify_URL(spotify_playlist_url)
    url = f"https://api.spotify.com/v1/playlists/{final_playlist_ID}/tracks"
    headers = get_auth_header(token)

    response = get(url, headers=headers)
    response_data = response.json()

    song_names = []
    for each in response_data['items']:
        song_name = each['track']['name']
        song_names.append(song_name)

    return song_names

# YouTube functions
def search_yt(song_names):
    search_results = []
    for each in song_names:
        s = Search(each)
        if s.results:
            search_results.append(s.results[0].watch_url)
    return search_results

# Download function for YouTube link
def download_video(youtube_link):
    if youtube_link:
        # Command to download the video
        command = f'yt-dlp -f bestaudio {youtube_link}'
        # Run the command in the terminal
        subprocess.run(command, shell=True)

# Tkinter application
def fetch_songs():
    # Fetch the playlist songs and YouTube links
    playlist_url = playlist_entry.get()
    token = get_token()
    song_names = get_song_names_from_spotify_playlist(playlist_url, token)
    youtube_urls = search_yt(song_names)

    # Clear previous results and buttons
    for widget in song_frame.winfo_children():
        widget.destroy()

    # Display the song names and YouTube URLs with buttons in the same row
    for i, song_name in enumerate(song_names):
        youtube_url = youtube_urls[i]
        
        # Label for the song name
        song_label = tk.Label(song_frame, text=f"{i + 1}. {song_name}")
        song_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
        
        # Button to download the song
        download_button = tk.Button(song_frame, text="Download", 
                                    command=lambda link=youtube_url: download_video(link))
        download_button.grid(row=i, column=1, padx=5, pady=5, sticky="e")

# Main window setup
root = tk.Tk()
root.title("Spotify to YouTube Download")

# Spotify playlist URL entry
playlist_label = tk.Label(root, text="Enter Spotify Playlist URL:")
playlist_label.pack(pady=10)

playlist_entry = tk.Entry(root, width=50)
playlist_entry.pack(pady=10, padx=10)

# Fetch songs button
fetch_button = tk.Button(root, text="Get Songs", command=fetch_songs)
fetch_button.pack(pady=10)

# Create a frame to hold the song names and buttons
song_frame = tk.Frame(root)
song_frame.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()