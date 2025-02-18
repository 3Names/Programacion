import os
from pathlib import Path
basepath = '.'
#for entry in os.listdir(basepath):
#    if not os.path.isfile(os.path.join(basepath, entry)):
#        print(entry)


for entry in os.scandir(basepath):
    if entry.is_file():
        print(entry)
