#!/usr/bin/python3
from flask import Blueprint, render_template, request
from os import getlogin
from sys import version_info
from json import load
from proxy_ninja import proxies_json, fetch_proxies
from flaskext.markdown import Markdown


views_route = Blueprint("views", __name__)






def load_json(json_file):
    global json_data
    with open(json_file) as f:
        json_data = load(f)
        return json_data


def proxies_fetch(proxy_type):
    global json_list
    json_list = []
    json_list = proxies_json(proxy_type)
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
    # data = load_json("app/abc_socks.json")
    message = "None"
    success = "None"
    if request.method == 'POST':
        prot = str(request.form.get("protocol"))
        sv = str(request.form.get("save_file"))
        fname = str(request.form.get("filename"))
        fmt = str(request.form.get("format"))
        if prot == "https" and sv == "None":
            proxies_fetch("https")
            data = json_list
            data_len = len(data)
            return render_template("https.html", data=data, data_len=data_len)
        elif prot == "socks4" and sv == "None":
            proxies_fetch("socks")
            data = []
            for i in json_list:
                if i['IP Address'] not in data:
                    data.append(i)
            data_len = len(data)
            return render_template("socks.html", data=data, data_len=data_len)
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
                    return render_template("proxies.html", message=message)    
            else:
                message = "Please Enter a valid filename."
                return render_template("proxies.html", message=message)
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
                    return render_template("proxies.html", message=message)
            else:
                message = "Please Enter a valid filename."
                return render_template("proxies.html", message=message)    
        else:
            message = "Please select the proxy type."
            return render_template("proxies.html", message=message)
    elif request.method == 'GET':
        return render_template("proxies.html", message=message, success=success)
    else:
        return 'Not a valid request method for this route'
    


@views_route.route("/proxy_checker", methods=['GET', 'POST'])
def proxy_checker():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')
            # proxy: 1
            # port: 2
            # protocol: https
            # timeout: 12
        return "123"
    else:
        return render_template("checker.html")


@views_route.route("/history")
def history():
    return render_template("history.html")


@views_route.route("/about")
def about():
    about_md = open("app/static/about.md", "r", encoding="utf-8").read()
    return render_template("about.html", about_md=about_md)