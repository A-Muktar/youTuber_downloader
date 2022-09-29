from pytube import YouTube
link = input("Enter the link:  ")
print("Downloading please wait...")
YouTube(link).streams.first().download()
print("Video download successfully")
input()