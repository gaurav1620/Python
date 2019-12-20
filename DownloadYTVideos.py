from pytube import YouTube                                                      


yt = YouTube(input("Enter the line and wait ! : "))
yt.streams.filter(progressive=True).all()[0].download()

