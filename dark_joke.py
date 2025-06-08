import requests
import json
import time
import subprocess


def get_dark_joke():
    """
    Fetches a two-part dark joke from JokeAPI.
    Returns the joke as a combined string (setup + delivery).
    """
    url = "https://v2.jokeapi.dev/joke/Dark,Pun?type=twopart"
    response = requests.get(url)
    data = response.json()

    # Format the joke (setup and delivery parts)
    return f"{data['setup']}\n{data['delivery']}"


def main():
    """
    Main function to get a joke and show notification.
    """
    while True:
        joke = get_dark_joke()
        notify_mac("Joke Bot", joke)
        time.sleep(30)


def notify_mac(title, message):     # title is joke bot, message is the joke from def main
    """
    Uses terminal-notifier to show a macOS notification with given title and message.
    """
    subprocess.run([
        "/opt/homebrew/bin/terminal-notifier",
        "-title", title,
        "-message", message,
        "-appIcon", "/Users/mohammadhumzah/Downloads/icon.png"
    ])


if __name__ == "__main__":
    main()
