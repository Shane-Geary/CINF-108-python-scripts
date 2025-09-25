# Python script to read from a CSV file with data on top Twitch channels and find specified information
import pandas

dataFrame = pandas.read_csv('twitchdata.csv')

def findTwitchChannelData():
	# print(dataFrame.head())
	largestFollowers = dataFrame.nlargest(1, 'Followers')

	print(largestFollowers['Channel'].min())


findTwitchChannelData()