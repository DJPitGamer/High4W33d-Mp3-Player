# High4W33d Mp3 Player

## Overview

The **High4W33d Mp3 Player** is a modern, visually appealing music player application built using Python and PyQt5. It provides a rich user interface with dark mode support, Discord Rich Presence integration, and functionalities like song playback, shuffle, repeat, and more. The player also fetches song covers from YouTube, making it a complete multimedia experience.

## Features

- **Dark Mode**: A sleek, dark-themed user interface.
- **Discord Rich Presence**: Display the currently playing song on your Discord profile.
- **YouTube Integration**: Automatically fetches and displays album covers from YouTube.
- **Playback Controls**: Play, pause, next, previous, shuffle, and repeat functionalities.
- **Progress Bar**: Displays the progress of the currently playing song.
- **Song List**: Displays all available songs in the directory.
- **Responsive UI**: The player is maximized on launch for an immersive experience.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- Install dependencies from the `requirements.txt`.
- A Discord application with a Client ID for Rich Presence (can be obtained from the [Discord Developer Portal](https://discord.com/developers/applications)).

## Installation

### Clone the Repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/DJPitGamer/High4W33d-Mp3-Player.git
cd High4W33d-Mp3-Player
```

### Set Up Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Edit the `.env` file and set your `DISCORD_CLIENT_ID`:

```env
DISCORD_CLIENT_ID=your_discord_client_id_here
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

- `PyQt5`
- `pygame`
- `mutagen`
- `youtube-search-python`
- `requests`
- `Pillow`
- `pypresence`
- `python-dotenv`

### Adding Your Music

Place your `.mp3` files in the `musik` directory located in the same directory as `main.py`. The player will automatically load and display them.

### Running the Application

You can run the application using:

```bash
python main.py
```

### Creating an Executable

To create an executable version of the application, you can use `PyInstaller`:

1. Install PyInstaller if you haven't already:

    ```bash
    pip install pyinstaller
    ```

2. Create the executable:

    ```bash
    pyinstaller --onefile --windowed --icon "cannabis.ico" --add-data "musik;musik" --add-data "no_cover.jpg;." --add-data "cannabis.ico;." --name High4W33d-MP3-Player main.py
    ```

   This will generate an executable in the `dist` directory.

### Customizing the Icon

To change the application icon, replace the `cannabis.ico` file in the project directory with your custom `.ico` file. Ensure it has the same name.

## Usage

### Playback Controls

- **Play/Pause**: Toggle playback of the selected song.
- **Next/Previous**: Navigate through your playlist.
- **Shuffle**: Randomize the order of songs in the playlist.
- **Repeat**: Toggle between no repeat, repeat one, and repeat all modes.

### Discord Integration

Ensure your Discord app is running. The player will automatically update your status with the current song.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
- [pygame](https://www.pygame.org/news)
- [mutagen](https://mutagen.readthedocs.io/en/latest/)
- [YouTube Search Python](https://pypi.org/project/youtube-search-python/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [pypresence](https://pypi.org/project/pypresence/)

---

*Developed by DJPitGamer*
