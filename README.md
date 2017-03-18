# Password Strength Calculator

Calculate an evaluation of the entered password from 1 to 10.

1 - very weak password

10 - strong and good password

Script check symbols in a password against top used passwords and some bad patterns like phone number, date, and car number.
Every flaw of the password reduces the score.

# How to use

1. Download a list of top-used passwords of your choice from [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords) 
2. Rename the list to `top.txt` and place it in same directory as `password_strength.py`
3. Run `python password_strength.py`

# Example of use

```bash
$ python password_strength.py
-
Please enter your password: t3XKczXFIOrqHRr_
Your password is 10/10
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
