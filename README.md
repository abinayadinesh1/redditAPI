# redditAPI
gets data for all of the comments and posts for a specified subreddit
- collects id, author, title, body, created_at, comment score (), number of comments for each post, upvote ratio
- uses psaw to collect all of these posts from pushshift (searches through externally stored reddit posts/comments) (con: not real time)

*logistical differences between posts and comments- treated the same way but have slightly varying attributes

# to use
1. download 
2. update credentials
3. update script for preferred subreddit
4. run file in command line
