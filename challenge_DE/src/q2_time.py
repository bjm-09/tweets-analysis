from typing import List, Tuple
import json
from emoji import EMOJI_DATA
from collections import Counter
from multiprocessing import Pool
from functools import partial
from memory_profiler import profile 
import time

def get_emojis(line: str) -> List[str]:

    # In case that it is possible that a tweet is generated without a content key. 
    # We are assuming every record of the file is a valid json object.
    # Otherwise, the json.loads() line should be treated separately but it seemed a bit extreme 
    try:
        tweet = json.loads(line)
        text = tweet['content']
        emojis = [c for c in text if c in EMOJI_DATA.keys()]
        return emojis
    except KeyError:

        # Unlike the memory function, here we need to return something with the same structure as
        # we would if the key does exist
        print("Tweet does not have 'content' key.")
        return []

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:

    # We will update this counter with the output of each pool so we can aggregate at the end
    emojis_counter = Counter()

    # try-catch in case the file doesn't exist or the path is wrong
    try:
        # Open json file with tweets data to loop through every record
        with open(file_path, 'r') as file:

            # Create a pool of processes to run in parallel
            with Pool() as pool:

                # Apply the get_emojis function with file path argument
                process_line = partial(get_emojis)

                # Map the get_emojis function to each line in the file using the pool
                results = pool.map(process_line, file)

            # Group the list of lists of emojis into a single list
            emojis = [emoji for sublist in results for emoji in sublist]

            # Use the update method to feed the counter with the new data that we have collected
            emojis_counter.update(emojis)

        # Use the most_common method we retreive the top 10 most used emojis across all tweets
        return emojis_counter.most_common(10)
    
    except FileNotFoundError as e:
        return(f"File not found: {e}")

        
if __name__=='__main__':

    start_time = time.time()

    file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

    print(q2_time(file_path=file_path))

    end_time = time.time()

    total_time = round(end_time - start_time , 2)

    print(f"The job finished running un {total_time} seconds.")