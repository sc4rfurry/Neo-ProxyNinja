[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# Neo ProxyNinja
A flask Web-Application that Fetches free proxies (HTTP/HTTPS/Socks4) from websites and api's using [ProxyNinja-ng](https://pypi.org/project/proxy-ninja-ng/).

<hr>

## Table of Contents
  - [🔧 Technologies & Tools](#-technologies--tools)
  - [Operating System(Tested)](#operating-systemtested)
  - [📚 Requirements ](#-requirements-)
  - [🚀 Installation](#-installation)
    - [📝 Usage](#-usage)
  - [🗿 Pypi](#-pypi)
  - [⚡️Github](#️github)
  - [Features](#features)
  - [TODO](#todo)
  - [Known Issues](#known-issues)
  - [License](#license)
  - [Feedback](#feedback)

#

### 🔧 Technologies & Tools

</br>

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/framework-flask-informational?style=flat-square&logo=flask&logoColor=white&color=5194f0&bgcolor=110d17)
##
#

## Operating System(Tested)
</br>
    
[![Lufi](https://svgshare.com/i/ZjA.svg)](https://svgshare.com/i/ZjA.svg)

![Linux](https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

![Debian](https://img.shields.io/badge/debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)

![Kali](https://img.shields.io/badge/kali-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)

![Ubuntu](https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</br>

> Only tested on Ubuntu/Debian Linux...

> 🚨 This script **Un-Officially** supports Windows and Mac OS.

##

#
## 📚 Requirements
> - Python 3.9+
> - Flask

##
#

## Installation

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
#

### 🗿 Pypi
> ProxyNinja-ng is also available as [python3](https://www.python.org/) module on [Pypi](https://pypi.org/).

- Pypi package [ProxyNinja-ng](https://pypi.org/project/proxy-ninja-ng/)

[![PyPI version](https://badge.fury.io/py/proxy-ninja-ng.svg)](https://badge.fury.io/py/proxy-ninja-ng)

- Info 

[![Downloads](https://pepy.tech/badge/proxy-ninja-ng)](https://pepy.tech/project/proxy-ninja-ng)
[![Downloads](https://pepy.tech/badge/proxy-ninja-ng/month)](https://pepy.tech/project/proxy-ninja-ng/month)
[![Downloads](https://pepy.tech/badge/proxy-ninja-ng/week)](https://pepy.tech/project/proxy-ninja-ng/week)
##

#

### ⚡️Github
</br>

[![GitHub version](https://badge.fury.io/gh/sc4rfurry%2FProxyNinja-ng.svg)](https://badge.fury.io/gh/sc4rfurry%2FProxyNinja-ng)


> See the **cli** version on [github](https://github.com/sc4rfurry/ProxyNinja-ng) for Installation and Usage.

</br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![GitHub](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github)


#

##

## Features

- ~~ChromeDriver to scrape the site.~~
- Uses python `requests` to fetch the proxies.
- save output in txt or json format.
- Implemented ProxyChecker. (Only for HTTP/HTTPS proxies for now)
- User Friendly. :D

## ToDo
- ~~Proxy Checker backend implementation~~ (Implemented Partially).
- Optimize the workflow
- Application Optimization
- More bugs to fix
- Socket5 support

## Known Issues

- ~~Checker tab's backend is not implemented yet.~~
- ProxyChecker is not Implemented for SOCKS proxies.

#

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch

