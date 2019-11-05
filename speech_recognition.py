import speech_recognition as sr                         
                                                        
r = sr.Recongnizer()                                    
                                                        
with sr.Microphone() as source:                         
    print ("Speak Anything")                            
    audio = r.listen(source)                            
                                                        
                                                        
    try:                                                
        text = r.recongnize_google(audio)               
        print ('You said: {}'.format(text))             
    except:                                             
        print ('Sorry Could Not understand your voice') 
			
			
	try:                                                
		text = r.recognize_google(audio)
        print ('You said: {}'.format(text))             
  except:                                             
        print ('Sorry Could Not understand your voice') 
