# SRT_SYNC
A simple program to help sync up *.srt subtitle files.

Some times srt subtitle files don't perfectly match the video files in terms of start and end point or in terms of exact playback speed
which leads to the need to sync up the subtitle file to match up the brgining and the pace of the movie better - this program helps you do that!

Usage:
1. install python on your system and add it to PATH
2. run the program by typing python SRT_SYNC.py in the comandline
3. provide the absolute or relative path to the *.srt file in need of fixing
4. provide the time when the firs line shuld apear
5. provide the time when the last line shuld apear

if everything worked as expected a new copy of the original *.srt file will be created beside it with ".out" apended to it's file name

p.s. vlc doesn't like it when the filename ends with .out instead of .srt so I recommend renaming the output file accordingly =]
