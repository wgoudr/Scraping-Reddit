This project was made to find if there was any correlation between the number of times the keywords "Baldur's Gate 3" and the number of times "game of the year" appeared in the gaming subreddit. Since Baldur's Gate 3 was such a success at the launch, I thought it had the potential to be the game of the year. I decided to figure out if I could predict this by finding the number of times specific keywords were mentioned in the comments and finding the correlation between them. I looked at the top Reddit posts in the past month, since they usually have the most comments, and decided to run my program within that time frame. 

After getting the results from the regression model, I got an R-squared value of 0.1511. I could rerun the program over a longer period of time, over a more recent period, or any other combination, but the results may completely change. However, this r-squared value needs to be compared to other values, as this is not enough to form any meaningful conclusions. Although you can't conlude anything from the results, I beleive, in my unhumble opinion, this r-squared value is good enough. Considering there are many other possible variables to account for, the value 0.1511 is a strong indication of some sort relationship. Therefore, I predict that Baldur's Gate 3 will receive the GOTY award. 

Saved files of the collected data, and images of the graphed results are provided in the repo. Copies are there as well. The main files for this project, are in order of execution. The data collection program DOES NOT need to be run again, as it takes almost 2 hours to run. This happens because requesting information from Reddit too quickly will cause Reddit to stop your requests. Another thing that takes time is Reddit loading each nested comment. Here are the main files:

bg3_goty_data_collection:   This is the first program. It sends a request to Reddit, collects keywords, and saves it.

organizing_bg_data: This program organizes the data and processes it in chronological order.

bg_to_goty_regression:  This program uses a linear regression model using the least squares method to find the correlation between       the data points. The model and data are then graphed.

