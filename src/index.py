from pytube import YouTube
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

video = yt.streams.get_highest_resolution()

print("Enter the destination (leave blank for the directory)")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
