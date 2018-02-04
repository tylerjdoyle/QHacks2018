import praw
import time

import pandas

reddit = praw.Reddit(client_id='YlK5VB78FlL0Ug',
                     client_secret='uooOaERWpsVBF6pG-aENhD0SfrU',
                     password='QHACKS2018',
                     user_agent='topPostGatherer',
                     username='QHacks2018Project')

startSept =   1501545600    # Sept 1st 2017
startYester = 1517529600    # Feb 2nd 2018
startJan = 1517356800

end = time.time()

def get_posts(start_time, end_time):
    
    submission_scores = []
    submission_titles = []
    comment_scores = []
    comment_bodies = []

    subreddits = [None] * 3
    
    subreddits[0] = reddit.subreddit('Monero')
    subreddits[1] = reddit.subreddit('BytecoinBCN')
    subreddits[2] = reddit.subreddit('Electroneum')

    day = 86400 # The number of seconds in a day.
    
    current_time = start_time

    while (current_time < end_time):
        
        print(current_time)
     
        for subreddit in subreddits:

            submissions = list(subreddit.submissions(current_time, current_time + day))

            end_submissions_loop = min(len(submissions), 10)
            for i in range(0, end_submissions_loop):
                
                comments = submissions[i].comments
                
                end_comments_loop = min(len(comments), 10)
                for j in range(0, end_comments_loop):

                    submission_scores.append(submissions[i].score)
                    submission_titles.append(submissions[i].title.encode("utf-8", errors="ignore"))
                    comment_scores.append(comments[j].score)
                    comment_bodies.append(comments[j].body.encode("utf-8", errors="ignore"))
            
            time.sleep(10)
            
        #end day.
        
        dataframe = pandas.DataFrame()
    
        dataframe['submission_scores'] = submission_scores
        dataframe['submission_titles'] = submission_titles
        dataframe['comment_scores'] = comment_scores
        dataframe['comment_bodies'] = comment_bodies
        
        dataframe.to_csv('subreddit_data.csv', index=False)
        
        current_time += day
    
get_posts(startSept, end)


