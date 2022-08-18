[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# Neo ProxyNinja
Web-Application for Python script to get https or socks(4) proxies by scraping the web using StealthChromiumDriver.

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/framework-flask-informational?style=flat-square&logo=flask&logoColor=white&color=5194f0&bgcolor=110d17)
##
### Operating System(Tested)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)

> Only tested on Ubuntu/Debian Linux...

>> 🚨 This script **Un-Officially** supports Windows and Mac OS.
##

### 📚 Requirements
> - Python 3.9+
> - ChromeDriver
> - Selenium
> - Flask

##

### Installation

Before installing the python3 requirements , please install the ChromiumDriver as following debian/kali

```bash
    sudo apt-get update && sudo apt-get full-upgrade -y
    sudo apt-get install chromium-driver
    python3 -m pip install -r requirements.txt
```

##

### Usage
> Please run the following command for Production server.
```bash
gunicorn -w 10 'app:create_app()'
```
OR

> For Development server
```bash
python3 Neo-ProxyNinja.py
```

##

### 🗿 Pypi
> Proxy Ninja is also available as [python3](https://www.python.org/) module on [Pypi](https://pypi.org/).

- Pypi package [Proxy Ninja](https://pypi.org/project/proxy-ninja/)

[![PyPI version](https://badge.fury.io/py/proxy-ninja.svg)](https://badge.fury.io/py/proxy-ninja)
##

### ⚡️Github
[![GitHub version](https://badge.fury.io/gh/sc4rfurry%2FProxy-Ninja.svg)](https://badge.fury.io/gh/sc4rfurry%2FProxy-Ninja)
> See the **cli** version on [github](https://github.com/sc4rfurry/Proxy-Ninja) for Installation and Usage.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


##

## Features

- Web UI written in flask
- ChromeDriver to scrape the site.
- Stealth Profle implmented.
- save output in txt or json format.
- User Friendly. :D

## ToDo
- Proxy Checker backend implementation.
- Optimize the workflow
- Application Optimization
- More bugs to fix

## Known Issues

- Checker tab's backend is not implemented yet.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch

