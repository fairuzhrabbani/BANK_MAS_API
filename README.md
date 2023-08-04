# API Testing - Reqres
API Testing with Python

## What will the test do?
- Create user
- Update user
- Delete user

## Tech

- [Python] - Python is used successfully in thousands of real-world business applications around the world
- [Request] - Requests is a simple, yet elegant, HTTP library.
- [Pytest] - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
- [PyCharm] - The Python IDE for Professional Developers

## Installation

Download & Install [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe) 3.11.4.
Check Python version in cmd
```sh
python --version
Python 3.11.4
```
Download & Install [PyCharm]
Install Python [Request] di cmd
```sh
pip install requests
```
Install Python [Pytest] di cmd
```sh
pip install pytest
```
Check Packages Request & Pytest in cmd has been done 
```sh
pip list
```
## Development
1. Open PyCharm
2. Create new project
3. Create New -> Python Package -> Reqres
4. Create file .py -> test_reqres_api.py
5. Import packages
6. Create function in python with start name is 'test_'
7. Open terminal in PyCharm 
8. Run scripts with report
```sh
pytest Reqres/test_reqres_api.py -v --html=report.html
```
9. Report will be generated .html

   [Python]: <https://www.python.org/>
   [Request]: <https://pypi.org/project/requests/>
   [Pytest]: <https://pypi.org/project/pytest/>
   [PyCharm]: <https://www.jetbrains.com/pycharm/>
