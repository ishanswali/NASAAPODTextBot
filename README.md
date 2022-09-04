# NASA Astronomy Picture of the Day Text Bot

## Description
Hello there. This project is an automated delivery of an astronomy picture and description from NASA's Astronomy Picture of the Day (APOD) API. It's a small side project under development born from my love for Astronomy and Automation.

This system is still under development, but for now I'm deploying it on a small scale locally. It combines multiple different components: the NASA API, my own Python automation, and an [SMS/MMS Script](https://youtu.be/4-ysecoraKo) from [Alfredo Sequeida](https://github.com/AlfredoSequeida/). Huge thanks to him for his help on this project.

Keep an eye out for a website that allows sign up for APOD texts featuring my newly minted full stack developer skills 😎. 

## Installation

### To run locally
In main.py, enter your number, provider, and email to each respective "<    >"
For the sender_credentials, create a Gmail account with an [app password](https://support.google.com/mail/answer/185833?hl=en). 

I will have the sign up feature set up soon, so it won't be necessary to run locally. Keep an eye out :)

```
$ git clone git@github.com:ishanswali/NASAAPODTextBot.git
$ pip install -r requirements.txt
$ cd NASAAPODTextBot/
$ python main.py
```