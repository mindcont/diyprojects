# Pi Frame

A digital picture frame aimed at grandparents.

```css
  _____ _____      ______ _____            __  __ ______
 |  __ \_   _|    |  ____|  __ \     /\   |  \/  |  ____|
 | |__) || |______| |__  | |__) |   /  \  | \  / | |__   
 |  ___/ | |______|  __| |  _  /   / /\ \ | |\/| |  __|  
 | |    _| |_     | |    | | \ \  / ____ \| |  | | |____
 |_|   |_____|    |_|    |_|  \_\/_/    \_\_|  |_|______|

    A digital picture frame aimed at family members,     
             such as grandparents.                       
```

The idea is that parents taking pictures of their children, can easily share those pictures with the children's grandparents by making them appear on the picture frame automatically. In turn, the grandparents can "like" the pictures, letting the children's parents know which pictures are their favourites.


#### More related projects

 * https://github.com/fvdbosch/ConnectedFrame
 * https://github.com/mrwangyu2/DigitalPhotoFrame/
 * https://github.com/libbymiller/pi-frame
 * http://hongjiang.info/tag/feh/

### Install

```
# feh — image viewer and cataloguer, more visit doc or `man feh`
$ sudo apt-get install feh

# mplayer  - movie player
$ sudo apt-get install mplayer

$ git clone https://github.com/mindcont/diyprojects-raspbian diy
$ cd diy
```
before doing this ,just change the folder path `/home/pi/Seafile/dev` as your local path.
```
$ bash pi-frame.sh
```

### Timer
By use crontab, we can timed execution the script to show the pictures and videos.
```
$ sudo apt-get install postfix
$ sudo systemctl list-unit-files | grep cron
$ sudo systemctl status cron
$ sduo systemctl start cron
$ crontab -e
```
For example，performed once every 15 minutes
```
# minute   hour   day   month   week   command
30 7-20 * * * bash /home/pi/iot/frame/pi-frame.sh >> "/home/pi/iot/frame/log/$(date +"frame_debug_%Y-%m-%d").log" 2>&1
```

### License
© 2018 张正轩 [知识共享 署名-非商业性使用](http://creativecommons.org/licenses/by-nc-sa/4.0/)
