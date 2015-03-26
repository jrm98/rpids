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

# installs dependecies
apt-get install fbi
apt-get install ftp
apt-get install omxplayer
apt-get install python3
apt-get install python-pip

# installs python dependecies
pip install flask


# ensures dependecies are up to date
apt-get update
apt-get upgrade

cd "/home/pi/rpids"
./rpids_update.sh