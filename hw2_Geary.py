# Shane T Geary
# CINF: 108
# 08/25/2025
# University at Albany

# Script to calculate how much rain it takes to operate both locks of the Panama Canal for a full year, 
# assuming an average of 35 ships pass through each lock daily. 
# It then estimates the daily rain required during the 9-month rainy season, 
# and converts this to millimeters of rainfall per day.

waterVolume = 0
millimetersOfRainFactor = 600000 # Number representing cubic meters of water in lake = 1 millimeter of rain fall

def volume_solid(width, length, depth): # Find the volume of water needed to fill a single container/lock of given dimensions
	global waterVolume
	filledLockWaterVolume = width * length * depth
	waterVolume = filledLockWaterVolume
	return filledLockWaterVolume

volume_solid(32, 320, 10) # Pass in dimensions of the lock

# Find the volume of water needed to fill a container/lock for a full year,
# how much rain must fall during the 9 month rainy season,
# and around how many millimeters of daily rain occurs during that season
def water_needed_perlock(volume):
	shipsPerDay = 35
	yearlyWaterVolumeReq = volume * 365 * shipsPerDay
	rainySeasonDailyRainReq = yearlyWaterVolumeReq / (30 * 9)
	dailyMMRainConversion = round(rainySeasonDailyRainReq / millimetersOfRainFactor, 10)

	return (
		f"Panama canal statistics:\n"
		f"The total volume of water needed in Gatun lake: {yearlyWaterVolumeReq} m³\n"
		f"In the rainy season, daily rain should be at least: {round(rainySeasonDailyRainReq)} m³\n"
		f"This means, it rains about {dailyMMRainConversion} millimeters every day during the rainy season"
	)

print(water_needed_perlock(waterVolume * 2)) # Account for both locks by multiplying waterVolume by 2