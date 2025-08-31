# Shane T Geary
# CINF: 108
# 08/24/2025
# University at Albany

# Script to calculate how much of each ingredient is needed for X amount of cookies

fourtyEightCookies = {
	"cupsOfSugar": 1.5,
	"cupOfButter": 1,
	"cupsOfFlour": 2.75
}

def bakeCookies(cookies):
	scaleFactor = cookies / 48
	adjustedRecipe = {}
	for ingredient, amount in fourtyEightCookies.items():
		adjustedRecipe[ingredient] = round(amount * scaleFactor, 2)

	return adjustedRecipe

print(bakeCookies(730))