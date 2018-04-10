#!/bin/bash

## pi-frame, a digital picture frame aimed at randparents.
## date: 2018-03-22
## email: bond@mindcont.com
## platform:  ubuntu 14.04 x86_64
## More related projects
##    https://github.com/fvdbosch/ConnectedFrame
##    https://github.com/mrwangyu2/DigitalPhotoFrame/
##    https://github.com/libbymiller/pi-frame
##    http://hongjiang.info/tag/feh/
## --------------------------------------------------------------
## Detail:
## The idea is that parents taking pictures of their children, can easily share those pictures with
## the children's grandparents by making them appear on the picture frame automatically.
## In turn, the grandparents can "like" the pictures, letting the children's parents know which pictures
## are their favourites.
## --------------------------------------------------------------
# echo "  _____ _____      ______ _____            __  __ ______ ";
# echo " |  __ \_   _|    |  ____|  __ \     /\   |  \/  |  ____|";
# echo " | |__) || |______| |__  | |__) |   /  \  | \  / | |__   ";
# echo " |  ___/ | |______|  __| |  _  /   / /\ \ | |\/| |  __|  ";
# echo " | |    _| |_     | |    | | \ \  / ____ \| |  | | |____ ";
# echo " |_|   |_____|    |_|    |_|  \_\/_/    \_\_|  |_|______|";
# echo "                                                         ";
# echo "    A digital picture frame aimed at family members,     ";
# echo "             such as grandparents.                       ";
# echo "                                                         ";
# echo "                                                         ";

#Generated listfile first on each start.
function getlist(){
  #cd command run path
  cd /home/pi/Seafile/dev
  echo "============$(date '+%Y/%m/%d %H:%M.%S %A')============"
  ls photos/ | sed "s:^:`pwd`/photos/:" > photos.list
  ls videos/ | sed "s:^:`pwd`/videos/:" > videos.list
  sleep 3
  echo "Generated filelist successfully"
}

#show phoots on /home/pi/Seafile/dev/photos folder.
function show_pic(){
  DISPLAY=:0.0 feh --auto-zoom --cycle-once --draw-filename \
  --fontpath /usr/share/fonts/truetype/droid/ --font DroidSansFallbackFull/30 \
  --full-screen --hide-pointer \
  --no-menus --preload -x  \
  --quiet --slideshow-delay 5 \
  /home/pi/Seafile/dev/photos
  sleep 3
  echo "show pictures successfully"
}

# play videos on /home/pi/Seafile/dev/videos folder.
function play_video() {
  # mplayer -fs -framedrop -msglevel all=1 -nomouseinput -nojoystick  -noar -nolirc -playlist videos.list
  # or use ~/.mplayer/config
  DISPLAY=:0.0 mplayer -playlist videos.list
  sleep 3
  echo "play videos successfully"
}
# sh /home/pi/Seafile/dev/pi-frame.sh | tee -a /home/pi/Seafile/dev/pi-frame-debug.log
function main() {
  getlist
  show_pic
  play_video
  #xset -display :0.0 dpms force off
}
main
