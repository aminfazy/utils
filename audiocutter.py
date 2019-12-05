########### created by AMINFAZY     ########
#convert audio to nummpy array and back to audio
# input is audio in wav format
# output is wav format audio
# audio can be cut using frame rate and numpy array signal array 

####   DEPENDENCIES  #######
# ffmpeg must be installed (sudo apt-get install ffmpeg)
# pydub must be installed (pip install pydub
# numpy and scipy are also required




import audioop
from os import path
from pydub import AudioSegment
from scipy.io.wavfile import read,write

# files                                                                         
src = "testaudio.mp3"  # input audio
dst = "testwav.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")



import numpy as np
a,b = read(dst)  # returns rate and numpy array of signal
print a,":",len(b)
#exit()
c=b[4983300:5780700]
print len(c)
write("cut_file.wav",a,c)
# sound=np.array(sound[1,0:50],dtype=float)
# print a,";",b 

