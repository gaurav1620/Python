
# Execute the program with python3 or you will get an error that bs4 is not found

import bs4
import requests
from bs4 import BeautifulSoup

# print("This program is created by : ")
# print("   ______ ")
# print("  / ____/___ ___  ___________ __   __")
# print(" / / __/ __ `/ / / / ___/ __ `/ | / /")
# print("/ /_/ / /_/ / /_/ / /  / /_/ /| |/ / ")
# print("\____/\__,_/\__,_/_/   \__,_/ |___/ ")
# print("")
# print("    __ __ __          _                      ")
# print("   / //_// /_  ____ _(_)________  ____ ______")
# print("  / ,<  / __ \/ __ `/ / ___/ __ \/ __ `/ ___/")
# print(" / /| |/ / / / /_/ / / /  / / / / /_/ / /   ")
# print("/_/ |_/_/ /_/\__,_/_/_/  /_/ /_/\__,_/_/     ")
# print("")

usrname = input("Enter the usename : ")
linkInput = 'https://github.com/'+usrname+'?tab=repositories'
r = requests.get(linkInput)

soup = BeautifulSoup(r.content,"html.parser")

#currently it is only getting the first page repositories
rawList = soup.find_all('a',itemprop='name codeRepository')

repList = []


for i in range(len(rawList)):
	repList.append(rawList[i].string.lstrip())
	print(i,rawList[i].string.lstrip())

ind = int(input("\nEnter the repository Number you want to enter : "))
repLink = 'https://github.com/'+usrname+'/'+repList[ind]

s = requests.get(repLink)
repSoup = BeautifulSoup(s.content,'html.parser')


repRawList = repSoup.find_all('span',class_='css-truncate css-truncate-target')
# print(repRawList)
repContentNames = []
repContentLinks = []


for i in range (len(repRawList)):
	if(i%3 == 0):
		repContentNames.append(repRawList[i].contents[0].contents[0])
		repContentLinks.append('https://github.com'+repRawList[i].contents[0]['href'])
	
for i in range(len(repContentNames)):
	print(i,' : ',repContentNames[i])

print("Enter the file Number you want to enter : ")
arg = input()
arg = int(arg)



print(repContentLinks[arg])

# print(repContent);

# for i in range(len(repRawList)):
# 	repContent.append(repRawList[i].string.lstrip())
# 	print(i,repRawList[i].string.lstrip())


	
