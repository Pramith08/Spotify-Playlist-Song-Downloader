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
3. A **YouTube Data API key** to perform YouTube searches.
4. A `.env` file containing your Spotify API credentials and YouTube API key.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/spotify-to-youtube-downloader.git
   cd spotify-to-youtube-downloader
2. Install the required Python dependencies:
