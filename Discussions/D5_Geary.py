# Python script to read from a CSV file with data on top Twitch channels and find specified information
import csv
from datetime import timedelta

def findTwitchChannelData(searchParam, sortBy=None, filename='twitchdata.csv'):
	channels = []

	with open(filename, newline="") as file: # Utilize 'csv' library to open CSV file and loop through the data
		reader = csv.DictReader(file)

		for row in reader: # Loop through rows (each twitch channel) and append to list
			channels.append(row)

	# Find the channel with the greatest value of the attribute specified by the searchParam argument (First criteria)
	mostWatchedChannel = max(channels, key=lambda row: int(row[searchParam]))
	seconds = int(mostWatchedChannel[searchParam]) # Convert to int for the timedelta library conversion
	print(f'{mostWatchedChannel['Channel']} has the most watch time, totalling at {timedelta(seconds=seconds)}')
	# Error handling
	if not channels:
		print('No matching channels: check attribute parameters.')
	else:
		# Check whether the most watched channel is partnered (Second criteria)
		if(mostWatchedChannel[sortBy] == 'True'):
			print('This streamers channel is partnered.')
		else:
			print('This streamers channel is not partnered.')

findTwitchChannelData('Watch time(Minutes)', sortBy='Partnered')