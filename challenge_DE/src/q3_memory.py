from typing import List, Tuple
import json
from collections import Counter
from memory_profiler import profile 
import time 

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    
    mentions_counter = Counter()

    # I found out that there is a mentionedUsers key with the tweet mentions so I will use that instead
    # of the regular expression that I used to have
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)

            if tweet['mentionedUsers']:
                
                # Loop through all mentioned users in the tweet
                for user in tweet['mentionedUsers']:

                    # Increase that usernames counter by 1
                    mentions_counter[user['username']] += 1

    # Use the most_common method we retreive the top 10 most mentioned users across all tweets
    return mentions_counter.most_common(10)


if __name__=='__main__':

    start_time = time.time()

    file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

    print(q3_memory(file_path=file_path))

    end_time = time.time()

    total_time = round(end_time - start_time , 2)

    print(f"The job finished running un {total_time} seconds.")