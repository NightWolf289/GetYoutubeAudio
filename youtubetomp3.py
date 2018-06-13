'''
Author: Adam M. Novak
Date: 06/01/2018
Description: This program reads YouTube links from downloadlist.txt. The links shoud be placed one per line.
the program then places the mp4 files in a folder.
Required: Python3.6, pytube, moviepy, ffmpeg
'''
from pytube import YouTube
from os import getcwd
from os import listdir
from os import path
from os import remove
from moviepy.audio.io.ffmpeg_audiowriter import ffmpeg_audiowrite
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pathlib import Path
#import mutagen


errorList = []
print('YouTube to MP4 v3.0\n')
file = open('downloadlist.txt', 'r') 
for line in file: 
    #open the youtube video, get the mp4 audio stream, and save it to a file
    ogVid = YouTube(line)
    yt = ogVid.streams.filter(only_audio=True, subtype='mp4')
    if yt.count() == 0:
        yt = ogVid.streams.filter(subtype='mp4')
    yt.first().download(getcwd() + '/.trash')

    #erase special characters from file name search to match the file created by the YouTube downloader
    vidTitle = ogVid.title
    vidTitle = vidTitle.replace(',' , '')
    vidTitle = vidTitle.replace('\'', '')
    vidTitle = vidTitle.replace('\"', '')
    vidTitle = vidTitle.replace('.', '')
    vidTitle = vidTitle.replace(';', '')
    vidTitle = vidTitle.replace(':', '')
    vidTitle = vidTitle.replace('$', '')
    vidTitle = vidTitle.replace('\\', '')
    vidTitle = vidTitle.replace('/', '')
    vidTitle = vidTitle.replace('?', '')
    vidTitle = vidTitle.replace('*', '')
    vidTitle = vidTitle.replace('<', '')
    vidTitle = vidTitle.replace('>', '')
    vidTitle = vidTitle.replace('|', '')
    vidTitle = vidTitle.replace('#', '')
    vidTitle = vidTitle.replace('%', '')
    vidTitle = vidTitle.replace('~', '')

    #throws an error if the file is not found
    my_file = Path(getcwd() + '/.trash/' + vidTitle + '.mp3')
    try:
        my_abs_path = my_file.resolve(strict=True)
    except FileNotFoundError:
        # doesn't exist
        print('ERROR. \n' + ogVid.title + ' was not downloaded')
        errorList.append(ogVid.title)
    else:
        # exists
        #open the video with moviepy and save it to clip the weird silence off of the end
        #brew reinstall ffmpeg --with-libvorbis --with-libavformat
        #sudo apt-get install ffmpeg libavcodec-extra-52
        clip = AudioFileClip(getcwd() + '/.trash/' + vidTitle + '.mp4')
        clipLen = clip.duration
        clip.close()
        clip = AudioFileClip(getcwd() + '/.trash/' + vidTitle + '.mp4').subclip(0, clipLen/2)
        ffmpeg_audiowrite(clip, getcwd() + '/MusicFiles/' + vidTitle + '.mp3', fps=44100, nbytes=4, buffersize=2000, codec='libmp3lame') 
        #libavformat
        #libvorbis
        #libxvid
        #libx264
        #libmp3lame
        clip.close() 
        print(ogVid.title + ' DOWNLOADED')
file.close()

#delete all the useless files in the .trash folder
filelist = [ f for f in listdir(getcwd() + '/.trash/') if f.endswith('.mp4') ]
for f in filelist:
    remove(path.join(getcwd() + '/.trash/', f))
print('\nYouTube to MP3 EXITED.')

#print out a list of videos that were not downloaded
if len(errorList) > 0:
    print('WARNING. ' + str(len(errorList)) + ' videos not downloaded.')
    for x in errorList:
        print(x + ' was not downloaded.')