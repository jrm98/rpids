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

# parameter 1 represents the interval between slides; default 10 sec.
if [ -z "$1" ] 
	then
	fbi -a -noverbose -t 10 loop/* &
else
	fbi -a -noverbose -t $1 loop/* &
fi