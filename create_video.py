from moviepy.editor import *
import pyttsx3

# Read story from file
with open('story.txt', 'r') as file:
    story = file.read()

# Text-to-speech
engine = pyttsx3.init()
engine.save_to_file(story, 'story_audio.mp3')
engine.runAndWait()

# Load media files
background = VideoFileClip('background.mp4').subclip(0, 60)
audio = AudioFileClip('story_audio.mp3')

# Create subtitles
subtitles = TextClip(story, fontsize=24, color='white', size=background.size)
subtitles = subtitles.set_duration(60).set_position(('center', 'bottom'))

# Create final video
final = CompositeVideoClip([background, subtitles])
final = final.set_audio(audio)
final.write_videofile('final_video.mp4', codec='libx264')
