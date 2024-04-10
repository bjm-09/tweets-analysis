from typing import List, Tuple
import json
from emoji import EMOJI_DATA
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    
    # Counter objects provide time optimized methods
    emojis_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)

            # We save the tweet content in this text variable
            text = tweet['content']

            # We loop through the tweet text and append all emojis to a list
            emojis = [c for c in text if c in EMOJI_DATA.keys()]

            # Use the update method to feed the counter with the new data that we have collected
            emojis_counter.update(emojis)

    # Using the most_common method we retreive the top 10 most used emojis across all tweets
    return emojis_counter.most_common(10)