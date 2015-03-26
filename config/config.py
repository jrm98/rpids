
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
# 
# Author: Jake Martinez (jrm98@vt.edu)
# Description: Creates a json file with playlist data in the specified format
#		for use with the rpi-dsignage.py program.
#
# For the latest version, visit github.com/jrm98/raspi-dsign
#-------------------------------------------------------------------------------

import sys, getopt, json
from pprint import pprint

# called if incorrect usage was performed
def usage():
	print('./rpi-dsignage.py [-am] [-u <auto,on,off>] [PLAYLIST PATH]')
	pass

def main(argv):
	# process command line arguments
	#  - options for:
	#          > auto updating enabled "-a" "--auto-update"
	#          > auto updating disabled (manual) "-m" "--manual-update"
	#          > play <video> video at <time> time "-p "
	#          > video playback settings
	#          > ftp/sftp source destination
	try:
		opts, args = getopt.getopt(argv, "amu:", 
			["ftp="])
	except getopt.GetoptError as err:
		print(str(err))
		usage()
		sys.exit(2)

	print(opts)
	print(args)
	for o, a in opts:
		if o == "-u":
			pass
		elif o == "--ftp":
			pass
		elif o in ("-a", "--auto-update"):
			pass
		elif o in ("-m", "--manual-update"):
			pass
		else:
			usage()
			assert False, "invalid option"

	# load playlist data
	if len(args) > 0:
		json_file = args[0]
	else:
		json_file = 'rpids_default.json'

	try:
		json_data = open(json_file)
		data = json.load(json_data)
		pprint(data)
		json_data.close()
	except FileNotFoundError as err:
		print('rpids: could not find playlist "' + json_file + '"')

		if json_file == 'rpids_default.json':
			# create a new default playlist
		print('')

	

if __name__ == '__main__':
	main(sys.argv[1:])




