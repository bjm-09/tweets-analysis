from typing import List, Tuple
import json
from collections import Counter
import re 

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    
    mentions_counter = Counter()

    # Simple regular expression to find mentions within a tweet text. We're assuming all mentions are preceded by a white space
    ## and that are separate words. Not the most robust regular expression but it should do the trick for this excercise.
    mention_regex = "@\w+"

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)

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