#goty_data_collection

#i could SQL to search through data??? maybe use this 
#maybe use regular epxression to help find names more specifically
#requesting information from reddit. For every submission requested, add info to 
# the set() allows for unique values and therefore can be run over time to get results over time
"""taken from praw documentation about not finding all comments "Finally, note that the value of 
submission.num_comments may not match up 100% with the number of comments extracted via PRAW. 
This discrepancy is normal as that count includes deleted, removed, and spam comments."""
#use linear regression to find relation between points
 
import praw
from praw.models import MoreComments
import time
import re 
from pathlib import Path
import json 

#for me to measure how long this takes to run
start_time = time.time()

#function definitions
#get the time of the post and add to a list but needs to be a list of dictionaries
def _get_unix_time(post):
    post_time = int(post.created_utc)       
    
    return post_time

#name of scrapper, client id and secret from my reddit account when the script was crated on reddit
user_agent = "looking_at_gaming_subreddit_for_game_of_the_year_comments by /Forest_Warden"

reddit = praw.Reddit(
    client_id = "0hL50W0v-njHL1rPyAvqeA",
    client_secret = "C_cWvvzqUeYKc77ZbkfsJlTDsNwMww",
    user_agent = user_agent,   
)

#making reddit object for a post
top_posts = reddit.subreddit('gaming').top(limit=None, time_filter="month") 

#list of dics containing key: bg_count, post_time
goty_info = []

#regular expressions compilation
game_of_the_year_word = re.compile("game of the year", re.IGNORECASE)
goty_word = re.compile("goty", re.IGNORECASE)

#iterate over post and for every post read every comment and store baldur's, and unix counters
for post in top_posts:

    #reseting biden and trump counters for every post
    goty_count = 0    

    #taking the time of the post
    u_time = _get_unix_time(post)

    #search through the post title for baldurs gate     
    game_of_the_year_list = re.findall(game_of_the_year_word, post.title)
    goty_list = re.findall(goty_word, post.title)

    #removing the "more comments" section of the post
    #also, the limit of 0 is important and greatly reduces the amount of api request!!
    post.comments.replace_more(limit=0)        

    #adding to baldurs gate count
    goty_count += len(game_of_the_year_list) + len(goty_list)
    
    for comment in post.comments.list():   
        #search through the comment for trump and biden     
        game_of_the_year_list = re.findall(game_of_the_year_word, comment.body)
        goty_list = re.findall(goty_word, comment.body)

        #adding to baldurs gate count
        goty_count += len(game_of_the_year_list) + len(goty_list)              

    #taking all the gathered info in a dictionary and appending it to the list of all information
    post_info = {
        'unix_time': u_time,
        'goty_count': goty_count,        
        } 
    goty_info.append(post_info)  

#saving data
path = Path("goty_info.json")
contents = json.dumps(goty_info)
path.write_text(contents)

for x in goty_info:    
    for keys, val in x.items():
        print(f"{keys} {val}, ", end='')
    print()

print(time.time() - start_time)


