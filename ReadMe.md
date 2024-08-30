# Music Player

Ein einfacher, aber leistungsstarker Musikplayer, der in Python entwickelt wurde und das PyQt5-Framework für die GUI verwendet. Der Player unterstützt Funktionen wie Dark Mode, Shuffle, Repeat und die Anzeige von Album-Covern durch YouTube-Suche.

## Voraussetzungen

Bevor du den Musikplayer verwendest, stelle sicher, dass die folgenden Voraussetzungen auf deinem System installiert sind:

- Python 3.x
- pip (Python-Paketmanager)

Zusätzlich benötigte Python-Bibliotheken:

- PyQt5
- pygame
- mutagen
- youtube-search-python
- pillow
- requests

## Installation

### Windows

1. **Python installieren**: Stelle sicher, dass Python 3.x installiert ist. Du kannst es von der [offiziellen Python-Website](https://www.python.org/downloads/) herunterladen.

2. **Virtuelle Umgebung erstellen (optional)**:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Musikplayer starten**:
   ```bash
   python main.py
   ```

### Ubuntu

1. **Python installieren** (falls nicht bereits installiert):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Virtuelle Umgebung erstellen (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Musikplayer starten**:
   ```bash
   python3 main.py
   ```

### Kali Linux

1. **Python installieren** (falls nicht bereits installiert):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Virtuelle Umgebung erstellen (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Musikplayer starten**:
   ```bash
   python3 main.py
   ```

### macOS

1. **Homebrew installieren** (falls nicht bereits installiert):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Python installieren**:
   ```bash
   brew install python3
   ```

3. **Virtuelle Umgebung erstellen (optional)**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Musikplayer starten**:
   ```bash
   python3 main.py
   ```

## Benutzung

Nach der Installation und dem Start des Programms kannst du:

- **Musik abspielen**: Wähle eine MP3-Datei aus der Liste aus und drücke "Play".
- **Songs shufflen**: Drücke auf "Shuffle", um die Wiedergabeliste zu mischen.
- **Repeat-Modus**: Wechsle zwischen den Repeat-Modi "No Repeat", "Repeat One", und "Repeat All".
- **Song liken**: Klicke auf "Like", um einen Song als Favoriten zu markieren.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die `LICENSE`-Datei für weitere Informationen.
