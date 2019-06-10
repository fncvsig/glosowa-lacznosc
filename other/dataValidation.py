# Checks if all data has the correct framerate

import os
import wave

frameRate = 8000;
clear = 1;

for subdir, dirs, files in os.walk('../data') or :
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):
            wf = wave.open(filepath, 'rb')

            if wf.getframerate() != frameRate:
                print("Incorrect frame rate in: ", filepath, "(", wf.getframerate(), "instead of", frameRate, ")")
                clear = 0;

if clear:
    print("All good!")
    
