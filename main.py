import os
import json
import requests
import traceback
from platforms import PicoCTF, TryHackMe

if __name__ == "__main__":
    webhook_url = "enter webhook url here"
    
    # Use absolute path for profiles directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    profile_path = os.path.join(script_dir, "profiles")
    
    if not os.path.exists(profile_path):
        print(f"Error: Profile directory not found at {profile_path}")
        exit(1)

    # Filter for .json files to avoid crashing on hidden files or READMEs
    users = [f for f in os.listdir(profile_path) if f.endswith('.json')]

    for user in users:
        try:
            full_path = os.path.join(profile_path, user)
            with open(full_path, 'r') as file:
                profile = json.load(file)
                
                discord_id = profile.get("discord")
                if not discord_id:
                    print(f"Skipping {user}: No discord ID found.")
                    continue
                
                mention = f"<@{discord_id}>"
                embeds = []

                if "picoctf" in profile.keys():
                    try:
                        picoctf = PicoCTF(profile["picoctf"])
                        embeds.append(picoctf.get_profile_embed())
                    except Exception as e:
                        print(f"Error fetching PicoCTF for {user}: {e}")

                if "tryhackme" in profile.keys():
                    try:
                        tryhackme = TryHackMe(profile["tryhackme"])
                        embeds.append(tryhackme.get_profile_embed())
                    except Exception as e:
                        print(f"Error fetching TryHackMe for {user}: {e}")

                for embed in embeds:
                    res = requests.post(webhook_url, json={"content": mention, "embeds": [embed]})
                    res.raise_for_status()
                    
        except Exception as e:
            print(f"Fatal error processing user file {user}:")
            traceback.print_exc()


