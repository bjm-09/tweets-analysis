from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
from memory_profiler import profile 

# With this function we will read the file one line at a time to optimize memory usage
def tweet_generator(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)


# In this function I reused the code for the q1_time with a few adjustments to use the helper function:
@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    agg_dict =  defaultdict(lambda: defaultdict(int))

    # Iterate through each tweet using the helper function and count tweets for each date
    for tweet in tweet_generator(file_path):

        # We are interested only on dates, not datetimes so we create a key for every date
        # We also create a key with every date-key with the username, as we need to keep track of how many tweets each user has
        try:
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()

        except ValueError as e:
            print(f"Error parsing date for tweet: {e}")
            continue  # Skip this record and continue to the next one

        username = tweet['user']['username']
        agg_dict[date][username] += 1

    # Sort our dictionary by the total tweets, in descending order
    ## We sort the values only once, at the end
    top_10_dates = sorted(agg_dict.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Previous step left us only with the 10 dates with most tweets
    ## Now we need to get the user with most tweets from each date to match the expected output
    return [(date, max(users, key=users.get)) for date, users in top_10_dates]

file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'


print(q1_memory(file_path=file_path))