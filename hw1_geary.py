# Shane T Geary
# CINF: 108
# 08/21/2025
# University at Albany

# Python script to run calculations on the scores of a programming competition candidate and return the spreads and final score.
computational_programming = [21, 32, 28, 24, 29]

robotics_freestyle = [24, 28, 19, 23, 24]

def scoreComputations(programming, robotics):
	computationalProgrammingInstance = computational_programming.copy()
	roboticsFreestyleInstance = robotics_freestyle.copy()

	maxMinProgrammingScores = [max(computationalProgrammingInstance), min(computationalProgrammingInstance)]
	maxMinRoboticsScores = [max(roboticsFreestyleInstance), min(roboticsFreestyleInstance)]

	for index in maxMinProgrammingScores:
		if index in computationalProgrammingInstance:
			computationalProgrammingInstance.remove(index)

	computationalAverage = sum(computationalProgrammingInstance) / 3
	computationalSpread = (maxMinProgrammingScores[0] - maxMinProgrammingScores[1]) / computationalAverage

	for index in maxMinRoboticsScores:
		if index in roboticsFreestyleInstance:
			roboticsFreestyleInstance.remove(index)

	roboticsAverage = sum(roboticsFreestyleInstance) / 3
	roboticsSpread = (maxMinRoboticsScores[0] - maxMinRoboticsScores[1]) / roboticsAverage

	finalScore = sum(computationalProgrammingInstance) + sum(roboticsFreestyleInstance)
	
	return (
		f"Computational Programming scores {computational_programming}\n"
		f"Robotics Freestlye scores {robotics_freestyle}\n"
		f"Spread of the Computational Programming is {round(computationalSpread, 12)}\n"
		f"Spread of the Robotics Freestyle is {round(roboticsSpread, 12)}\n"
		f"The total score for the competitor is {finalScore}"
	)

print(scoreComputations(computational_programming, robotics_freestyle))