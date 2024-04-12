from typing import List, Tuple
import json
from emoji import EMOJI_DATA
from collections import Counter
from memory_profiler import profile 
import time 

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    # Counter objects provide time optimized methods like the one we will be using to get the most popular emojis
    emojis_counter = Counter()

    # try-catch in case the file doesn't exist or the path is wrong
    try:
        # Open json file with tweets data to loop through every record
        with open(file_path, 'r') as file:
            # By reading the file line by line we are avoiding unnecessary memory usage.
            for line in file:
                tweet = json.loads(line)

                # try-catch in case the content key does not exist
                try:
                    tweet = json.loads(line)
                    text = tweet['content']
                    # We loop through the tweet text and append all emojis to a list
                    # If it doesn't exist we move to the next tweet
                    emojis = [c for c in text if c in EMOJI_DATA.keys()]

                except KeyError:
                    print("Tweet does not have 'content' key.") 
                    continue

                # Use the update method to feed the counter with the new data that we have collected
                emojis_counter.update(emojis)

        # Use the most_common method we retreive the top 10 most used emojis across all tweets
        return emojis_counter.most_common(10)

    except FileNotFoundError as e:
        return(f"File not found: {e}")


if __name__=='__main__':

    start_time = time.time()

    file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

    print(q2_memory(file_path=file_path))

    end_time = time.time()

    total_time = round(end_time - start_time , 2)

    print(f"The job finished running un {total_time} seconds.")