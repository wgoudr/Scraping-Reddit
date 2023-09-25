# baldur's gate and goty data collection

# NO NEED TO RUN THIS RPOGRAM AGAIN. it will override saved data and will
# cause the data to be taken from a different time frame, which changes the analysis.
# This program also takes a long time to run. (made a copy of data in case anything happens)

# In short, this program sends requests to Reddit, asking for comment information for a set 
# of posts, within a specified timeframe. This information is stored in a list of dics
# and will be processed in another file.
 
import praw
from praw.models import MoreComments
import time
import re 
from pathlib import Path
import json 

#for my own purpose to measure how long this takes to run
start_time = time.time()

#function definitions
#get the time of the post and add to a list, but needs to be converted to an int
#or else sorting doesnt work properly
def _get_unix_time(post):
    post_time = int(post.created_utc)       
    
    return post_time

# name of scraper, a user agent is a unique identifier that helps 
# Reddit determine the source of network requests.
user_agent = "checking_comments_for_bg_and_goty"

# creating a reddit instance. Instances of this class 
# are the gateway to interacting with Reddit's API through PRAW.
reddit = praw.Reddit(
    client_id = "0hL50W0v-njHL1rPyAvqeA",
    client_secret = "C_cWvvzqUeYKc77ZbkfsJlTDsNwMww",
    user_agent = user_agent, 
    ratelimit_seconds = 120  
)

#making a reddit object, for the gaming subreddit and for the top posts in the past month
top_posts = reddit.subreddit('gaming').top(limit=None, time_filter="month") 

#list of dictionaries containing keys: bg_count, post_time
baldursgate_goty_data = []

# regular expressions compilation for baldur's gate keyword
# it needs to be compiled into an object before using regex functions 
# any combination of baldur's gate capitalized or not
baldurs_word = re.compile("baldurs gate", re.IGNORECASE)
baldur_s_word = re.compile("baldur's gate", re.IGNORECASE)

# regular expressions compilation, for game of the year keyword 
# any combination of game of the year or goty, capitalized or not
game_of_the_year_word = re.compile("game of the year", re.IGNORECASE)
goty_word = re.compile("goty", re.IGNORECASE)

# iterate over every post and for every post read every 
# comment and store baldur's gate, goty, and unix counters
for post in top_posts:

    # reseting counters for every post
    bg_count = 0 
    goty_count = 0   

    # taking the time (time measured in unix) of the post
    u_time = _get_unix_time(post)

    # search through the post title for baldurs gate, and goty 
    # keywords and adding to baldurs gate and goty list 
    baldurs_gate_list = re.findall(baldurs_word, post.title)
    baldur_s_gate_list = re.findall(baldur_s_word, post.title)    
    game_of_the_year_list = re.findall(game_of_the_year_word, post.title)
    goty_list = re.findall(goty_word, post.title)

    #adding legnth of list to baldurs gate count
    bg_count += len(baldurs_gate_list) + len(baldur_s_gate_list)   
    goty_count += len(game_of_the_year_list) + len(goty_list)

    #removing the "more comments" section of the post
    #this allows the program to request post information for posts 
    #in the "more comments" section
    #also, the limit of 0 is important and greatly reduces the amount of requests!! (instead of =None)
    post.comments.replace_more(limit=0)       
    
    #for every comment, there are sub comments withing comments, so we do this 
    #to look at every single comment
    for comment in post.comments.list(): 

        #search through the comments for baldurs gate and goty keywords
        # same as previously but in comments rather than in the title    
        baldurs_gate_list = re.findall(baldurs_word, comment.body)
        baldur_s_gate_list = re.findall(baldur_s_word, comment.body)        
        game_of_the_year_list = re.findall(game_of_the_year_word, comment.body)
        goty_list = re.findall(goty_word, comment.body)

        #adding to baldurs gate and goty count
        bg_count += len(baldurs_gate_list) + len(baldur_s_gate_list) 
        goty_count += len(game_of_the_year_list) + len(goty_list)           

    #taking all the gathered info in a dictionary and appending it to the list of all information
    #you need to do this before going to the next post, because counters reset. 
    post_info = {
        'unix_time': u_time,
        'bg_count': bg_count, 
        'goty_count': goty_count       
        } 
    
    # this list is what will be processed later, and is a list of dictionaries
    baldursgate_goty_data.append(post_info)  

# saving data, so we can run this program only once.
# Includes baldur's gate and goty information
path = Path("baldursgate_goty_data.json")
contents = json.dumps(baldursgate_goty_data)
path.write_text(contents)

for x in baldursgate_goty_data:    
    for keys, val in x.items():
        print(f"{keys} {val}, ", end='')
    print()

print(time.time() - start_time)


