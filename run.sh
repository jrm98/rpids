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

export RPIDS_DIR=/home/pi/rpids

echo ""
echo "-------------------------------------------------------------"
echo "Spawning background daemon SCREEN named rpids." 
echo "To resume: type screen -r rpids."
echo "To detach from screen: press the magic sequence: ctrl-A, D."
echo "To quit rpids:1) type at terminal: screen -r rpids"
echo ". . . . . . . 2) type: stop"
echo "-------------------------------------------------------------"
echo ""

#Change user working directory for preparation of "java -jar" command
cd $RPIDS_DIR

#Check to see if a rpids screen is already running
lineCount=`screen -r rpids | grep "There is no screen to be resumed matching rpids." | wc -l`

#Start the rpids server in a detached screen named "rpids" if its not running
#Launch the command line interface for rpids if it is arealdy running.
if [ $lineCount -eq 1 ]
  then
    echo linecount: $lineCount. Starting in a detached screen named rpids. Use screen -r rpids to view.
    screen -dmS rpids python $RPIDS_DIR/rpids_server.py
  else
    echo linecount: $lineCount. RPiDS is already running. Use screen -r rpids to view. Running now.
    screen -r rpids
fi
