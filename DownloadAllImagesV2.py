import bs4
import requests
from bs4 import BeautifulSoup

print("This is a program to download all the images from a website")
print("This program is created by : ")
print("   ______ ")
print("  / ____/___ ___  ___________ __   __")
print(" / / __/ __ `/ / / / ___/ __ `/ | / /")
print("/ /_/ / /_/ / /_/ / /  / /_/ /| |/ / ")
print("\____/\__,_/\__,_/_/   \__,_/ |___/ ")
print("")
print("    __ __ __          _                      ")
print("   / //_// /_  ____ _(_)________  ____ ______")
print("  / ,<  / __ \/ __ `/ / ___/ __ \/ __ `/ ___/")
print(" / /| |/ / / / /_/ / / /  / / / / /_/ / /   ")
print("/_/ |_/_/ /_/\__,_/_/_/  /_/ /_/\__,_/_/     ")
print("")
print("The Images will be saved in the same folder where this file is!")
print("")

linkInput = input("Enter the link of website-")

r = requests.get(linkInput)
soup = BeautifulSoup(r.content,"html.parser")
x = soup.find_all('img')
a = 1;
images = []
for img in x:
	images.append(img.get('src'))

print(images)
for x in images:
	try:
		a = a+1
		r = requests.get(x)
		with open(str(a),'wb') as f:
			f.write(r.content)
	except:
		print("An image could not be downloaded")

print("Thanks for testing the program")
	
