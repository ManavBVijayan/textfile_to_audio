from gtts import gTTS
import os
text=open('demo.txt','r',encoding='utf-8').read()
language='en'
output=gTTS(text=text,lang=language,slow=False)
output.save('output2.mp3')
os.system('start output2.mp3')