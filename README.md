# Cybersecurity Monitor

A script to fetch updates from cybersecurity platforms and post it to Discord!

## Platforms currently supported are:
- TryHackMe
- PicoCTF

## How to run

### Project layout
```
.
├── main.py
├── platforms
│   ├── __init__.py
│   ├── picoctf.py
│   └── tryhackme.py
├── README.md
└── requirements.txt

2 directories, 6 files
```

### Instructions
1. Git clone the repository
2. Set the `webhook_url` in the `main.py` file.
3. Create a folder named `profiles` and add json files with the following structure.
```json
{
    "discord": "98793298415351819",
    "picoctf": "syswraith",
    "tryhackme": "syswraith"
}
```

- Replace the value of the `discord` key with your Discord ID. [Where can I find my Discord ID?](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID).
- Replace the other fields with your username on the platforms.

Contributions are welcome!
