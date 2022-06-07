# Password Evaluater 
Final semester project for University of Sunderland's Cyber Security course (CET324)

Django, a python-based web framework used to create a web app with security in mind. The two main features are the following: 
- a registration/log in system
- a way to evaluate the strength 

# Requirements and  python libraries 
Python 3.9 or below

Requests

Urlllib

Python-Decouple

# How to Run
First navigate a terminal to the root directory and execute the following command to set up a virtual environment
```
venv\Scripts\activate.bat
```
Next enter the Django project folder and execute the following command to run the server
```
python manage.py runserver
```
Note the IP address and the port and enter it in a browser. 
# Credits
Special thanks to [zxcvbn](https://github.com/dropbox/zxcvbn), a Javascript library developed by Dropbox. This library was used to evaluate the strength of the passwrod. 

And [this blog](https://www.ocpsoft.org/tutorials/regular-expressions/password-regular-expression/) which helped me get through the headache of writing regex. 

# License & Copyright

Chan Nyein Thu @ Harry 

Licensed under the [MIT License](LICENSE) 
