from typing import List, Tuple
import json
from collections import Counter
import re 
from memory_profiler import profile 


# With this function we will read the file one line at a time to optimize memory usage
def tweet_generator(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    
    mentions_counter = Counter()

    # Simple regular expression to find mentions within a tweet text. We're assuming all mentions are preceded by a white space
    ## and that are separate words. Not the most robust regular expression but it should do the trick for this excercise.
    mention_regex = "@\w+"

    with open(file_path, 'r') as file:
        
        for tweet in tweet_generator(file_path):

            # We save the tweet content in this text variable
            text = tweet['content']

            # Asuming that the words separator in the tweet text is always a white space.
            words = text.split()

            # Store mentions in this list. We remove the '@' to match the statement requirement.
            mentions = [w[1:] for w in words if re.match(mention_regex, w)]

            #Use the update method to feed the counter with the new data that we have collected
            mentions_counter.update(mentions)

    # Using the most_common method we retreive the top 10 most mentioned users across all tweets
    return mentions_counter.most_common(10)

file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'


print(q3_memory(file_path=file_path))