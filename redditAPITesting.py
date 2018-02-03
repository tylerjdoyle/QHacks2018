import praw

reddit = praw.Reddit(client_id='YlK5VB78FlL0Ug',
                     client_secret='uooOaERWpsVBF6pG-aENhD0SfrU',
                     password='QHACKS2018',
                     user_agent='topPostGatherer',
                     username='QHacks2018Project')

listing = reddit.subreddits.search('cryptocoin', limit=5)
for sub in listing:
    topPosts = sub.hot(limit=2)
    for post in topPosts:
        print(post.title)
