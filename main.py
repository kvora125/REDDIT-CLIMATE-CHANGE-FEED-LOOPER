# Import required libraries
import os
x = os.system('pip install praw')
import praw

# Create a reddit instance
reddit = praw.Reddit(
    client_id='<Your client id>',
    client_secret='Your client Secret',
    username='Your username',
    password='Your Password',
    user_agent='Your user agent'
)

# Create another instance
subreddit = reddit.subreddit('climatechange')


# Create a function to show feed one by one
def reddit_climate_change_feed_looper():
    """Print the title and description of each reddit feed one by one
    
    Arguments: None
    
    Returns : None
    """
    # Select the subreddit of climatechange under the label "hot"
    hot_posts_climatechange = subreddit.hot(limit=100)

    # Initialise a flag variable (to mark the user's choice to continue or end program)
    flag = "y"
    # make an infinite loop to update feeds continuously with counter
    n = 0
    while True:
        # Loop across the posts to print them one by one.
        i = 1
        for post in hot_posts_climatechange:

            # This 'if' statement will ensure that, at least one post will be displayed
            if flag == "y":

                # Print the title of the reddit post
                print("news id: ", n * 100 + i)
                print(post.title)
                print("-" * 100)
                print("\n")
                # Print the description/content of the post
                print(post.selftext)
                print("=" * 100)
                print("\n")
                i = i + 1
                # Ask the user if he/she wants to continue viewing the next post or not
                flag = input("CONTINUE? (y/n) ")
                print("\n")

            # If the user chooses not to continue then exit the program with a Thanks message
            else:
                print("Thank you!")
                break
        # refresh feeds or exit based on user choice
        if flag == 'y':
            hot_posts_climatechange = subreddit.hot(limit=100)
            n = n + 1
        else:
            break


# main class (beginning of execution)
if __name__ == '__main__':
    # Calling the looper function to loop through the reddit posts
    reddit_climate_change_feed_looper()
