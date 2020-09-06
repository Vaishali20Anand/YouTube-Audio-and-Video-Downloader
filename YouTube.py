import pafy

#Code for video
#You can replace link here
url = "https://www.youtube.com/watch?v=07d2dXHYb94"
video = pafy.new(url) 
  
streams = video.streams 
for i in streams: 
    print(i) 
      
# get best resolution regardless of format 
best = video.getbest() 
  
print(best.resolution, best.extension) 
  
# Download the video 
best.download() 

#Code for audio
#You can replace link here

url = "https://www.youtube.com/watch?v=07d2dXHYb94"
video = pafy.new(url) 
  
bestaudio = video.getbestaudio() 
bestaudio.download() 
