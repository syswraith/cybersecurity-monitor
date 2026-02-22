import requests
import json

class TryHackMe:
    def __init__(self, username):
        self.username = username
        response = requests.get(f"https://tryhackme.com/api/v2/public-profile?username={self.username}")
        
        if response.status_code != 200:
            raise Exception(f"TryHackMe user '{username}' not found or API error (Status: {response.status_code})")
            
        json_data = response.json()
        if "data" not in json_data:
             raise Exception(f"Invalid TryHackMe response for '{username}': missing 'data' field")
             
        self.profile = json_data["data"]



    def get_profile(self):
        return {
                "rank": self.profile["rank"],
                "top": self.profile["topPercentage"],
                "level": self.profile["level"],
                "badges": self.profile["badgesNumber"],
                "streak": self.profile["streak"],
                "completed": self.profile["completedRoomsNumber"],
                "profile": f"https://tryhackme.com/p/{self.username}"
                }

    def get_profile_embed(self):
        desc = (
                f"Rank: **{self.profile['rank']}**\n"
                f"Top %: **{self.profile['topPercentage']}**\n"
                f"Level: **{self.profile['level']}**\n"
                f"Badges: **{self.profile['badgesNumber']}**\n"
                f"Streak: **{self.profile['streak']}**\n"
                f"Completed Rooms: **{self.profile['completedRoomsNumber']}**\n"
                f"Profile URL: https://tryhackme.com/p/{self.username}\n"
                )

        embed = {
                "title": f"TryHackMe Profile: {self.profile['username']}",
                "thumbnail": {"url": self.profile["avatar"]},
                "description": desc,
                "color": 0x00ff00
                }

        return embed
