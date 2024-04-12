from typing import List, Tuple
import json
from functools import partial
from collections import Counter
from multiprocessing import Pool
from memory_profiler import profile 
import time

def get_mentions(line: str) -> Counter:

    mentions_counter = Counter()

    # We will pass the files' lines as argument when we run this function
    tweet = json.loads(line)

    # I found out that there is a mentionedUsers key with the tweet mentions so I will use that instead
    # of the regular expression that I used to have

    # If the key exists, we will loop through it to get all the usernames of the users mentioned in the tweet
    # If not we just ignore the tweet and do nothing with it
    if tweet['mentionedUsers']:

        # Loop through all mentioned users in the tweet
        for user in tweet['mentionedUsers']:

            # Increase that usernames counter by 1
            mentions_counter[user['username']] += 1

    return mentions_counter

def merge_counters(counters: List[Counter]) -> Counter:
    
    # Since we are parallelizing with pools, we need to merge all counters before calculating the top 10
    # So we will loop through the list of counters and update the one we're initializing here
    merged_counter = Counter()

    for counter in counters:
        merged_counter.update(counter)

    return merged_counter

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:

    with open(file_path, 'r') as file:

        # Create a pool of processes to run in parallel
        with Pool() as pool:

            # Apply the get_mentions function with file path argument
            process_line = partial(get_mentions)

            # Map the get_mentions function to each line in the file using the pool
            counters = pool.map(process_line, file)

        # Merge all counters together using the helper function
        mentions_counter = merge_counters(counters)

    # Use the most_common method we retreive the top 10 most mentioned users across all tweets
    return mentions_counter.most_common(10)


if __name__ == '__main__':
    start_time = time.time()

    file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

    print(q3_time(file_path=file_path))

    end_time = time.time()

    total_time = round(end_time - start_time , 2)

    print(f"The job finished running in {total_time} seconds.")
