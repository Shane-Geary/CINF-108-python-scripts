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

	return (
		f"{list(adjustedRecipe.keys())[0]}: {list(adjustedRecipe.values())[0]}\n"
		f"{list(adjustedRecipe.keys())[1]}: {list(adjustedRecipe.values())[1]}\n"
		f"{list(adjustedRecipe.keys())[2]}: {list(adjustedRecipe.values())[2]}\n"
	)

print(bakeCookies(104))