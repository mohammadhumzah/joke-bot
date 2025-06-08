# Joke Notifier 🤡

A Python script that sends a random dark two-part joke after fixed interval as a macOS notification.

## Features
- Fetches dark, two-part jokes from JokeAPI.
- Displays native macOS notifications using `terminal-notifier`.
- Can be run in the background with tools like `screen`.

## Requirements
- macOS
- Python 3.x
- `terminal-notifier` (install via Homebrew)
- Internet connection

## Setup Instructions (macOS only)

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/joke-bot.git
cd joke-bot
pip install -r requirements.txt
brew install terminal-notifier
python3 dark_joke.py

To keep the program running in after quitting the terminal, in terminal create a new screen session as;

screen -S joke_session
python3 dark_joke.py
# To detach from screen session: press Ctrl + A, then D

1. **After Quitting Terminal**

The program keeps running in background, to completely stop the script from running:
i. Open Terminal.
ii. Reattach the screen session.
iii. ```bash
  screen -r joke_session
  Ctrl + C
iv. After stopping script type, exit, to completely stop the program.

Your session is now fully closed.

## License

MIT License

2. The jokes can be really unhinged, i take no responsibility for them as they are fetched from a random api.


     

