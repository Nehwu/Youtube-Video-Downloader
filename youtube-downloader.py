from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("There has been an error in downloading the youtube video")
  print("Download completed")

link = input("Input the link of the video. URL: ")
Download(link)
