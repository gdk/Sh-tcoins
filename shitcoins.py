# shitcoins!
import hashlib
import random
import gdata.youtube
import gdata.youtube.service
import xml.dom.minidom
import sys

currentShitCoins = 0.0
currentNonce = 0

currentDifficulty = "000000ffffff0000000000000000000000000000000000000000000000000000"

yt_service = gdata.youtube.service.YouTubeService()
videoIds = []

try:
	f = open("myshit.txt", "r")
	currentShitCoins = float(f.read())
	f.close()
	
	print "found your shit"
except:
	print "no shit"

if len(sys.argv) <= 1:
	print "usage: give video_ids as arguments: shitcoins [...video_ids...]"
	sys.exit()
	
for ids in sys.argv[1:]:
	videoIds.append(ids)

for vid in videoIds:
	print "finding shit..."
	try:
		feed = yt_service.GetYouTubeVideoCommentFeed(video_id=vid)
	
	except:
		print "didn't find shit.  check your video ids"
		sys.exit()
		
	shitMine = []

	print "receiving shit..."

	for comment in feed.entry:
		dom = xml.dom.minidom.parseString(comment.ToString())
		for item in dom.getElementsByTagName("ns0:content"):
			shitMine.append(item.firstChild.nodeValue)
		
	print "mining shit..."

	for currentNonce in range(0, 1000000):
		for currentHash in shitMine:
			hash = hashlib.sha256(currentHash.encode('latin-1') + str(currentNonce)).hexdigest()
	
			if int(hash, 16) < int(currentDifficulty, 16):
				thisIsTheNewShit = .0001 * random.random()
				currentShitCoins += thisIsTheNewShit
				exchangeRate = random.randint(1, 10) * random.random() / (random.randint(1, 10000) * random.random())
				print "Congratulations!  You got", thisIsTheNewShit, "shitcoins with total of", currentShitCoins, "!  That's equal to", currentShitCoins * exchangeRate, "USD with the current exchange rate of 1 =", exchangeRate, "USD/SHT"
	
print "saving shit..."
try:
	f = open("myshit.txt", "w")
	f.write(str(currentShitCoins))
	f.close()
	
except:
	print "lost your shit"
