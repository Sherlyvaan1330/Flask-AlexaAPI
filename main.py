from flask import Flask, render_template, redirect, request
import warnings
warnings.filterwarnings('ignore')

# Importing Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import json
import sys
import pyaudio

listener = sr.Recognizer()

import os

app = Flask("__name__")

#code to make the bot talk
def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# get weather of mentioned city in celcius
def weather(city):
    # Enter your API key here 
    api_key = "1042f3581b0a46c8f928788564408fac"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    city_name = city

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))

# Read what user speaks
def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

# The bot listens through user_commands and responds accordingly
def run_alexa():
    command = user_commands()

    #plays a random song
    if 'play a song' in command:
        song = 'Arijit Singh'
        engine_talk('Playing some music')
        pywhatkit.playonyt(song)

    # automatically opens whatsapp and sends the message
    elif 'whatsapp' in command:
        engine_talk('Please tell the phone number')
        country_code = '+91 '
        phone_number = country_code + user_commands()
        engine_talk('Please tell the message to be sent')
        message = user_commands()
        pywhatkit.sendwhatmsg_instantly(str(phone_number), message)

    # web page is automatically opened with the topic mentioned
    elif 'search' in command:
        engine_talk('Please tell the topic')
        topic = user_commands()
        pywhatkit.search(topic)

    #opens web whatsapp
    elif 'open web' in command:
        pywhatkit.open_web()

    # Auto sends mail
    # elif 'mail' or 'email':
        ## Below code is to take inputs from the user

        # To get password, turn on 2 step email verification
        # from myaccout.google.com/apppasswords get the unique 16 digit password and paste it in '<your password>'

        # sender_mail = '<your email>'
        # sender_pwd = '<your password>'
        # engine_talk('Please tell the subject')
        # subject = user_commands()
        # engine_talk('Please tell body of the mail')
        # body = user_commands()
        # engine_talk('Please tell your name')
        # name = user_commands()
        # engine_talk('Please tell receivers email')
        # receivers_mail = user_commands()
        #pywhatkit.send_mail('<your email>', '<your password>', '<subject>', '<body>', '<receivers_mail>')
        # engine_talk('Mail sent successfully')

    # Auto opens You tube and plays song mentioned
    elif 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing' + song)
        pywhatkit.playonyt(song)
    
    # Tells the current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' + time)

    # Tells short summary of the person that user mention.
    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 1)
        engine_talk(info)

    #Tells a random joke
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())

    # Tells the weather of the city mentioned by the user.
    elif 'weather' in command:
        engine_talk('Please tell the name of the city')
        city = user_commands()
        weather_api = weather(city)
        engine_talk('The temperature in' + city + 'is' + weather_api + 'degree celcius')

    elif 'stop' in command:
        engine_talk('Good bye')

    #if the Bot hears only alexa this else part is executed.
    else:
        engine_talk('Sorry, I could not hear you properly')

# Start page for the web application
@app.route('/')
def hello():
    return render_template("alexa.html")

@app.route("/home")
def home():
    return redirect('/')

#Triggered when the mic is clicked
@app.route("/",methods=['POST', 'GET'])
def submit():
    while True:
        run_alexa()
        return render_template("alexa.html")

#Starts up the Flask Server
if __name__ == "__main__":
    app.run(debug=True)
