# storage/save_story.py

import os
from datetime import datetime

def save_story_to_file(story_text):
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = "generated_stories"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"story_{date_str}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story_text)
    return file_path
