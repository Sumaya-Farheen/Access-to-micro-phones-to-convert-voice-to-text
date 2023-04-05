# Voice to Text Converter using Microphones
# Reference link: https://www.youtube.com/watch?v=GluSLXFGfJ8

import speech_recognition as sr

def main():   #main method
    # Initialize the recognizer
    r = sr.Recognizer()
    # Source we are going to use in this code is Microphones
    with sr.Microphone() as source:
    
        r.adjust_for_ambient_noise   #To adjust the ambient noise with the r as Recognizer
        print('Yes, say something!')

        audio= r.listen(source)   # To listen to the source
        print('Yes, say something!')
        # we are going to use the recognizer to convert audio into text
        try:        # When ever we use audio we have to use the key word "except" or else it wil throw error because "try:" is a boolean vaule. so if "try" is true then "except Exception as e" is false
            print('Yes, say something!')
            print('You have said: \n' + r.recognize_google(audio))

        except Exception as e:   # argument 
            
            print("Oops :( \n Unable to hear you! \n Please try again! " +str(e))

#main method
if __name__=="__main__":
    main()
