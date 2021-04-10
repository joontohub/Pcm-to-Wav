import wave

from os import listdir
from os.path import isfile, join
import os
filepath = os.getcwd()

files = [f for f in listdir(filepath) if isfile(join(filepath, f))]

files = [ x for x in files if x.find(".pcm") != -1]


# The parameters are prerequisite information. More specifically,
# channels, bit_depth, sampling_rate must be known to use this function.
def pcm2wav( pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000 ):

    # Check if the options are valid.
    if bit_depth % 8 != 0:
        raise ValueError("bit_depth "+str(bit_depth)+" must be a multiple of 8.")
        
    # Read the .pcm file as a binary file and store the data to pcm_data
    with open( pcm_file, 'rb') as opened_pcm_file:
        pcm_data = opened_pcm_file.read()
        
        obj2write = wave.open( wav_file, 'wb')
        obj2write.setnchannels( channels )
        obj2write.setsampwidth( bit_depth // 8 )
        obj2write.setframerate( sampling_rate )
        obj2write.writeframes( pcm_data )
        obj2write.close()


for i in range(len(files)):
    print(files[i])
#pcm2wav( 'KsponSpeech_003003.pcm', 'KsponSpeech_003003.wav', 1, 16, 16000 )