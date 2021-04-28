import pandas as pd
import praw
from psaw import PushshiftAPI

#do not run without filling out credentials
r = praw.Reddit(client_id='client id',
                client_secret='client secret',
                user_agent='user agent')
	
api = PushshiftAPI(r)

def get_reddit_data(subreddit, post_limit = 100, timestamp = None):
	if timestamp !=None:
		timestamp=int(timestamp) 
	
	new_submissions = list(api.search_submissions(after=timestamp, subreddit=subreddit, limit=post_limit))
	
	comments = []
	users = []
	for submission in new_submissions:
	#collect post data     
		comments.append({'id': submission.id, 'author': submission.author, 'body': submission.title, 'created_at': submission.created_utc, 'score': submission.score, 'url': submission.url, 'parent_id': None, 'num_comments': submission.num_comments, 'upvote_ratio': submission.upvote_ratio})
		submission.comments.replace_more(limit=None) # Goes to website
		for comment in submission.comments.list():
			comments.append({'id': comment.id, 'author': comment.author, 'body': comment.body, 'created_at': comment.created_utc, 'score': comment.score, 'url': None, 'parent_id': comment.parent_id, 'num_comments': None, 'upvote_ratio': None})
	
	#collect user data
		user = submission.author
		try:
			users.append({"comment_author": user.name, "karma": user.comment_karma, "created_at": user.created_utc})
		except:
			pass		
		for comment in submission.comments.list():
			try:
				users.append({"comment_author": comment.author.name, "karma": comment.author.comment_karma, "created_at": comment.author.created_utc})
			except:
				pass

	post_data = pd.DataFrame(comments)
	user_data = pd.DataFrame(users)
	
	user_data.drop_duplicates(inplace=True)

	return post_data, user_data

if __name__ == "__main__":
	post_data, user_data = get_reddit_data("cscareerquestions") #input w subreddit of choice