import praw
import time

import pandas

reddit = praw.Reddit(client_id='YlK5VB78FlL0Ug',
                     client_secret='uooOaERWpsVBF6pG-aENhD0SfrU',
                     password='QHACKS2018',
                     user_agent='topPostGatherer',
                     username='QHacks2018Project')

startSept =   1501545600 # Sept 1st 2017
startYester = 1517529600 # Feb 2nd 2018
startJan = 1517356800

end = time.time()


def func() :
    listing = reddit.subreddits.search('cryptocoin', limit=5)
    for sub in listing:
        topPosts = sub.hot(limit=2)
        for post in topPosts:
            print(post.title)

# sorted(reddit.subreddit('ucsb').submissions(), key=lambda x: -x.score)
def getPosts(startTime, endTime):

    listing = [None]*3
    listing[0] = reddit.subreddit('cats')
    listing[1] = reddit.subreddit('whales')
    listing[2] = reddit.subreddit('monkeys')

    day = 86400
    currentStart = startTime
    currentEnd = startTime + day
    
    while (currentStart < endTime):        
        
        for sub in listing:

            # This will sort the posts in a given day by score (Top scores first)
            posts = sorted(sub.submissions(currentStart, currentEnd), key=lambda x: -x.score)

            # In case there are less than 10 posts in a day
            endPostLoop = min(len(posts), 10)
        
            for i in range(0, endPostLoop):

                # Display the top 10 posts in a day
                print(posts[i].score, posts[i].title.encode("utf-8", errors='ignore'))

                # Sort the comments by score (Top scores first)
                comments = sorted(posts[i].comments, key=lambda x: -x.score)

                # In case there are less than 10 comments in a post
                endCommentLoop = min(len(comments), 10)

                for j in range(0, endCommentLoop):

                    # Display the top 10 commenton a post
                    a = 1 # remove this once the printing is in place
                    #print(comments[j].score, comments[j].body.encode("utf-8", errors='ignore'))

                # Distinguish the next post
                print("END POST")
            # Distinguish the next sub
            print("END SUB")
            time.sleep(10)
        # Distinguish the next day
        print("END DAY")
                
        currentStart = currentEnd
        currentEnd += day

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

                    subreddit_titles.append(subreddit.title.encode("utf-8", errors="ignore"))
                    submission_titles.append(submissions[i].title.encode("utf-8", errors="ignore"))
                    comment_bodies.append(comments[j].body.encode("utf-8", errors="ignore"))
            
            time.sleep(5)
            
        #end day.
        
        dataframe = pandas.DataFrame()

        dataframe['subreddit_titles'] = subreddit_titles
        dataframe['submission_titles'] = submission_titles
        dataframe['comment_bodies'] = comment_bodies
        
        dataframe.to_csv('subreddit_data.csv', index=False)
        
        current_time += day
    
#get_posts(startSept, end)

def getMorePosts():

    submission_titles = []
    comment_bodies = []
    
    listing = [None]*3
    subreddits[0] = reddit.subreddit('Monero')
    subreddits[1] = reddit.subreddit('BytecoinBCN')
    subreddits[2] = reddit.subreddit('Electroneum')
    
    currentTime = time.time()
    startTime = currentTime - 600 #10 mins in past

    for sub in listing:
        
        posts = sub.submissions(startTime, currentTime)
        
        for post in posts:

            print(post.score, post.title.encode("utf-8", errors='ignore'))

            comments = post.comments

            for comment in comments:

                submission_titles.append(sub.title.encode("utf-8", errors="ignore"))
                comment_bodies.append(comment.body.encode("utf-8", errors="ignore"))


    dataframe = pandas.DataFrame()
    
    dataframe['submission_titles'] = submission_titles
    dataframe['comment_bodies'] = comment_bodies
        
    dataframe.to_csv('subreddit_data.csv', index=False)



#getMorePosts()

#getPosts(startJan, end)


