{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# INST728E - Module 4. Collecting Social Media Data\n",
    "\n",
    "This notebook contains examples for using web-based APIs (Application Programmer Interfaces) to download data from social media platforms.\n",
    "Our examples will include:\n",
    "\n",
    "- Reddit\n",
    "- Facebook\n",
    "- Twitter\n",
    "\n",
    "For most services, we need to register with the platform in order to use their API.\n",
    "Instructions for the registration processes are outlined in each specific section below.\n",
    "\n",
    "We will use APIs because they *can* be much faster than manually copying and pasting data from the web site, APIs provide uniform methods for accessing resources (searching for keywords, places, or dates), and it should conform to the platform's terms of service (important for partnering and publications).\n",
    "Note however that each of these platforms has strict limits on access times: e.g., requests per hour, search history depth, maximum number of items returned per request, and similar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "import json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/RedditLogo.jpg\" width=\"20%\">\n",
    "\n",
    "## Topic 2.1: Reddit API\n",
    "\n",
    "Reddit's API used to be the easiest to use since it did not require credentials to access data on its subreddit pages.\n",
    "Unfortunately, this process has been changed, and developers now need to create a Reddit application on Reddit's app page located here: (https://www.reddit.com/prefs/apps/)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "# For our first piece of code, we need to import the package \n",
    "# that connects to Reddit. Praw is a thin wrapper around reddit's \n",
    "# web APIs and works well\n",
    "\n",
    "import praw"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating a Reddit Application\n",
    "Go to https://www.reddit.com/prefs/apps/.\n",
    "Scroll down to \"create application\", select \"web app\", and provide a name, description, and URL (which can be anything).\n",
    "\n",
    "After you press \"create app\", you will be redirected to a new page with information about your application. Copy the unique identifiers below \"web app\" and beside \"secret\". These are your client_id and client_secret values, which you need below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/reddit_screens/0-001.png\" scale=\"10%\"/>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/reddit_screens/1-002.png\" scale=\"20%\"/>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/reddit_screens/1-003a.png\" scale=\"10%\"/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now we specify a \"unique\" user agent for our code\n",
    "# This is primarily for identification, I think, and some\n",
    "# user-agents of bad actors might be blocked\n",
    "redditApi = praw.Reddit(client_id='OdpBKZ1utVJw8Q',\n",
    "                        client_secret='KH5zzauulUBG45W-XYeAS5a2EdA',\n",
    "                        user_agent='crisis_informatics_v01')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Capturing Reddit Posts\n",
    "\n",
    "Now for a given subreddit, we can get the newest posts to that sub. \n",
    "Post titles are generally short, so you could treat them as something similar to a tweet."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jeff Bezos is the richest person in history\n",
      "Collapse of Huawei-AT&T deal ‘will threaten China-US trade ties’\n",
      "Julian Assange's stay in London embassy untenable, says Ecuador\n",
      "Israeli PM Netanyahu’s son, seeking cash for stripper, brags of US$20billion deal for friend’s father\n",
      "World Health Organization to declare gaming addiction a mental disorder.\n",
      "Fusion GPS: Trump-Russia firm chief's transcript released\n",
      "‘Swatting’ suspect Tyler Barriss now has warrants issued in Calgary, Canada\n",
      "Facebook has settled a landmark legal action case in which a 14-year-old girl sued Facebook, after a man allegedly posted a naked photo of her on the website\n",
      "World Bank issues warnings on interest rates and inflation | Business\n",
      "Germany's Foreign Minister: 'We Are Seeing What Happens When the U.S. Pulls Back'\n"
     ]
    }
   ],
   "source": [
    "subreddit = \"worldnews\"\n",
    "\n",
    "targetSub = redditApi.subreddit(subreddit)\n",
    "\n",
    "submissions = targetSub.new(limit=10)\n",
    "for post in submissions:\n",
    "    print(post.title)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Leveraging Reddit's Voting\n",
    "\n",
    "Getting the new posts gives us the most up-to-date information. \n",
    "You can also get the \"hot\" posts, \"top\" posts, etc. that should be of higher quality. \n",
    "In theory.\n",
    "__Caveat emptor__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "North Korea to join Olympics in South Korea\n",
      "Trump-Russia: Senator Dianne Feinstein releases testimony of dossier firm boss\n",
      "Plastic microbeads can no longer be used in cosmetics and personal care products in the UK, after a long-promised ban came into effect on Tuesday. The ban initially bars the manufacture of such products and a ban on sales will follow in July.\n",
      "Heartbroken scientists lament the likely loss of ‘most of the world’s coral reefs’: 'Scientists surveyed 100 reefs around the world and found that extreme bleaching events that once occurred every 25 or 30 years now happen about every five or six years.'\n",
      "Russian historian who exposed Stalin's crimes faces enforced psychiatric testing\n"
     ]
    }
   ],
   "source": [
    "subreddit = \"worldnews\"\n",
    "\n",
    "targetSub = redditApi.subreddit(subreddit)\n",
    "\n",
    "submissions = targetSub.hot(limit=5)\n",
    "for post in submissions:\n",
    "    print(post.title)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Following Multiple Subreddits\n",
    "\n",
    "Reddit has a mechanism called \"multireddits\" that essentially allow you to view multiple reddits together as though they were one.\n",
    "To do this, you need to concatenate your subreddits of interesting using the \"+\" sign."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jeff Bezos is the richest person in history Petroleum-Engineer\n",
      "Democratic Senators clear key hurdle to voting against the FCC's repeal of Net Neutrality itsBonez\n",
      "Collapse of Huawei-AT&T deal ‘will threaten China-US trade ties’ dcismia\n",
      "A friend of Kurt Cobain made Demotapes from Nirvana public that Kurt gave him. DJKaito\n",
      "Julian Assange's stay in London embassy untenable, says Ecuador TexanDemocrat\n",
      "Israeli PM Netanyahu’s son, seeking cash for stripper, brags of US$20billion deal for friend’s father Waldongrado\n",
      "World Health Organization to declare gaming addiction a mental disorder. AlKarakhboy\n",
      "Dad turns in teenage son after finding child pornography on cell phone MIngmire\n",
      "Fusion GPS: Trump-Russia firm chief's transcript released The_man_who_sold\n",
      "13,000 tourists stranded at ski resort amid avalanche fears brotogeris1\n"
     ]
    }
   ],
   "source": [
    "subreddit = \"worldnews+news\"\n",
    "\n",
    "targetSub = redditApi.subreddit(subreddit)\n",
    "submissions = targetSub.new(limit=10)\n",
    "for post in submissions:\n",
    "    print(post.title, post.author)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Accessing Reddit Comments\n",
    "\n",
    "While you're never supposed to read the comments, for certain live streams or new and rising posts, the comments may provide useful insight into events on the ground or people's sentiment.\n",
    "New posts may not have comments yet though.\n",
    "\n",
    "Comments are attached to the post title, so for a given submission, you can pull its comments directly.\n",
    "\n",
    "Note Reddit returns pages of comments to prevent server overload, so you will not get all comments at once and will have to write code for getting more comments than the top ones returned at first.\n",
    "This pagination is performed using the MoreXYZ objects (e.g., MoreComments or MorePosts)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "North Korea to join Olympics in South Korea\n",
      "--- t1_dsfjo4x ---\n",
      "\t Really hoping that Kim Jong Un doesn't participate though... I'd like to see the US win at least one gold medal.\n",
      "--- t1_dsf05wr ---\n",
      "\t As I understand it, that was the goal of the recent peace talks, with a soft objective of calming the North down. As someone living in South Korea, this is fantastic news.\n",
      "\t --- t1_dsf5sms ---\n",
      "\t\t Hello from Seoul. Yup, feeling pretty good about it.\n",
      "--- t1_dsezuqt ---\n",
      "\t Stuff like this is a step in the right direction.\n",
      "--- t1_dsf0yvt ---\n",
      "\t This is the best tl;dr I could make, [original](https://www.ctvnews.ca/mobile/world/north-korea-to-join-olympics-in-south-korea-1.3751239) reduced by 87%. (I'm a bot)\n",
      "*****\n",
      "> SEOUL, Korea, Republic Of - The rival Koreas took steps toward reducing their bitter animosity during rare talks Tuesday, as North Korea agreed to send a delegation to next month&#039;s Winter Olympics in South Korea and reopen a military hotline.\n",
      "\n",
      "> North Korea is weak in winter sports and a pair of figure skaters, Ryom Tae Ok and Kim Ju Sik, earlier became the only North Korean athletes to qualify for next month&#039;s Pyeongchang Games before the North missed a confirmation deadline.\n",
      "\n",
      "> Chun, one of five South Korean negotiators, said the South proposed that North Korea send a big delegation and march with South Korean athletes during the Feb. 9-25 games&#039; opening and closing ceremonies.\n",
      "\n",
      "\n",
      "*****\n",
      "[**Extended Summary**](http://np.reddit.com/r/autotldr/comments/7p7euk/north_korea_to_join_olympics_in_south_korea/) | [FAQ](http://np.reddit.com/r/autotldr/comments/31b9fm/faq_autotldr_bot/ \"Version 1.65, ~279947 tl;drs so far.\") | [Feedback](http://np.reddit.com/message/compose?to=%23autotldr \"PM's and comments are monitored, constructive feedback is welcome.\") | *Top* *keywords*: **North**^#1 **Korea**^#2 **South**^#3 **Korean**^#4 **talks**^#5\n",
      "--- t1_dsf5sms ---\n",
      "\t Hello from Seoul. Yup, feeling pretty good about it.\n"
     ]
    }
   ],
   "source": [
    "subreddit = \"worldnews\"\n",
    "\n",
    "breadthCommentCount = 5\n",
    "\n",
    "targetSub = redditApi.subreddit(subreddit)\n",
    "\n",
    "submissions = targetSub.hot(limit=1)\n",
    "\n",
    "for post in submissions:\n",
    "    print (post.title)\n",
    "    \n",
    "    post.comment_limit = breadthCommentCount\n",
    "    \n",
    "    # Get the top few comments\n",
    "    for comment in post.comments.list():\n",
    "        if isinstance(comment, praw.models.MoreComments):\n",
    "            continue\n",
    "        \n",
    "        print (\"---\", comment.name, \"---\")\n",
    "        print (\"\\t\", comment.body)\n",
    "        \n",
    "        for reply in comment.replies.list():\n",
    "            if isinstance(reply, praw.models.MoreComments):\n",
    "                continue\n",
    "            \n",
    "            print (\"\\t\", \"---\", reply.name, \"---\")\n",
    "            print (\"\\t\\t\", reply.body)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/FacebookLogo.jpg\" width=\"20%\">\n",
    "\n",
    "## Topic 2.2: Facebook API\n",
    "\n",
    "Getting access to Facebook's API is slightly easier than Twitter's in that you can go to the Graph API explorer, grab an access token, and immediately start playing around with the API.\n",
    "The access token isn't good forever though, so if you plan on doing long-term analysis or data capture, you'll need to go the full OAuth route and generate tokens using the approved paths."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "# As before, the first thing we do is import the Facebook\n",
    "# wrapper\n",
    "\n",
    "import facebook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Connecting to the Facebook Graph\n",
    "\n",
    "Facebook has a \"Graph API\" that lets you explore its social graph. \n",
    "For privacy concerns, however, Facebook's Graph API is extremely limited in the kinds of data it can view.\n",
    "For instance, Graph API applications can now only view profiles of people who already have installed that particular application.\n",
    "These restrictions make it quite difficult to see a lot of Facebook's data.\n",
    "\n",
    "That being said, Facebook does have many popular public pages (e.g., BBC World News), and articles or messages posted by these public pages are accessible.\n",
    "In addition, many posts and comments made in reply to these public posts are also publically available for us to explore.\n",
    "\n",
    "To connect to Facebook's API though, we need an access token (unlike Reddit's API).\n",
    "Fortunately, for research and testing purposes, getting an access token is very easy.\n",
    "\n",
    "#### Acquiring a Facebook Access Token\n",
    "\n",
    "1. Log in to your Facebook account\n",
    "1. Go to Facebook's Graph Explorer (https://developers.facebook.com/tools/explorer/)\n",
    "1. Copy the *long* string out of \"Access Token\" box and paste it in the code cell bedlow\n",
    "\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/FacebookInstructions_f1.png\"/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fbAccessToken = \"EAACEdEose0cBAK2kyW5pcrgzUUMqmr4uR1ppwlz1lC5aIhJyVLm9Bfo1jOXBQwILsVzlt28dSmqwPdX9DQQDLz5zMEZC3ZB6HYTj5LyZA5hKoa3YneQpRyg3cCxwmb0Ea6uazjxaJX2QLNkL7i6BTVhy0bZCZBfvVb29AFZARFXhjcmsFO8QhY2EEhFyZBXIucZD\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we can use the Facebook Graph API with this temporary access token (it does expire after maybe 15 minutes)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to the graph API, note we use version 2.7\n",
    "graph = facebook.GraphAPI(access_token=fbAccessToken, version='2.7')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Parsing Posts from a Public Page\n",
    "\n",
    "To get a public page's posts, all you need is the name of the page. \n",
    "Then we can pull the page's feed, and for each post on the page, we can pull its comments and the name of the comment's author.\n",
    "While it's unlikely that we can get more user information than that, author name and sentiment or text analytics can give insight into bursting topics and demographics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "GraphAPIError",
     "evalue": "Error validating access token: Session has expired on Wednesday, 27-Dec-17 17:00:00 PST. The current time is Tuesday, 09-Jan-18 14:02:11 PST.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mGraphAPIError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-100-8cef7d2ef2d4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mmaxComments\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m5\u001b[0m \u001b[0;31m# How many comments for each post?\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mpost\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgraph\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_object\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mid\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtargetPage\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m'/feed'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;31m# For each post, print its message content and its ID\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.6/site-packages/facebook/__init__.py\u001b[0m in \u001b[0;36mget_object\u001b[0;34m(self, id, **args)\u001b[0m\n\u001b[1;32m    103\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mget_object\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mid\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    104\u001b[0m         \u001b[0;34m\"\"\"Fetches the given object from the graph.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 105\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mversion\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\"/\"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mid\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    106\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    107\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mget_objects\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mids\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.6/site-packages/facebook/__init__.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, path, args, post_args, files, method)\u001b[0m\n\u001b[1;32m    270\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    271\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"error\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 272\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mGraphAPIError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    273\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    274\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mGraphAPIError\u001b[0m: Error validating access token: Session has expired on Wednesday, 27-Dec-17 17:00:00 PST. The current time is Tuesday, 09-Jan-18 14:02:11 PST."
     ]
    }
   ],
   "source": [
    "# What page to look at?\n",
    "targetPage = \"nytimes\"\n",
    "\n",
    "# Other options for pages:\n",
    "# nytimes, bbc, bbcamerica, bbcafrica, redcross, disaster\n",
    "\n",
    "maxPosts = 10 # How many posts should we pull?\n",
    "maxComments = 5 # How many comments for each post?\n",
    "\n",
    "post = graph.get_object(id=targetPage + '/feed')\n",
    "\n",
    "# For each post, print its message content and its ID\n",
    "for v in post[\"data\"][:maxPosts]:\n",
    "    print (\"---\")\n",
    "    print (v[\"message\"], v[\"id\"])\n",
    "        \n",
    "    # For each comment on this post, print its number, \n",
    "    # the name of the author, and the message content\n",
    "    print (\"Comments:\")\n",
    "    comments = graph.get_object(id='%s/comments' % v[\"id\"])\n",
    "    for (i, comment) in enumerate(comments[\"data\"][:maxComments]):\n",
    "        print (\"\\t\", i, comment[\"from\"][\"name\"], comment[\"message\"])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterLogo.png\" width=\"20%\">\n",
    "\n",
    "## Topic 2.1: Twitter API\n",
    "\n",
    "Twitter's API is probably the most useful and flexible but takes several steps to configure. \n",
    "To get access to the API, you first need to have a Twitter account and have a mobile phone number (or any number that can receive text messages) attached to that account.\n",
    "Then, we'll use Twitter's developer portal to create an \"app\" that will then give us the keys tokens and keys (essentially IDs and passwords) we will need to connect to the API.\n",
    "\n",
    "So, in summary, the general steps are:\n",
    "\n",
    "0. Have a Twitter account,\n",
    "1. Configure your Twitter account with your mobile number,\n",
    "2. Create an app on Twitter's developer site, and\n",
    "3. Generate consumer and access keys and secrets.\n",
    "\n",
    "We will then plug these four strings into the code below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "# For our first piece of code, we need to import the package \n",
    "# that connects to Twitter. Tweepy is a popular and fully featured\n",
    "# implementation.\n",
    "\n",
    "import tweepy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating Twitter Credentials\n",
    "\n",
    "For more in-depth instructions for creating a Twitter account and/or setting up a Twitter account to use the following code, I will provide a walkthrough on configuring and generating this information.\n",
    "\n",
    "First, we assume you already have a Twitter account.\n",
    "If this is not true, either create one real quick or follow along.\n",
    "See the attached figures.\n",
    "\n",
    "- __Step 1. Create a Twitter account__ If you haven't already done this, do this now at Twitter.com.\n",
    "\n",
    "- __Step 2. Setting your mobile number__ Log into Twitter and go to \"Settings.\" From there, click \"Mobile\" and fill in an SMS-enabled phone number. You will be asked to confirm this number once it's set, and you'll need to do so before you can create any apps for the next step.\n",
    "\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f1.png\" scale=\"10%\"/>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f2.png\" scale=\"10%\"/>\n",
    "\n",
    "- __Step 3. Create an app in Twitter's Dev site__ Go to (apps.twitter.com), and click the \"Create New App\" button. Fill in the \"Name,\" \"Description,\" and \"Website\" fields, leaving the callback one blank (we're not going to use it). Note that the website __must__ be a fully qualified URL, so it should look like: http://test.url.com. Then scroll down and read the developer agreement, checking that agree, and finally click \"Create your Twitter application.\"\n",
    "\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f3.png\" scale=\"10%\"/>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f4.png\"/>\n",
    "\n",
    "- __Step 4. Generate keys and tokens with this app__ After your application has been created, you will see a summary page like the one below. Click \"Keys and Access Tokens\" to view and manage keys. Scroll down and click \"Create my access token.\" After a moment, your page should refresh, and it should show you four long strings of characters and numbers, a consume key, consumer secret, an access token, and an access secret (note these are __case-sensitive__!). Copy and past these four strings into the quotes in the code cell below.\n",
    "\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f5.png\" scale=\"10%\"/>\n",
    "<img src=\"http://www.cs.umd.edu/~cbuntain/inst728e/TwitterInstructions_f6.png\"/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the strings from your Twitter app webpage to populate these four \n",
    "# variables. Be sure and put the strings BETWEEN the quotation marks\n",
    "# to make it a valid Python string.\n",
    "\n",
    "consumer_key = \"1jFG5MF4PNf8zhg8Nmkk3kWVb\"\n",
    "consumer_secret = \"MOfU9zxDvsk7nKHLnYvpTUeWW5C7PsXrS9TuwnvYcx3ANzc5LG\"\n",
    "access_token = \"2343077714-N9yB6UKYegygTgTPl7xgm7PfUbLhO6TzqitlFP0\"\n",
    "access_secret = \"d44DHDHV3CYmeuDnWbITumnPcnrVJwS0mJhgITQYWyXdx\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Connecting to Twitter\n",
    "\n",
    "Once we have the authentication details set, we can connect to Twitter using the Tweepy OAuth handler, as below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connected to Twitter!\n"
     ]
    }
   ],
   "source": [
    "# Now we use the configured authentication information to connect\n",
    "# to Twitter's API\n",
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_secret)\n",
    "\n",
    "api = tweepy.API(auth)\n",
    "\n",
    "print(\"Connected to Twitter!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Testing our Connection\n",
    "\n",
    "Now that we are connected to Twitter, let's do a brief check that we can read tweets by pulling the first few tweets from our own timeline (or the account associated with your Twitter app) and printing them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pewresearch Pew Research Center said: Most Americans evaluate #STEM education in the U.S. as middling compared with other developed nations… https://t.co/9fTwHepPnF\n",
      "business Bloomberg said: Get caught up on all things tech! #BTECH is streaming LIVE right here on @Twitter https://t.co/Z2eKcAuXAJ\n",
      "WorldBank World Bank said: Transport is taking a serious toll on the wellbeing of people and the planet. Can technology help save the day? Joi… https://t.co/gcrDFlaYd4\n",
      "McKinsey McKinsey & Company said: Conventional wisdom has taught leaders that the first 100 days are imperative in a new role, but the data simply do… https://t.co/9BOw2TmFrh\n",
      "TechCrunch TechCrunch said: How AI and copyright would work https://t.co/fJmtkdI5R6\n"
     ]
    }
   ],
   "source": [
    "# Get tweets from our timeline\n",
    "public_tweets = api.home_timeline()\n",
    "\n",
    "# print the first five authors and tweet texts\n",
    "for tweet in public_tweets[:5]:\n",
    "    print (tweet.author.screen_name, tweet.author.name, \"said:\", tweet.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Searching Twitter for Keywords\n",
    "\n",
    "Now that we're connected, we can search Twitter for specific keywords with relative ease just like you were using Twitter's search box.\n",
    "While this search only goes back 7 days and/or 1,500 tweets (whichever is less), it can be powerful if an event you want to track just started.\n",
    "\n",
    "Note that you might have to deal with paging if you get lots of data. Twitter will only return you one page of up to 100 tweets at a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searched for: earthquake\n",
      "Number found: 14\n",
      "\n",
      "Tweets:\n",
      "SoCalEq SoCal Earthquakes USGS reports a M1.34 #earthquake 7km SSE of Redlands, California on 1/9/18 @ 21:59:11 UTC https://t.co/tmMamupjNe #quake\n",
      "everyEarthquake Every Earthquake USGS reports a M1.34 #earthquake 7km SSE of Redlands, California on 1/9/18 @ 21:59:11 UTC https://t.co/l1Ei3H2Egi #quake\n",
      "AvaBH64 Ava’s Gone Feral RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "tannerlikeskara Tanner Griffith A final breath. An earthquake. Dead raise. A curtain tears in two. A soldier falls to his knees. A mother weeps. Si… https://t.co/XPn2Zo7jbX\n",
      "GePeirson Gail Peirson RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "CornubiaGeol Gordon Neighbour RT @icelandgeology: Currently there is storm in part of Iceland. Tomorrow there is going to be more storm in Iceland. This limits earthquak…\n",
      "Quake_Tracker4 Earthquakes Tsunamis Mag: 4 - Depth: 84 km - UTC 21:50 - Guadeloupe Region, Leeward Isl. - EMSC Info: https://t.co/IHOtVbRkTC\n",
      "clango4 Ms. Lango Whose structure can survive a 20 sec. earthquake? @BarleySheafFRSD https://t.co/GuR968xU4t\n",
      "moto_sthkd StHkdのメモらしき何か RT @eq_map: 【M4.7】IZU ISLANDS, JAPAN REGION 40.1km 2018/01/10 02:50:33 JST[UTC+9]\n",
      "(G)https://t.co/IQinS0SJEY (USGS)https://t.co/iQ91gp9cer\n",
      "CornubiaGeol Gordon Neighbour RT @icelandgeology: Sharp increase in earthquake activity in Katla volcano and small glacier flood. https://t.co/xQLHbfVSFB\n",
      "thrillthewill Will Luciani RT @HashtagGriswold: Ending a temporary refugee status dating back to a 2001 earthquake is just like war crimes and genocide, says Heat Mis…\n",
      "KimReed3 Kim Reed RT @Carole4IL06: Disgusted that @theRealDonladTrump is ending Temporary Protected Status of nearly 200,000 Salvadorans that have been livin…\n",
      "from___japan from_japan 【#USGS #Breaking】#earthquake　M 0.6 - 5km ENE of Aguanga, CA https://t.co/qYGzeJRN6V #alert #tsunami #prayfromjapan\n",
      "Quake_Tracker Earthquake Report Mag: 4 - Depth: 84 km - UTC 9:50 PM - Guadeloupe Region, Leeward Isl. - EMSC Info: https://t.co/0g0cDgYdZl\n"
     ]
    }
   ],
   "source": [
    "# Our search string\n",
    "queryString = \"earthquake\"\n",
    "\n",
    "# Perform the search\n",
    "matchingTweets = api.search(queryString)\n",
    "\n",
    "print (\"Searched for:\", queryString)\n",
    "print (\"Number found:\", len(matchingTweets))\n",
    "\n",
    "# For each tweet that matches our query, print the author and text\n",
    "print (\"\\nTweets:\")\n",
    "for tweet in matchingTweets:\n",
    "    print (tweet.author.screen_name, tweet.author.name, tweet.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### More Complex Queries\n",
    "\n",
    "Twitter's Search API exposes many capabilities, like filtering for media, links, mentions, geolocations, dates, etc.\n",
    "We can access these capabilities directly with the search function.\n",
    "\n",
    "For a list of operators Twitter supports, go here: https://dev.twitter.com/rest/public/search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searched for: earthquake (filter:media OR filter:links)\n",
      "Number found: 12\n",
      "\n",
      "Tweets:\n",
      "LiveFrom_Mars RT @VSUShare: SHARE isn’t allowed to directly sponsor a girl in Tanzania this semester due to their earthquake rebuilding fund. However, we…\n",
      "SoCalEq USGS reports a M1.34 #earthquake 7km SSE of Redlands, California on 1/9/18 @ 21:59:11 UTC https://t.co/tmMamupjNe #quake\n",
      "everyEarthquake USGS reports a M1.34 #earthquake 7km SSE of Redlands, California on 1/9/18 @ 21:59:11 UTC https://t.co/l1Ei3H2Egi #quake\n",
      "AvaBH64 RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "GePeirson RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "Quake_Tracker4 Mag: 4 - Depth: 84 km - UTC 21:50 - Guadeloupe Region, Leeward Isl. - EMSC Info: https://t.co/IHOtVbRkTC\n",
      "clango4 Whose structure can survive a 20 sec. earthquake? @BarleySheafFRSD https://t.co/GuR968xU4t\n",
      "moto_sthkd RT @eq_map: 【M4.7】IZU ISLANDS, JAPAN REGION 40.1km 2018/01/10 02:50:33 JST[UTC+9]\n",
      "(G)https://t.co/IQinS0SJEY (USGS)https://t.co/iQ91gp9cer\n",
      "CornubiaGeol RT @icelandgeology: Sharp increase in earthquake activity in Katla volcano and small glacier flood. https://t.co/xQLHbfVSFB\n",
      "thrillthewill RT @HashtagGriswold: Ending a temporary refugee status dating back to a 2001 earthquake is just like war crimes and genocide, says Heat Mis…\n",
      "from___japan 【#USGS #Breaking】#earthquake　M 0.6 - 5km ENE of Aguanga, CA https://t.co/qYGzeJRN6V #alert #tsunami #prayfromjapan\n",
      "Quake_Tracker Mag: 4 - Depth: 84 km - UTC 9:50 PM - Guadeloupe Region, Leeward Isl. - EMSC Info: https://t.co/0g0cDgYdZl\n"
     ]
    }
   ],
   "source": [
    "# Lets find only media or links about earthquakes\n",
    "queryString = \"earthquake (filter:media OR filter:links)\"\n",
    "\n",
    "# Perform the search\n",
    "matchingTweets = api.search(queryString)\n",
    "\n",
    "print (\"Searched for:\", queryString)\n",
    "print (\"Number found:\", len(matchingTweets))\n",
    "\n",
    "# For each tweet that matches our query, print the author and text\n",
    "print (\"\\nTweets:\")\n",
    "for tweet in matchingTweets:\n",
    "    print (tweet.author.screen_name, tweet.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dealing with Pages\n",
    "\n",
    "As mentioned, Twitter serves results in pages. \n",
    "To get all results, we can use Tweepy's Cursor implementation, which handles this iteration through pages for us in the background."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Tweets:\n",
      "myearthquakeapp 3.02 earthquake occurred near Ashhurst, Manawatu-Wanganui, New Zealand at 01:08 UTC! #earthquake #Ashhurst https://t.co/oeVIhrLQNH\n",
      "SP16_EARTHQUAKE https://t.co/CPrIKlKfeI\n",
      "everyEarthquake USGS reports a M0.34 #earthquake 11km W of Toms Place, CA on 1/10/18 @ 0:30:28 UTC https://t.co/7GyIhSFNtq #quake\n",
      "myearthquakeapp 2.48 earthquake occurred near Mohaka, Hawke's Bay, New Zealand at 01:07 UTC! #earthquake #Mohaka https://t.co/jRs1aYrG7i\n",
      "earthquake_all7 【微小地震速報 三重県20/74】\n",
      "2018/01/10 7:21:35 JST, \n",
      "日本 三重県 志摩市役所の東南東57km, \n",
      "M2.5, TNT84.8kg, 深さ0.0km, \n",
      "MAP https://t.co/ZHQTagrb35\n",
      "earthquake_all 【微小地震速報 和歌山県3/131】\n",
      "2018/01/10 9:34:51 JST, \n",
      "日本 和歌山県 和歌山市役所の南西6km, \n",
      "M1.4, TNT1.9kg, 深さ7.1km, \n",
      "MAP https://t.co/ZZ3cR8ycVF 1464\n",
      "myearthquakeapp 2.6 earthquake occurred near Otaki Beach, New Zealand at 01:06 UTC! #earthquake #OtakiBeach https://t.co/8lR0utskud\n",
      "EARTH3R For the 200,000 Salvadoran earthquake refugees in the U.S., being sent back could be a death sentence… https://t.co/GmJmoRLtk5\n",
      "awadallah RT @Pogue: You know my big story on Fitbit’s 6 billion nights’ worth of collected sleep data? (https://t.co/jbn2kchJog ) They just sent ove…\n",
      "IAmTheShockWave RT @OregonStateCCE: Seminar | Presenters from OSU, @ch2m, @Degenkolb, @reid_middleton + more share Lessons Learned from the 2017 Mexico Cit…\n",
      "flairforstyle RT @noveliciouss: Be happy in the moment, that's enough. Each moment is all we need, not more.\n",
      "Mother Teresa\n",
      "#writing\n",
      "#Art 'An Instant Befo…\n",
      "EQAlerts #Earthquake M3.6 New Zealand 3mins ago 10 Jan 01:05 UTC - report/info: \n",
      "https://t.co/Oa2mLGRaB2\n",
      "sakuya3619 RT @tenkijp_jishin: 10日8時38分頃、茨城県で最大震度1を観測する地震がありました。震源地は茨城県南部、M3.2。この地震による津波の心配はありません。 https://t.co/N6nfMJENfg #jishin #地震\n",
      "myearthquakeapp 3.74 earthquake occurred near New Zealand at 01:04 UTC! #earthquake #NewZealand https://t.co/rTdSsttcSb\n",
      "PujanNews RT @EarthNews6: Vibrations indicate a large #earthquake is due. Could have two on both sides of planet. https://t.co/NdDaTYwFgo\n",
      "myearthquakeapp 0.81 earthquake occurred 8km NW of The Geysers, CA at 01:02 UTC! #earthquake #TheGeysers https://t.co/LbjNjxV0uD\n",
      "WeREqual2 @Eionthenet @TheRealJuIian @realDonaldTrump @ChelseaClinton Yeah, you compare how we responded to Haiti when they h… https://t.co/UxZ6A40z7A\n",
      "Earthquake_rt MD 3.2 PUERTO RICO REGION https://t.co/prbEqpPsMN https://t.co/0VIuzhNScD\n",
      "Vortice_EFC ML 2.8 SICILY, ITALY https://t.co/3ha5CMxd16\n",
      "weerenonweer MD 3.2 PUERTO RICO REGION: Magnitude   MD 3.2 Region   PUERTO RICO REGION Date time   2018-01-09 19:02:17.2 UTC Loc… https://t.co/ei3F1tuu0g\n",
      "Vortice_EFC ML 3.4 TARAPACA, CHILE https://t.co/iCdzWGNlMn\n",
      "NacreBit RT @QuakeFactor: QuakeFactor:ML 2.4 GREATER LOS ANGELES AREA, CALIF. https://t.co/vVx3z8WaIZ https://t.co/joluiKNaDt\n",
      "phoenx7 RT @TheRealNews: Salvadorans under TPS, who have been living in the US following an earthquake that killed over 1000 people, now have 18 mo…\n",
      "JessChilin RT @TheRealNews: Salvadorans under TPS, who have been living in the US following an earthquake that killed over 1000 people, now have 18 mo…\n",
      "earthquake_all7 【小地震速報 三重県19/73】\n",
      "2018/01/10 7:05:23 JST, \n",
      "日本 三重県 志摩市役所の南南東100km, \n",
      "M3.6, TNT3.8トン, 深さ180.4km, \n",
      "MAP https://t.co/T7vyYp8GVs\n",
      "jliu_42 RT @OregonStateCCE: Seminar | Presenters from OSU, @ch2m, @Degenkolb, @reid_middleton + more share Lessons Learned from the 2017 Mexico Cit…\n",
      "earthquake_all 【微小地震速報 岩手県13/130】\n",
      "2018/01/10 9:29:10 JST, \n",
      "日本 岩手県 田野畑村役場の東南東24km, \n",
      "M2.4, TNT60.0kg, 深さ27.9km, \n",
      "MAP https://t.co/PQmnsBe2Jp 1462\n",
      "ms_stateside RT @angelica_lyn_22: The moment i saw Hope's new dp i really don't know what i feel. It's just like there's an earthquake inside my heart…\n",
      "earthquake_all2 【微小地震速報】\n",
      "2018/01/10 9:55:08 JST, \n",
      "イラン・イスラム共和国 アフバーズの北東108km, \n",
      "M1.8, TNT7.6kg, 深さ10.0km, \n",
      "https://t.co/hC1lAmiCW6\n",
      "brewer_pam RT @HashtagGriswold: Ending a temporary refugee status dating back to a 2001 earthquake is just like war crimes and genocide, says Heat Mis…\n",
      "sakuya3619 RT @tenkijp_jishin: 10日8時57分頃、鳥取県で最大震度1を観測する地震がありました。震源地は鳥取県中部、M2.5。この地震による津波の心配はありません。 https://t.co/RorLGsNRQT #jishin #地震\n",
      "myearthquakeapp 1.7 earthquake occurred near Ravansar, Kermanshah at 00:59 UTC! #earthquake #Ravansar https://t.co/jDpU5tgsNU\n",
      "AbregoLeisy RT @TheRealNews: Salvadorans under TPS, who have been living in the US following an earthquake that killed over 1000 people, now have 18 mo…\n",
      "Moreno90Souza RT @pushthefeeling: #woodmorning you guys! How did you sleep? #earthquake https://t.co/pzQ2Qcczvj\n",
      "etalbert RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "GirlWithCrocs RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "earthquake_all2 【微小地震速報】\n",
      "2018/01/10 9:38:03 JST, \n",
      "イラン・イスラム共和国 ケルマーンシャーの北西38km, \n",
      "M2.8, TNT239.0kg, 深さ10.0km, \n",
      "https://t.co/mlE5S30w6a\n",
      "DanRFowler2 RT @noveliciouss: Be happy in the moment, that's enough. Each moment is all we need, not more.\n",
      "Mother Teresa\n",
      "#writing\n",
      "#Art 'An Instant Befo…\n",
      "child_dreamer RT @earthquake_jp: ［気象庁情報］10日　07時30分頃　千葉県東方沖（N35.4/E141.4）にて　最大震度2（M5.2）の地震が発生。　震源の深さは30km。( https://t.co/MoJi0uvZPX ) #saigai #jishin #ear…\n",
      "moonsaha6 PLANET X NEWS – EARTHQUAKE UPDATE JANUARY 3rd, 2018 https://t.co/d7oxHQEblp https://t.co/H2E61Rq4dB\n",
      "jamintolife RT @Bazoom_: The Great Manila Earthquake is Coming, and Prayer Won’t Stop It https://t.co/gPPrZ4ywDE\n",
      "child_dreamer RT @earthquake_jp: ［速報LV1］10日　07時30分頃　房総半島東方沖（N35.3/E141.4）(推定)にて　M4.3（推定）の地震が発生。　震源の深さは推定12.8km。( https://t.co/PxC5zyGpP7 ) #saigai #jishi…\n",
      "moonsaha6 New post (PLANET X NEWS - EARTHQUAKE UPDATE JANUARY 3rd, 2018) has been published on Funny Videos -… https://t.co/0IhKXMNPrF\n",
      "smallLifesub RT @eq_map: 【M4.7】IZU ISLANDS, JAPAN REGION 40.1km 2018/01/10 02:50:33 JST[UTC+9]\n",
      "(G)https://t.co/IQinS0SJEY (USGS)https://t.co/iQ91gp9cer\n",
      "taborix 【地震速報・ livedoor】 10日08:38 [ 最大震度 ] 震度 1 [ 震源地 ] 茨城県南部 https://t.co/dBgbJjhFeD （tabot）#tbreqc\n",
      "everyEarthquake USGS reports a M0.81 #earthquake 8km NW of The Geysers, CA on 1/10/18 @ 1:02:00 UTC https://t.co/7pZTHiHQfp #quake\n",
      "earthquake_all2 【微小地震速報】\n",
      "2018/01/10 9:36:12 JST, \n",
      "アメリカ合衆国 アラスカ フェアバンクスの東北東198km, \n",
      "ML1.8, TNT7.6kg, 深さ6.1km, \n",
      "https://t.co/iRjcwrshXe\n",
      "mexusmx @JCasaTodd We are at about 8000 ft so it is not as warm as you might think, but I am not complaining (unless there… https://t.co/YEzJ5UZIKO\n",
      "jane_lavoie RT @TheRealNews: Salvadorans under TPS, who have been living in the US following an earthquake that killed over 1000 people, now have 18 mo…\n",
      "child_dreamer RT @earthquake_jp: ［気象庁情報］10日　07時21分頃　千葉県東方沖（N35.4/E141.5）にて　最大震度1（M4.8）の地震が発生。　震源の深さは20km。( https://t.co/1scnq9L5m5 ) #saigai #jishin #ear…\n",
      "myearthquakeapp 1.8 earthquake occurred near Izeh, Khuzestan at 00:55 UTC! #earthquake #Izeh https://t.co/Jc54syfoLm\n",
      "child_dreamer RT @earthquake_jp: ［速報LV5］10日　07時20分頃　千葉県東方沖（N35.4/E141.2）(推定)にて　M4.7（推定）の地震が発生。　震源の深さは推定36km。( https://t.co/HKTy4cTyCC ) #saigai #jishin #…\n",
      "earthquake_pred https://t.co/QSdutgOOmH\n",
      "child_dreamer RT @earthquake_jp: ［速報LV4］10日　07時20分頃　千葉県東方沖（N35.4/E141.3）(推定)にて　M4.7（推定）の地震が発生。　震源の深さは推定35km。( https://t.co/dAI7E1syfb ) #saigai #jishin #…\n",
      "yourpacrat RT @HashtagGriswold: Ending a temporary refugee status dating back to a 2001 earthquake is just like war crimes and genocide, says Heat Mis…\n",
      "DisasterChannL RT @JulissaTrevino: @Racked @Dickies And this one that I wrote when I was living in Mexico and a devastating earthquake hit. Wrote for @BBC…\n",
      "azmk5 RT @noveliciouss: Be happy in the moment, that's enough. Each moment is all we need, not more.\n",
      "Mother Teresa\n",
      "#writing\n",
      "#Art 'An Instant Befo…\n",
      "earthquakeinfos M 1.6 - 11km SW of Ridgemark, CA https://t.co/irlGT2CVaG\n",
      "earthquakeinfos M 1.3 - 7km N of Beaumont, CA https://t.co/mtoQmAeYY6\n",
      "earthquakeinfos M 0.9 - 1km NNE of Idyllwild, CA https://t.co/RfnKNtF37q\n",
      "earthquakeinfos M 1.7 - 32km NW of Bridgeport, California https://t.co/AbxiRACmLD\n",
      "243ix3wmDACoVFP RT @earthquake_jp: ［速報LV1］10日　07時30分頃　房総半島東方沖（N35.3/E141.4）(推定)にて　M4.3（推定）の地震が発生。　震源の深さは推定12.8km。( https://t.co/PxC5zyGpP7 ) #saigai #jishi…\n",
      "LivingOnChi @japantimes @leurenmoret #GeoEngineering\n",
      ".@realGeoEngWatch 9/29/14\n",
      " ➖\n",
      "Was #HAARP A Factor In The #Fukushima Earthqu… https://t.co/yBEvgr22s9\n",
      "child_dreamer RT @earthquake_jp: ［速報LV1］10日　07時20分頃　房総半島東方沖（N35.3/E141.4）(推定)にて　M4.5（推定）の地震が発生。　震源の深さは推定10km未満。( https://t.co/1wT4zSpSWk ) #saigai #jishi…\n",
      "PCEstatesTeam What should you do during those moments when a big #earthquake strikes? And what should you do when it's over? Here… https://t.co/4XUy1OpDyB\n",
      "myearthquakeapp 0.76 earthquake occurred 4km SW of Volcano, Hawaii at 16:57 UTC! #earthquake #Volcano https://t.co/vYf9AssVMD\n",
      "CRUSH_ST Help support the victims of the Japanese Earthquake and Pacific Tsunami https://t.co/ruN0X4C via @yoshikifa\n",
      "from___japan 【#USGS #Breaking】#earthquake　M 1.3 - 7km N of Beaumont, CA https://t.co/yeosQCzqLS #alert #tsunami #prayfromjapan\n",
      "S_Coyner Can animals tell if an earthquake is coming? https://t.co/rZiVk5U4cD\n",
      "shi_ge_chi_n RT @earthquakejapan: （東京地震のリスク） - （6.4の地震は可能です）（次の40時間の間に） - https://t.co/MSA4iPozgl …\n",
      "shi_ge_chi_n RT @earthquakejapan: （5.2地震）（警戒区域）（東京、日本） - https://t.co/ePhk7jNNMW\n",
      "TheRealNews Salvadorans under TPS, who have been living in the US following an earthquake that killed over 1000 people, now hav… https://t.co/EtUw6urbuU\n",
      "countryboyexec RT @prageru: \"The Clintons have been a top target of protesters in Port au Prince, who claim earthquake aid money was mismanaged and lucrat…\n",
      "ChileAlertaApp #Sismografo de la region de #Antofagasta registrando #sismo en tiempo real. #temblor #earthquake #Chile… https://t.co/OnKfl35y1J\n",
      "Binod1966 Yes. It was an earthquake moment. थर थर कांप रहा थे सभी। https://t.co/o9ym5xUXJx\n",
      "LuciaBW15 RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "edis251 RT @immigrant_legal: #WinterStormGrayson #MorningJoe #earthquake Obama-era  \n",
      "Delivered less than 3% GDP \n",
      "Deceived about Obamacare\n",
      "Destroyed…\n",
      "JaneFultonAlt RT @SenFeinstein: Thursday’s East Bay earthquake underscored the urgent need for full implementation of an early-warning system. We must be…\n",
      "CUGeology RT @NESTA_US: #SmartPhones helping in our understanding of #earthquakes?\n",
      "\n",
      "#Algorithm analyses different vibrations on phone's accelerometer…\n",
      "myearthquakeapp 0.69 earthquake occurred 30km NW of West Yellowstone, Montana at 22:09 UTC! #earthquake #WestYellowstone https://t.co/D8gk7J4Vkw\n",
      "campokescans Snorlax ♂ Lick/Earthquake (IV: 73% - CP: 1477 - L: 16 until 08:22:55pm. https://t.co/UBjbBgLvHw\n",
      "Goosey8711 RT @prageru: \"The Clintons have been a top target of protesters in Port au Prince, who claim earthquake aid money was mismanaged and lucrat…\n",
      "Julianka8265 RT @earthquakeBot: A 5.7 magnitude earthquake occurred 167.15mi NNW of Puerto Ayora, Ecuador. Details: https://t.co/Jwfwe3S9NW Map: https:/…\n",
      "ChileAlertaApp Aviso \n",
      "#Sismo detectado en la region de #Antofagasta.\n",
      "#temblor #earthquake #Chile https://t.co/RblVNxZYn8 \n",
      "id:r5xiId\n",
      "Julianka8265 RT @earthquakeBot: A 5.4 magnitude earthquake occurred 37.28mi SE of Hasaki, Japan. Details: https://t.co/ek0jya2jXO Map: https://t.co/pKNH…\n",
      "Julianka8265 RT @earthquakeBot: A 5.0 magnitude earthquake occurred 65.24mi ESE of Vanj, Tajikistan. Details: https://t.co/x2llAYmOvB Map: https://t.co/…\n",
      "zbpokescans Snorlax ♂ Lick/Earthquake (IV: 33% - CP: 409 - L: 5 until 08:25:56pm. https://t.co/YoyrxBnVyf\n",
      "AyCProductores RT @ChileAlertaApp: New #Earthquake. 🌎\n",
      "5.4 - 60km SE of #Hasaki - #Japan.\n",
      "2018/01/09 22:30:18.\n",
      "#Temblor #Sismo #USGS #alert https://t.co/dt…\n",
      "RenoCERT RT @QuakesToday: 1.9 magnitude #earthquake. 6 km from #Harper, KS, United States https://t.co/B8OOVy7aCl\n",
      "EarthquakeView Earthquake : M 4.9 - 54km SE of Hasaki, Japan: DYFI? - IITime2018-01-09 22:20:50 UTC2018-01-10 07:20:50 +09:00 at e… https://t.co/ZuESQbn5H0\n",
      "EarthquakeView Earthquake : M 4.3 - 24km SSW of Shushtar, Iran: Time2018-01-09 23:12:54 UTC2018-01-10 02:42:54 +03:30 at epicenter… https://t.co/WmuM4FOu3f\n",
      "likeybytwice nayeons claw hands — imagine those smacking ya ass omg earthquake https://t.co/NLOvYFHO1U\n",
      "dog_of_dogs RT @SenKamalaHarris: These are people who rebuilt their lives in the U.S. after fleeing an earthquake over a decade ago. They have kids, jo…\n",
      "fantacybellita RT @angelica_lyn_22: The moment i saw Hope's new dp i really don't know what i feel. It's just like there's an earthquake inside my heart…\n",
      "macmeg523 RT @SchusterInst: New seismology research shows #earthquakes in north Texas are \"occurring  on faults that were inactive for at least 300m…\n",
      "MarieMyungOkLee RT @SchusterInst: New seismology research shows #earthquakes in north Texas are \"occurring  on faults that were inactive for at least 300m…\n",
      "jkomrade RT @HashtagGriswold: Ending a temporary refugee status dating back to a 2001 earthquake is just like war crimes and genocide, says Heat Mis…\n",
      "jane_lavoie RT @CECHR_UoD: Canadian officials confirm largest earthquake caused by fracking\n",
      "https://t.co/I8pfNWdSjA #environment https://t.co/Cyf6w3Vw4M\n",
      "earthquake_all 【微小地震速報 岩手県12/129】\n",
      "2018/01/10 9:29:03 JST, \n",
      "日本 岩手県 平泉町役場の西20km, \n",
      "M1.3, TNT1.3kg, 深さ6.4km, \n",
      "MAP https://t.co/wtwsonqHbK 1464\n",
      "Angrymike281 The biggest fire in Kalifornia history, a semi minor earthquake and now flooding, it seems as if the entire \"state\"… https://t.co/X2h5TQpsFv\n"
     ]
    }
   ],
   "source": [
    "# Lets find only media or links about earthquakes\n",
    "queryString = \"earthquake (filter:media OR filter:links)\"\n",
    "\n",
    "# How many tweets should we fetch? Upper limit is 1,500\n",
    "maxToReturn = 100\n",
    "\n",
    "# Perform the search, and for each tweet that matches our query, \n",
    "# print the author and text\n",
    "print (\"\\nTweets:\")\n",
    "for status in tweepy.Cursor(api.search, q=queryString).items(maxToReturn):\n",
    "    print (status.author.screen_name, status.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Other Search Functionality\n",
    "\n",
    "The Tweepy wrapper and Twitter API is pretty extensive.\n",
    "You can do things like pull the last 3,200 tweets from other users' timelines, find all retweets of your account, get follower lists, search for users matching a query, etc.\n",
    "\n",
    "More information on Tweepy's capabilities are available at its documentation page: (http://tweepy.readthedocs.io/)\n",
    "\n",
    "Other information on the Twitter API is available here: (https://developer.twitter.com/en/docs/tweets/search/overview)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Twitter Streaming\n",
    "\n",
    "Up to this point, all of our work has been retrospective. \n",
    "An event has occurred, and we want to see how Twitter responded over some period of time. \n",
    "\n",
    "To follow an event in real time, Twitter and Tweepy support Twitter streaming.\n",
    "Streaming is a bit complicated, but it essentially lets of track a set of keywords, places, or users.\n",
    "\n",
    "To keep things simple, I will provide a simple class and show methods for printing the first few tweets.\n",
    "Larger solutions exist specifically for handling Twitter streaming.\n",
    "\n",
    "You could take this code though and easily extend it by writing data to a file rather than the console.\n",
    "I've marked where that code could be inserted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "# First, we need to create our own listener for the stream\n",
    "# that will stop after a few tweets\n",
    "class LocalStreamListener(tweepy.StreamListener):\n",
    "    \"\"\"A simple stream listener that breaks out after X tweets\"\"\"\n",
    "    \n",
    "    # Max number of tweets\n",
    "    maxTweetCount = 10\n",
    "    \n",
    "    # Set current counter\n",
    "    def __init__(self):\n",
    "        tweepy.StreamListener.__init__(self)\n",
    "        self.currentTweetCount = 0\n",
    "        \n",
    "        # For writing out to a file\n",
    "        self.filePtr = None\n",
    "        \n",
    "    # Create a log file\n",
    "    def set_log_file(self, newFile):\n",
    "        if ( self.filePtr ):\n",
    "            self.filePtr.close()\n",
    "            \n",
    "        self.filePtr = newFile\n",
    "        \n",
    "    # Close log file\n",
    "    def close_log_file(self):\n",
    "        if ( self.filePtr ):\n",
    "            self.filePtr.close()\n",
    "    \n",
    "    # Pass data up to parent then check if we should stop\n",
    "    def on_data(self, data):\n",
    "\n",
    "        print (self.currentTweetCount)\n",
    "        \n",
    "        tweepy.StreamListener.on_data(self, data)\n",
    "            \n",
    "        if ( self.currentTweetCount >= self.maxTweetCount ):\n",
    "            return False\n",
    "\n",
    "    # Increment the number of statuses we've seen\n",
    "    def on_status(self, status):\n",
    "        self.currentTweetCount += 1\n",
    "        \n",
    "        # Could write this status to a file instead of to the console\n",
    "        print (status.text)\n",
    "        \n",
    "        # If we have specified a file, write to it\n",
    "        if ( self.filePtr ):\n",
    "            self.filePtr.write(\"%s\\n\" % status._json)\n",
    "        \n",
    "    # Error handling below here\n",
    "    def on_exception(self, exc):\n",
    "        print (exc)\n",
    "\n",
    "    def on_limit(self, track):\n",
    "        \"\"\"Called when a limitation notice arrives\"\"\"\n",
    "        print (\"Limit\", track)\n",
    "        return\n",
    "\n",
    "    def on_error(self, status_code):\n",
    "        \"\"\"Called when a non-200 status code is returned\"\"\"\n",
    "        print (\"Error:\", status_code)\n",
    "        return False\n",
    "\n",
    "    def on_timeout(self):\n",
    "        \"\"\"Called when stream connection times out\"\"\"\n",
    "        print (\"Timeout\")\n",
    "        return\n",
    "\n",
    "    def on_disconnect(self, notice):\n",
    "        \"\"\"Called when twitter sends a disconnect notice\n",
    "        \"\"\"\n",
    "        print (\"Disconnect:\", notice)\n",
    "        return\n",
    "\n",
    "    def on_warning(self, notice):\n",
    "        print (\"Warning:\", notice)\n",
    "        \"\"\"Called when a disconnection warning message arrives\"\"\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we set up the stream using the listener above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "listener = LocalStreamListener()\n",
    "localStream = tweepy.Stream(api.auth, listener)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "RT @WendySiegelman: @maddow This oil tanker disaster is happening now in the East China Sea - the ship may explode and release 1 million ba…\n",
      "1\n",
      "\"People in war-torn Yemen are facing a situation that \"'looks like the Apocalypse'\", says UN's humanitarian chief.… https://t.co/jhjg6kQPAp\n",
      "2\n",
      "RT @ARTVReviews: I got a @MoviePass subscription ($10 a month to be able to see 1 movie a day in theaters) and I saw some flicks this past…\n",
      "3\n",
      "RT @jennygardiner: Share your dating disaster story at @JUSTConRom for a chance to win an ebook copy of FALLING FOR MR. MAYBE. https://t.co…\n",
      "4\n",
      "Now all I have to left to finish of the original NES Mega Man is the horrifically difficult beautiful disaster of e… https://t.co/AI6Yk6agSL\n",
      "5\n",
      "RT @sosadtoday: one time i tried to be positive and it was a disaster\n",
      "6\n",
      "@amjoyshow @ChetPowell @teresatomlinson : it would be a goat rope disaster. NEVER.\n",
      "7\n",
      "RT @178kakapo: \"Our children are suffering.\"\n",
      "Yemen is on the brink of the worst humanitarian disaster in 50 years. \n",
      "fr. AJEnglish\n",
      "https://t…\n",
      "8\n",
      "RT @s_oldham: I asked Tommy Wiseau what he would have said last night had James Franco not blocked him. His response: “If a lot of people l…\n",
      "9\n",
      "Magnitude 3.1 earthquake rattles part of Oklahoma https://t.co/UI12Tu0fWs\n"
     ]
    }
   ],
   "source": [
    "# Stream based on keywords\n",
    "localStream.filter(track=['earthquake', 'disaster'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "@nytimes What a POS. You couldn’t pay me enough money to watch these man hating pigs.\n",
      "1\n",
      "RT @nytimes: Trump's lawyers are assessing the risks of allowing him to be interviewed by the special counsel, who told them a request was…\n",
      "2\n",
      "RT @nytimes: Best: Oprah Winfrey's speech, Natalie Portman's one-liner \n",
      "Worst: Mostly silent men, some of those red-carpet interviews https…\n",
      "3\n",
      "@nytimes What a joke! Aren’t you the journalists that suppressed the Weinstein story!\n",
      "4\n",
      "@nytimes …. unless we disagree with the truth. Then we just make it up\n",
      "5\n",
      "RT @nytimes: Times investigations expose the truth that holds power to account. #TruthHasAVoice\n",
      "6\n",
      "RT @nytimes: Times journalists pursue the truth wherever it leads.\n",
      "7\n",
      "@nytimes Donald that dossier was on me Hillary and the Democrats paid to have your name put on it with the help of… https://t.co/sFCV0pSgWO\n",
      "8\n",
      "@nytimes Your truth could be a crappy opinion that spreads as truth tho.\n",
      "9\n",
      "RT @nytimes: The truth has power. #TruthHasAVoice\n",
      "\n",
      " https://t.co/GjlBsfUAa7\n"
     ]
    }
   ],
   "source": [
    "listener = LocalStreamListener()\n",
    "localStream = tweepy.Stream(api.auth, listener)\n",
    "\n",
    "# List of screen names to track\n",
    "screenNames = ['bbcbreaking', 'CNews', 'bbc', 'nytimes']\n",
    "\n",
    "# Twitter stream uses user IDs instead of names\n",
    "# so we must convert\n",
    "userIds = []\n",
    "for sn in screenNames:\n",
    "    user = api.get_user(sn)\n",
    "    userIds.append(user.id_str)\n",
    "\n",
    "# Stream based on users\n",
    "localStream.filter(follow=userIds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "SYRE IS SO GOOD THANK YOU. @officialjaden\n",
      "1\n",
      "@BreitbartNews My 2 favorite NJ. Generals. Walker &amp; Trump! Fluties pretty good 2.\n",
      "2\n",
      "A Chorus of Color: Amazing Birds on Public Lands https://t.co/dUw4OV6zqO\n",
      "3\n",
      "@brooke_castro It was great. I had sweets today.  There was 6 cupcakes on the table. I had 4 of them as a snack and… https://t.co/wOYmdkntQa\n",
      "4\n",
      "Agree wholeheartedly with Kerr on this. Media's moves are a reflection of society, not the other way around. https://t.co/QfysXwoujI\n",
      "5\n",
      "@Twitch_Pink You have to try puerto nuevo style lobster in Chipotle sauce! Soo tasty!\n",
      "6\n",
      "@TyIslit Oya let me send you my head too. Mschewww\n",
      "7\n",
      "Wowww ): https://t.co/s5xWdsi3AG\n",
      "8\n",
      "TEST_PLACE: 6d8ae305-ebf6-447f-a930-4a89d69cb34e\n",
      "9\n",
      "Me too 🙋🏻‍♂️🙋🏻‍♂️ https://t.co/mwGB6rmOZz\n"
     ]
    }
   ],
   "source": [
    "listener = LocalStreamListener()\n",
    "localStream = tweepy.Stream(api.auth, listener)\n",
    "\n",
    "# Specify coordinates for a bounding box around area of interest\n",
    "# In this case, we use San Francisco\n",
    "swCornerLat = 36.8\n",
    "swCornerLon = -122.75\n",
    "neCornerLat = 37.8\n",
    "neCornerLon = -121.75\n",
    "\n",
    "boxArray = [swCornerLon, swCornerLat, neCornerLon, neCornerLat]\n",
    "\n",
    "# Say we want to write these tweets to a file\n",
    "listener.set_log_file(open(\"tweet_log.json\", \"w\"))\n",
    "\n",
    "# Stream based on location\n",
    "localStream.filter(locations=boxArray)\n",
    "\n",
    "# Close the log file\n",
    "listener.close_log_file()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
