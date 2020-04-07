"""

	RedditToSMS retrieves the last 15 posts from a given subreddit with the PRAW API.
	You can customize how often the posts will update with the timeDelay variable on line 25.

	Author: Austin Hargis
	Date: 3/13/20
	Last Updated: 3/19/20

"""

import datetime
import os, sys
import pickle
import praw
import time
from twilio.rest import Client

def createLog(message):
	logFile.write(f"[{getCurrentTime()}] {message}")
	logFile.flush()

def getCurrentTime():
	time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return time

def loadArray():

	if os.path.isfile("./idArray.p"):
		fileIn = open("./idArray.p", "rb")
		idArray = pickle.load(fileIn)
		fileIn.close()

	else:
		idArray = []

	return idArray

def saveArray():
	
	fileOut = open("./idArray.p", "wb")
	pickle.dump(idArray, fileOut)
	fileOut.close()

def getNewSubmissions():

	createLog(f"Getting {postLimit} new posts\n")

	for submission in reddit.subreddit(subredditName).new(limit = postLimit):

		if "" in submission.title.lower() or "" in submission.title.lower():

			if submission.id not in idArray:

				idArray.append(submission.id)
				saveArray()

				createLog(f"Found new post: {submission.title}\n")

				try:

					for number in numberList:
						message = client.messages.create(

							body = f"COVID-19 Update: {submission.title} \n\nVisit the link here: {submission.url}",
							from_ = sendingPhoneNumber,
							to = number,

						)

						time.sleep(5)

				except:
					createLog(f"Text did not send succesfully\n")
				finally:
					createLog(f"Text sent successfully\n")
					createLog(f"Message ID: {message.sid}\n")
				
		else:
			createLog(f"Submission doesn't contain correct criteria\n")

	createLog(f"Sleeping for {1 * timeDelay} minutes\n\n")
	try:
		time.sleep(60 * timeDelay)
	except KeyboardInterrupt:
		createLog(f"Shutdown received\n")
		logFile.close()

if __name__ == "__main__":

	"""
	Account Setup Variables
	"""
	accountSid = ""
	authToken = ""
	client = Client(accountSid, authToken)
	reddit = praw.Reddit(

			client_id = "",
			client_secret = "",		
			user_agent = "TextRedditNews"

		)

	"""
	Customization Setup Variables
	"""
	numberList = [""]
	postLimit = 15
	sendingPhoneNumber = ""
	subredditName = ""
	timeDelay = 5

	"""
	Other Variables
	"""
	idArray = loadArray()
	if not os.path.isdir("./logs"):
		os.mkdir("./logs")
	logFile = open(f"./logs/log {getCurrentTime().replace(':', '')}.txt", "a+")

	while True:
		getNewSubmissions()

	sys.exit()