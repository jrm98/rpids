RPiDS
===================
#####Raspberry Pi Digital Signage Software

####Description
RPiDS is a digital signage manager program designed to run on a Raspbian based, Raspberry Pi system to be used as a means of producing imagery for display. The goal of this project is to produce a flexible, user-friendly, and cost effective alternative to professional digital signage systems of the same type. Furthermore, this system employs a Flask-based web service that is used to act as an interface between the user and the systems functionality

####Installation and Dependencies
There are a few major dependecies that RPiDS relies on to perform core tasks such as displaying photos or videos. For photo/video display, RPiDS utilizes the ```omxplayer``` and ```fbi``` programs. Also, for enhanced functionality, RPiDS uses ```ftp``` to pull new content from a centralized server, ```screen``` to allow RPiDS to run in the background, and ```Flask``` to allow administrators to access a control panel remotely.

All of these packages can be installed quickly and easily by running the included ```scripts/install.sh``` script.


