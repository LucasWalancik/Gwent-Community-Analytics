
python3 main.py

ffmpeg -framerate 60 -i ./Animations/Daily-Activity/Frames/%d.png  ./Animations/Daily-Activity/Daily-Activity.mp4
ffmpeg -framerate 60 -i ./Animations/Weekly-Activity/Frames/%d.png  ./Animations/Weekly-Activity/Weekly-Activity.mp4
ffmpeg -framerate 60 -i ./Animations/Monthly-Activity/Frames/%d.png  ./Animations/Monthly-Activity/Monthly-Activity.mp4