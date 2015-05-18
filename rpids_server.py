#! /usr/bin/env python
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

# uses web browser interface

import sys, time, os, subprocess, signal, ConfigParser
from flask import Flask
from functools import wraps
from flask import request, Response, render_template, flash
import rpids

app = Flask(__name__)
app.debug = False

pid = 0
stat = False

if not stat:
    stat = True
    pid = os.fork()
    if pid == 0:
        subprocess.call(["python", "rpids.py"])
        os._exit(EX_OK)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


# webpage building functions --------------------------------------------------
def header():
    return "<head>\
                <title>Raspberry Pi Digital Signage</title>\
            </head>"

def style(arg):
    return "<style>" + arg + "</style>"

def unit_display(units):
    u = "<ul>"
    for unit in units:
        u += "<li>" + unit + "</li>"
    u += "</ul>"

    return u

def shutdown_server():
    subprocess.call(["sh", "scripts/killproc.sh"])
    global pid
    try:
        os.killpg(os.getpgrp(), signal.SIGTERM)
    except Exception:
        print "No child processes"
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# dashboard
@app.route("/")
@requires_auth
def dashboard():
    return render_template('home.html')

# starts the defaul playlist
@app.route("/start")
@requires_auth
def start():
    global stat
    global pid
    if not stat:
        stat = True
        pid = os.fork()
        if pid == 0:
            subprocess.call(["python", "rpids.py"])
            os._exit(EX_OK)
        return render_template('start.html')
    return render_template('start_e.html')

# starts the desired playlist
@app.route("/start/<playlist>/")
@requires_auth
def start_playlist(playlist):
    return render_template('home.html')

# stops the current playlist, if one is playing
@app.route("/stop")
@requires_auth
def stop():
    global stat
    global pid
    if stat & (pid != 0):
        stat = False
        os.kill(pid, signal.SIGTERM)
        subprocess.call(["sh", "scripts/killproc.sh"])
        return render_template('stop.html')
    subprocess.call(["sh", "scripts/killproc.sh"])
    stat = False
    return render_template('stop_e.html')

# starts the defaul playlist
@app.route("/status")
@requires_auth
def status():
    global stat
    s = "<html> "
    s += header()
    s += " <body> <h1>Raspberry Pi Digital Signage</h1> "
    s += "<h2>System Manager - alpha version</h2> "
    s += "<b>Status</b>: "
    if stat:
        s += "Running"
    else:
        s += "Stopped"
    s += "<br><br><br><a href='/'>back</a></body></html>"
    return s

# runs update scripts
@app.route("/update")
@requires_auth
def update():
    config = ConfigParser.ConfigParser()
    config.read('default.ini')
    subprocess.call(
        ["sh", "scripts/update.sh", 
        config.get('FTP','host'), 
        config.get('FTP','user'), 
        config.get('FTP','pass')], 
        shell=True)
    return render_template('update.html')

# powers off and restarts the unit
@app.route("/restart")
@requires_auth
def restart():
    return render_template('restart.html')

# powers off the unit
@app.route("/shutdown")
@requires_auth
def shutdown():
    shutdown_server()
    return render_template('shutdown.html')

# starts the desired playlist
@app.route("/logout")
@requires_auth
def logout():
    return render_template('logout.html')


app.run(host='0.0.0.0')
try:
    os.killpg(os.getpgrp(), signal.SIGTERM)
except Exception:
    print "No child processes"

print "rpids_server exiting..."