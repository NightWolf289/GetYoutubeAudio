Prerequisites:
Programs:
	python3.6
	ffmpeg
Python Libraries:
	pytube
	moviepy

There are two programs. One program is for downloading individual YouTube videos directly to MP4 (audio only). The second program is for downloading entire playlists to individual MP4 files (again, audio only).

Instructions for the YouTube to MP4 audio downloader:
1) Place a link to each YouTube video in downloadlist.txt, one per line.
2) Open Terminal (Command + Space and type in Terminal).
3) Using "ls" to see the files in the current directory and "cd <FolderName>" ("cd .." to go back up one level), navigate into the folder YouTubetoMP4. (Use Finder to assist you by viewing the folders if you are having difficulties.)
4) Type "python3.6 youtubetomp4.py" into the terminal.
5) Hit enter.
6) Enjoy.

Instructions for the YouTube Playlist to MP4 audio downloader:
1) Place a link to each YouTube playlist in downloadplaylist.txt, one per line.
2) Open Terminal (Command + Space and type in Terminal).
3) Using "ls" to see the files in the current directory and "cd <FolderName>" ("cd .." to go back up one level), navigate into the folder YouTubetoMP4. (Use Finder to assist you by viewing the folders if you are having difficulties.)
4) Type "python3.6 playlisttomp4.py" into the terminal.
5) Hit enter.
6) Enjoy.

Additional Notes:
1) The folder can be located anywhere on your computer.
2) Typing Ctrl + C in the terminal will interrupt the program and force it to end prematurely.
3) The program can take some time to run, especially with our internet. Once it's running, you can leave it alone and go do something else. Let it work its magic.
4) The playlist/video must be public or unlisted. If it is private, the program will not work.