# Python script to read from a CSV file with data on top Twitch channels and find specified information
import csv

def findTwitchChannelData(firstLevelAttribute, secondLevelAttribute, sortBy=None, filename='twitchdata.csv'):
	specifiedChannels = []
	sortedChannels = []

	with open(filename, newline="") as file:
		reader = csv.DictReader(file)

		for row in reader:
			if(row[firstLevelAttribute] == secondLevelAttribute):
				specifiedChannels.append(row)

	if not specifiedChannels:
		print('No matching channels: check attribute parameters.')

	if sortBy:
		if(specifiedChannels[0][sortBy].isdigit()):
			largestValueFromChannels = max(
				specifiedChannels,
				key=lambda row: int(row[sortBy])
			)
			print(largestValueFromChannels)
		else:
			print('Sort attribute is not an integer value')
			sortedChannels = sorted(specifiedChannels, key=lambda row: row[sortBy])
			print(f'Twitch channels sorted by {sortBy}: ')
			for channels in sortedChannels:
				print(channels)

	else:
		print('Channels matching search criteria: ')
		for channels in specifiedChannels:
			print(channels)

findTwitchChannelData('Language', 'Japanese', sortBy='Partnered')