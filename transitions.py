from moviepy.editor import *

def add_transitions(clips, duration=0.4):
    new_clips = []
    for clip in clips:
        new_clip = clip.fx(vfx.fadein, duration).fx(vfx.fadeout, duration)
        new_clips.append(new_clip)
    return new_clips