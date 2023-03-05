#!/usr/bin/python3
from flask import Blueprint, render_template, request
from os import getlogin
from sys import version_info
from json import load, loads
from flaskext.markdown import Markdown
from proxy_ninja_ng import fetch_proxies_json, fetch_proxies
from .core.utils import ProxiesChecker



views_route = Blueprint("views", __name__)





def load_json(json_file):
    global json_data
    with open(json_file) as f:
        json_data = load(f)
        return json_data


def proxies_fetch(proxy_type):
    global json_list
    json_list = []
    json_list = fetch_proxies_json(proxy_type)
    return json_list



@views_route.route("/")
@views_route.route("/home")
def home():
    user = getlogin()
    version = "Python: " + str(version_info.major) + "." + str(version_info.minor) + "." + str(version_info.micro)
    home_md = open("app/static/home.md", "r", encoding="utf-8").read()
    return render_template("home.html", user=user, version=version, home_md=home_md)



@views_route.route("/proxies", methods=['GET', 'POST'])
def proxies():
    message = "None"
    success = "None"
    if request.method == 'POST':
        prot = str(request.form.get("protocol"))
        sv = str(request.form.get("save_file"))
        fname = str(request.form.get("filename"))
        fmt = str(request.form.get("format"))
        if prot == "https" and sv == "None":
            data = loads(fetch_proxies_json("https"))
            if len(data) > 1:
                return render_template("https.html", data=data)
            else:
                message = f"{prot} - No proxies found."
                return render_template("proxies.html", message=message, success=success)
        elif prot == "socks4" and sv == "None":
            data = loads(fetch_proxies_json("socks4"))
            if len(data) > 1:
                return render_template("socks.html", data=data)
            else:
                message = f"{prot} - No proxies found."
                return render_template("proxies.html", message=message, success=success)
        elif prot == "socks4" and sv == "on":
            if fname != "":
                if fmt == "json" or fmt == "txt":
                    prot = str(request.form.get("protocol"))
                    sv = str(request.form.get("save_file"))
                    fname = str(request.form.get("filename"))
                    fmt = str(request.form.get("format"))
                    fetch_proxies(prot, fname, fmt)
                    success = f"File Successfully Saved. {fname}.{fmt}"
                    return render_template("proxies.html", message=message, success=success)
                else:
                    message = "Please select a file format."
                    return render_template("proxies.html", message=message, success=success)    
            else:
                message = "Please Enter a valid filename."
                return render_template("proxies.html", message=message, success=success)
        elif prot == "https" and sv == "on":
            if fname != "":
                if fmt == "json" or fmt == "txt":
                    prot = str(request.form.get("protocol"))
                    sv = str(request.form.get("save_file"))
                    fname = str(request.form.get("filename"))
                    fmt = str(request.form.get("format"))
                    fetch_proxies(prot, fname, fmt)
                    success = f"File Successfully Saved. {fname}.{fmt}"
                    return render_template("proxies.html", message=message, success=success)
                else:
                    message = "Please select a file format."
                    return render_template("proxies.html", message=message, success=success)
            else:
                message = "Please Enter a valid filename."
                return render_template("proxies.html", message=message, success=success)
        else:
            message = "Please select the proxy type."
            return render_template("proxies.html", message=message, success=success)
    elif request.method == 'GET':
        return render_template("proxies.html", message=message, success=success)
    else:
        message = 'Not a valid request method for this route'
        return render_template("proxies.html", message=message, success=success)
    


@views_route.route("/proxy_checker", methods=['GET', 'POST'])
def proxy_checker():
    message = "None"
    success = "None"
    if request.method == 'POST':
        proxy = str(request.form.get("proxy"))
        port = str(request.form.get("port"))
        protocol = str(request.form.get("protocol"))
        timeout = str(request.form.get("timeout"))
        if proxy != "" and port != "" and protocol != "":
            if protocol == "https":
                if timeout == "":
                    timeout = 10
                result = ProxiesChecker.https(proxy, port, timeout)
                if result:
                    success = "Proxy is working."
                    return render_template("checker.html", message=message, success=success)
                else:
                    message = "Proxy is not working."
                    return render_template("checker.html", message=message, success=success)
            elif protocol == "socks4":
                    message = " Not Implemented Yet...! Only HTTP/HTTPS is supported yet."
                    return render_template("checker.html", message=message, success=success)
            else:
                message = "Please select a Valid Protocol."
                return render_template("checker.html", message=message, success=success)
        else:
            message = "Please fill all the fields."
            return render_template("checker.html", message=message, success=success)
    else:
        return render_template("checker.html", message=message, success=success)


@views_route.route("/history")
def history():
    return render_template("history.html")


@views_route.route("/about")
def about():
    about_md = open("app/static/about.md", "r", encoding="utf-8").read()
    return render_template("about.html", about_md=about_md)
