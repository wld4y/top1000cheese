from moviepy.editor import TextClip, ImageClip, ColorClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips, concatenate_audioclips
from moviepy.config import change_settings
import os
import random

from images import get_images
from transitions import add_transitions

from settings import *

# folder checks
if os.path.existss('music') == False: os.mkdir('music')
if os.listdir('music') == []: os.mkdir('music'); print('you do not have any music in the music folder! add mp3s to start.'); exit()

if os.path.exists('images') == False: os.mkdir('images')

# if using windows:
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
# if not using windows, i dont think you need to point to the binary.
# i dont know cause i haven't tested on linux yet

## creating the video

print('starting video generation')
all_clips = []

# welcome clip
background_clip = ColorClip(size=video_size, color=bg_color, duration=clip_length)

text_clip = TextClip(f"top {number_of_item} {item}", fontsize=font_size, color=text_color, font=font_path)
text_clip = text_clip.set_position("center").set_duration(clip_length)

welcome_clip = CompositeVideoClip([background_clip, text_clip])
all_clips.append(welcome_clip)

# search for and download images
images = get_images(item, number_of_item)
if images == False: print('rate limited :('); exit()
print('downloaded images!')

# creating clips
print('creating clips...')
number = number_of_item
while number != 0:
    # bg
    background_clip = ColorClip(size=video_size, color=bg_color, duration=clip_length)

    # texts
    text_clip = TextClip(f"number {number}", fontsize=font_size, color=text_color, font=font_path)
    text_clip = text_clip.set_position("center").set_duration(clip_length)

    # adds the bg and text together
    item_clip = CompositeVideoClip([background_clip, text_clip])
    all_clips.append(item_clip)
    
    # creates a clip with only an image stretched to fit the video frame
    image_clip = ImageClip(images[number-1])
    image_clip = image_clip.resize(video_size).set_duration(clip_length)
    all_clips.append(image_clip)
    
    number -= 1
    
# outro clip
background_clip = ColorClip(size=video_size, color=bg_color, duration=clip_length)

text_clip = TextClip(f"thank you for watching", fontsize=font_size, color=text_color, font=font_path)
text_clip = text_clip.set_position("center").set_duration(clip_length)

outro_clip = CompositeVideoClip([background_clip, text_clip])
all_clips.append(outro_clip)

# final video processing
print('final video processing...')
clips_transitioned = add_transitions(all_clips)
final_clip = concatenate_videoclips(clips_transitioned)

# adding music
print('adding music')
music_files = os.listdir('music')
music = []
for file in music_files: clip = AudioFileClip('music/'+file); music.append(clip)

audio = random.choice(music)
while audio.duration < final_clip.duration + 1: # adding +1 to prevent the audio from somehow being too short
    audio = concatenate_audioclips([audio, random.choice(music)])
audio = audio.subclip(0, final_clip.duration) # sets the audio to be as long as the video and cuts the rest off
    
final_clip = final_clip.set_audio(audio)


# export the final video!
print('rendering now!')
final_clip.write_videofile("output.mp4", codec="libx264", audio_codec="aac", fps=10, bitrate="20k", audio_bitrate="20k", ffmpeg_params=["-ac", "1"])