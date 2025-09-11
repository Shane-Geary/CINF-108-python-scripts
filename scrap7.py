# File I/O Python—Program will generate a bucket list and write it to a file

bucket_file = open("bucketlist.txt", 'x')

items = [
	"Skydiving\n",
	"Visit Japan\n",
	"Buy a house that costs at least $1 million\n"
	]

# Writing the bucket list items to a file
for item in items:
	bucket_file.write(item)

# Closing the connection to the file when done
bucket_file.close()