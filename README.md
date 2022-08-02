# YouTubeDownloader
This script downloads YouTube videos using a Python library.

###Prerequisites
The script uses **pytube** library.
```
pip3 install --upgrade pip
pip3 install pytube3
```

###Usage
```
python3 main.py url
```
- **url** is the path to a video you want to download
Or:
```
python3 main.py file
```
- **file** is the name of the file containing several links to download separated by line breaks. The file should be in the same directory of the main.py.
