# Flask-AlexaAPI
Alexa Web Application using Natural Language Processing.
# Web Application that acts like Alexa and responds to the user questions(Only few of them is used in the code below not for all the random questions).


1. Open Any Python IDE (I have used Visual Code because its fast compared to others IDE).
2. Create new python project(environment variable is mandatory).
3. Install all the below libraries using the Terminal.
     1. pip install SpeechReconition
     2. pip install pyttsx3
     3. pip install pywhatkit
     4. pip install datetime
     5. pip install wikipedia
     6. pip install pyjokes
     7. pip install flask
     8. pip install pyaudio
4. Get create templates folder and a html file inside template.
5. Take the Python file code(main.py) and the HTML file code(alexa.html) from this repository.
6. Run main.py file.
7. There are two steps to run the code,
     1. Click on run button in the IDE or
     2. Type --> python pythonfilename(main.py) in the terminal.
8. Open Web browser and type 127.0.0.1:5000 in the url bar.
9. Click on the Microphone button and start speaking(Use headphone).
     1. Before asking any question or telling some answer mention 'ALEXA' only then the BOT can         recognize.
     2. Click on Microphone for each use-case.
     3. If Bot finds 'Play a song' in the sentence user tell it opens you tube and plays a               random song automatically.
     4. If Bot finds 'Whatsapp' in the sentence user tell it opens Whatsapp and sends message to         the number you mention.
     5. If Bot finds 'search' in the sentence user tell it opens webpage with the topic you             mention.
     6. If Bot finds 'open web' in the sentence user tell it opens web whatsapp.
     7. If Bot finds 'mail or email' in the sentence user tell it automatically sends                   email(open main.py and check how to implement mail, I have commented since it requires           senders mail and password --> line number 113 to 131).
     8. If Bot finds 'Play' in the sentence user tell it opens you tube and plays a                     the mentioned song automatically.
     9. If Bot finds 'time' in the sentence user tell it tells the current time.
     10. If Bot finds 'who is' in the sentence user tell it tells about the person or thing that         you mention.
     11. If Bot finds 'joke' in the sentence user tell it tells a random joke.
     12. If Bot finds 'weather' in the sentence user tell it tells the weather in celcius at the          city you mention.
     13. If Bot finds 'stop' in the sentence user tell it tells good bye.
     14. If the user click on Microphone and stay quiet it shows unbounderror since the command          that is returned in line number 82 is None. In this case reload the page.
     15. If the bot hears only Alexa it tells 'Sorry, I could not hear you properly'.In this              case repeat theh sentence.
