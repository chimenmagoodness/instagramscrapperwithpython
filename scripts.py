# Import the module
import instaloader

num = int(input("how many hashtags do you want to search for? \npleas enter an number eg. 10: ").strip())
# Define the hashtags to scrape
hashtags = input("please input hashtags without spaces and separated by commas eg. clothes,newyork,walmart: ").split(",")

# Create an instance
L = instaloader.Instaloader()


# Loop through the hashtags
for hashtag in hashtags:
    # Get the posts for the hashtag
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

    # Loop through the posts
    for post in posts:
        # Print the post information
        print(f"Hashtag: {hashtag}")
        print(f"Post ID: {post.shortcode}")
        print(f"Date: {post.date_utc}")
        print(f"Caption: {post.caption}")
        print(f"Likes: {post.likes}")
        print(f"Comments: {post.comments}")

        # Download the post media
        L.download_post(post, target=f"{hashtag}")

        # Break after 10 posts per hashtag
        break
