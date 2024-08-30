# Music Player

A simple yet powerful music player developed in Python, utilizing the PyQt5 framework for the GUI. The player supports features such as Dark Mode, Shuffle, Repeat, and displaying album covers through YouTube search.

## Prerequisites

Before using the music player, ensure that the following prerequisites are installed on your system:

- Python 3.x
- pip (Python package manager)

Additionally, you will need the following Python libraries:

- PyQt5
- pygame
- mutagen
- youtube-search-python
- pillow
- requests

## Installation

### Windows

1. **Install Python**: Ensure that Python 3.x is installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Create a virtual environment (optional)**:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the music player**:
   ```bash
   python main.py
   ```

### Ubuntu

1. **Install Python** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Create a virtual environment (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the music player**:
   ```bash
   python3 main.py
   ```

### Kali Linux

1. **Install Python** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Create a virtual environment (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the music player**:
   ```bash
   python3 main.py
   ```

### macOS

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```bash
   brew install python3
   ```

3. **Create a virtual environment (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the music player**:
   ```bash
   python3 main.py
   ```

## Usage

After installation and starting the program, you can:

- **Play music**: Select an MP3 file from the list and press "Play."
- **Shuffle songs**: Click "Shuffle" to randomize the playlist.
- **Repeat mode**: Toggle between "No Repeat," "Repeat One," and "Repeat All" modes.
- **Like a song**: Click "Like" to mark a song as a favorite.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
