# Spotify to YouTube Playlist Downloader

This Python script allows users to download songs from their Spotify playlist by automating the process of fetching song names from a playlist, searching for them on YouTube, and downloading the corresponding audio. It's designed for users who use Spotify for free and want to download their custom playlists without needing a premium subscription.

## Features

- Fetches song names from any public Spotify playlist using Spotify's API.
- Searches for the song names on YouTube to find the closest match.
- Provides direct download buttons for each song from YouTube in high-quality audio.
- Offers a simple GUI interface built with `Tkinter`.
- Automates playlist-to-audio conversion and download, enabling offline listening for free.

## Prerequisites

Before running the script, make sure you have the following:

1. **Python 3.x** installed on your machine.
2. A **Spotify Developer Account** to obtain the Spotify API credentials (`client_id` and `client_secret`).
3. A `.env` file containing your Spotify API credentials.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Pramith08/Spotify-Playlist-Song-Downloader.git
   cd spotify-to-youtube-downloader

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Create a `.env` file in the project directory to fill API credentials:
   ```bash
   touch .env

4. Inside .env, add your API credentials:
   ```bash
   SPOTIFY_CLIENT_ID='your_spotify_client_id'
   SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
   
5. Run the Python script:
   ```bash
   python app.py

## Usage

1. **Enter your Spotify Playlist URL:** Copy the URL of any public Spotify playlist and paste it into the input field in the GUI.

2. **Fetch Songs:** Click the "Get Songs" button. The app will fetch the song names from Spotify and search for them on YouTube.

3. **Download Songs:** For each song in your playlist, the app will provide a download button next to the song name. Clicking the button will download the song from YouTube in high-quality audio.
   

