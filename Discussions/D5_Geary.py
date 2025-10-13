# Python script to read from a CSV file with data on top Twitch channels and find specified information
import csv
from datetime import timedelta

def findTwitchChannelData(searchParam, sortBy=None, filename='twitchdata.csv'):
	channels = []

	with open(filename, newline="") as file:
		reader = csv.DictReader(file)

		for row in reader:
			channels.append(row)

	mostWatchedChannel = max(channels, key=lambda row: int(row[searchParam]))
	print(type(mostWatchedChannel[searchParam]))
	seconds = int(mostWatchedChannel[searchParam])
	print(f'{mostWatchedChannel['Channel']} has the most watch time, totalling at {timedelta(seconds=seconds)}')
	if not channels:
		print('No matching channels: check attribute parameters.')
	else:
		if(mostWatchedChannel[sortBy] == 'True'):
			print('This streamers channel is partnered.')
		else:
			print('This streamers channel is not partnered.')

findTwitchChannelData('Watch time(Minutes)', sortBy='Partnered')