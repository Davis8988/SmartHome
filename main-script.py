from gtts import gTTS
import os
import subprocess
import hashlib

def text_to_speech(text, volume,language='en'):
    try:
        # This function needs this import lines : from gtts import gTTS and import hashlib
        hash_object = hashlib.md5(text.encode()).hexdigest()
        out_file = "/data/text_to_speech/{}.mp3".format(hash_object)
        if not os.path.isfile(out_file):
            myobj = gTTS(text=text, lang=language, slow=False)
            myobj.save(out_file)
        subprocess.Popen(["mpg123", out_file, "-g {}".format(volume)])
    except Exception as e:
        print("Error converting txt to speech: {}".format(e))


print("Hello david")
text_to_speech("David is a devops",100)

while(True):
	continue