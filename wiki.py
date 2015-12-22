import json, requests, webbrowser

url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'
r = requests.get(url = url)
rjson = r.json()

articlesList = rjson['query']['random']

reading = False
counter = 0

def validTitle(title):
	for c in title: 
		if ord(c) > 122:
			return False
	return True		


while reading == False:

	if counter == len(articlesList)-1:
		articlesList.append(requests.get(url=url).json()['query']['random'])

	title = articlesList[counter]['title'] #add a way to deal with unicode...this creates errors right now
	id = str(articlesList[counter]['id'])

	if validTitle(title):
		prompt = input("Would you like to read about " + title+ "? (Yes/No)")
		
		if prompt == "Yes":
			webbrowser.open("http://en.wikipedia.org/wiki?curid="+id)

		contread = input("Would you like to read more articles? (Yes/No)")
		if contread == "No":
			print("Thanks for reading!")
			reading = True

	counter = counter+1



	








