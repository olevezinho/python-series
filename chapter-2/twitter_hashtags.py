import tweepy

class Hashtags:
    def __init__(self, filename: str, array, logger, api):
        self.filename = filename
        self.array = array
        self.api = api
        self.logger = logger

    def read_tags(self, filename: str):
        # Read list of tags
        with open(filename, "r") as f:
            list_of_hashtags = list(f)
        return list_of_hashtags

    def write_tags(self, filename: str, array):
        # Write list of tags
        with open(filename, 'w') as f:
            for data in array:
                for trends in data['trends']:
                    #print(trends['name'])
                    f.write(trends['name']+'\n')
        return None

    def like_tags(self, api, logger, hashtags):
    # Count likes
        count = 0
        try:
        # search for topics in a list of hashtags
            for i in hashtags:
                logger.info(f"tweets about {i}")
                # search for the tweets related to a specific topic
                for tweet in api.search_tweets(q=i, lang="en"):
                # the status contains all information about a specific tweet, like date_of_creation, author name, etc
                    status = api.get_status(tweet.id)
                    # fetching the favorited attribute
                    favored = status.favorited
                    # if already liked, then skip
                    if favored == True:
                        logger.info("The authenticated user already liked the tweet.")
                    # else like the tweet
                    else:
                        logger.info(f"tweet id: [{tweet.id}] tweeted at: [{status.created_at}]")
                        api.create_favorite(tweet.id)
                        count += 1
                        logger.info("The tweet was favored!")
        except tweepy.TweepyException as e:
            logger.error(e)
            logger.info(f"{count} tweets favored!")
            logger.exception(e.with_traceback())
        return None