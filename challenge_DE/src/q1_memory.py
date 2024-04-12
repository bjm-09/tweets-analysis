from typing import List, Tuple
from datetime import datetime
import json 
from collections import defaultdict
from memory_profiler import profile 
import time 

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Using a defaultdict we will have constant-time complexity when we insert values and perform lookups
    agg_dict = defaultdict(lambda: defaultdict(int))

    # try-catch in case the file doesn't exist or the path is wrong
    try:
        # Open json file with tweets data to loop through every record
        with open(file_path, 'r') as file:

            # By reading the file line by line we are avoiding unnecessary memory usage.
            for line in file:
                tweet = json.loads(line)
                
                # We are interested only on dates, not datetimes so we create a key for every date
                # We also create a key with every date-key with the username, as we need to keep track of how many 
                # tweets each user has on that specific day
                try:
                    date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
                    username = tweet['user']['username']
                    agg_dict[date][username] += 1

                except ValueError as e:
                    print(f"Error parsing date for tweet: {e}")
                    continue  # Skip this record and continue to the next one
        
        # Sort our dictionary by the total tweets, in descending order
        ## We sort the values only once, at the end
        top_10_dates = sorted(agg_dict.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

        # Previous step left us only with the 10 dates with most tweets
        ## Now we need to get the user with most tweets from each date to match the expected output
        return [(date, max(users, key=users.get)) for date, users in top_10_dates]

    except FileNotFoundError as e:
        return(f"File not found: {e}")


if __name__=='__main__':

    start_time = time.time()

    file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

    print(q1_memory(file_path=file_path))

    end_time = time.time()

    total_time = round(end_time - start_time , 2)

    print(f"The job finished running un {total_time} seconds.")