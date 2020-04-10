#!/usr/bin/env python
import os
import subprocess as sp
from moviepy.editor import VideoFileClip, concatenate_videoclips
from main import SCENES

MEDIA_FOLDER = 'media/videos/main'
QUALITY = '1440p60'
OUTPUT_FILE = 'all_scenes.mp4'

if __name__ == '__main__':
    cwd = os.getcwd()
    media_folder = os.path.join(cwd, MEDIA_FOLDER, QUALITY)
    output_file = os.path.join(cwd, MEDIA_FOLDER, OUTPUT_FILE)

    clips = []

    for scene in SCENES:
        scene_video_file = os.path.join(media_folder, f'{scene.__name__}.mp4')

        if not os.path.exists(scene_video_file):
            continue

        clips.append(
            scene.__name__
        )

    print(',\n'.join(clips))
