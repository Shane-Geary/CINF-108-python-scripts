# Python script to read from a CSV file with data on top Twitch channels and find specified information
import csv

def findTwitchChannelData():
	with open('twitchdata.csv', newline="") as file:
		reader = csv.DictReader(file)

		japanChannels = []
		for row in reader:
			if(row["Language"] == 'Japanese'):
				# print(row)
				japanChannels.append(row)

		# for channel in japanChannels:
		# 	print(channel['Followers'])
			# followers.append(channel['Followers'])

		mostFollowedJapanChannel = max(
			japanChannels,
			key=lambda row: int(row['Followers'])
		)
		
		print(mostFollowedJapanChannel['Average viewers'])

findTwitchChannelData()