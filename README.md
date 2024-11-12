# top 1000 cheese
script that automatically makes top 10 videos from pictures on bing

# how to setup
 - download the source zip, then extract.
 - download and install image magick [here](https://imagemagick.org/script/download.php).
 - open terminal inside of folder
 - then run `pip install -r requirements.txt` (add sudo if needed)
 - configure video settings inside of **settings.py**
 - create a folder named **"music"**
 - add music into said folder
 - if on windows, you need to find your image magick binary and edit "generate.py" accordingly. it should be on the first couple of lines.
 - in terminal, run `generate.py`
 - output should be **"output.mp4"** :)

# notices
- if you find a bug, please report it into github issues!
- images will repeat after a certain number. as far as i know there isnt really a way to fix this unless you use some sort of api. please contribute if you know how to!
