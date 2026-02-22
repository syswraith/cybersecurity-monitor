import requests
import json

class PicoCTF:
    def __init__(self, username):
        self.username = username
        
        # Get user ID
        id_res = requests.get(f"https://play.picoctf.org/api/users/{self.username}/")
        if id_res.status_code != 200:
            raise Exception(f"PicoCTF user '{username}' not found or API error (Status: {id_res.status_code})")
            
        data = id_res.json()
        if "id" not in data:
            raise Exception(f"Invalid PicoCTF response for '{username}': missing 'id'")
        self.id = data["id"]

        # Get stats
        stats_res = requests.get(f"https://play.picoctf.org/api/users/{self.id}/gym_stats/")
        if stats_res.status_code != 200:
            raise Exception(f"Could not fetch gym stats for PicoCTF ID {self.id}")
            
        self.stats = stats_res.json()


        self.easy_solved = self.stats["by_difficulty"]["1"]["solved"]
        self.easy_total = self.stats["by_difficulty"]["1"]["available"]
        self.easy_percent = self.easy_solved * 100 // self.easy_total

        self.medium_solved = self.stats["by_difficulty"]["2"]["solved"]
        self.medium_total = self.stats["by_difficulty"]["2"]["available"]
        self.medium_percent = self.medium_solved * 100 // self.medium_total

        self.hard_solved = self.stats["by_difficulty"]["3"]["solved"]
        self.hard_total = self.stats["by_difficulty"]["3"]["available"]
        self.hard_percent = self.hard_solved * 100 // self.hard_total


    def get_profile_embed(self):
        desc = (
                f"Easy ({self.easy_percent}%) : **{self.easy_solved}** / {self.easy_total}\n"
                f"Medium ({self.medium_percent}%): **{self.medium_solved}** / {self.medium_total}\n"
                f"Hard ({self.hard_percent}%): **{self.hard_solved}** / {self.hard_total}\n"
                f"Profile URL: https://play.picoctf.org/users/{self.username}" 
                )

        embed = {
                "title": f"PicoCTF Profile: {self.username}",
                "description": desc,
                "color": 0x00ff00
                }

        return embed

