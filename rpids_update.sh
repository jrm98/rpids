#! /bin/bash

#-------------------------------------------------------------------------------
# Raspberry Pi Digital Signage
# v1.4 (08/06/2014)
# Copyright (C) 2014  Jake Martinez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

# updates dependecies
apt-get update
apt-get upgrade

cd "/home/pi/rpids"
# FTP updater for script updating
HOST=$1
USER=$2
PASS=$3

# move to tmp folder to download files
cd tmp

# open ftp connection
ftp -inv $HOST << EOF

user $USER $PASS

cd Pi/Loop

bin
mget *

cd ../Video
mget *

bye
EOF
# end of ftp connection

## uncomment the following lines to add daily backups (unstable: runs out of
## storage space relatively fast)
#cd ../backup
#tar -cf backup_`date +%F`.tar ../loop ../video
#gzip -f -1 -f backup_`date +%F`.tar
cd ..

# clears current slides and video
rm -r loop/*
rm -r video/*


cd tmp

# places supported image files in loop folder
mv ./*.jpg ../loop
mv ./*.png ../loop
mv ./*.JPG ../loop
mv ./*.PNG ../loop


# places supported video files in video folder
mv ./*.mov ../video
mv ./*.mpg ../video
mv ./*.mp4 ../video
mv ./*.mpeg ../video
mv ./*.m4v ../video

# sample of additional ways to batch move files
#mv countdown* ../video