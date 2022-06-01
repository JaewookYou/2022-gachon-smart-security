#-*- coding: utf-8 -*-
import flask
import datetime, uuid, socket, json, threading, os, base64, re, time, signal, errno
from functools import wraps
import logging, traceback
import pymysql
logging.basicConfig(level=logging.INFO)
logging.getLogger('werkzeug').setLevel(level=logging.WARNING)


app = flask.Flask(__name__, static_folder='static')
app.secret_key = os.urandom(16)
app.config['MAX_CONTENT_LENGTH'] = 80 * 1024 * 1024
chatdata = {}
users = {}

# -*-*-*-*-* common methods *-*-*-*-*- #

def doLoginQuery(userid, userpw):
    conn = pymysql.connect(
        user='arangdb_admin',
        passwd='th1s_1s_4dm1n_p4ssw0rd',
        host='172.22.0.4',
        db='arangdb',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = f"select userid from arangdb.user where userid='{userid}' and userpw='{userpw}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    print(result[0])
    return result[0]

# -*-*-*-*-* flask methods *-*-*-*-*- #

@app.route("/")
def root():
    return flask.redirect(flask.url_for("login"))


@app.route("/login", methods=["GET","POST"])
def login():
    if flask.request.method == "GET":        
        if "msg" in flask.request.args:
            msg = flask.request.args["msg"]
        else:
            msg = "false"

        return flask.render_template("login.html", msg=msg)
    else:        
        queryResult = doLoginQuery(flask.request.form["userid"], flask.request.form["userpw"])
        if "userid" in queryResult:
            flask.session["userid"] = queryResult["userid"]
            resp = flask.make_response(flask.redirect(flask.url_for("index")))
            return resp
        else:
            return flask.render_template("login.html", msg="login fail!")

@app.route("/index",methods=["GET"])
def index():
    if "userid" not in flask.session:
        return "error"

    if flask.session["userid"] == "admin":
        return r"gachon{yes_y0u_ar3_log1n_as_adm1n!}"
    elif flask.session["userid"] == "guest":
        return "hello guest!"
    else:
        return f"what? you are not admin or guest.. how did you do that? {flask.session['userid']}"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=9090)
    except Exception as ex:
        pass