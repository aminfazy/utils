# Created aminfazy
# Renames the files in a directory to specific form
# so that is can be sorted or accessed in order

import os
import re

files_dir = "/home/fazy/Desktop/Temp_data/iitp_dataset/new_vids_17_5_19/final_vids" 
list_dir = os.listdir(files_dir)
#ff = list_dir[-1]
#ft = list_dir[-1]
#n = int(ff[3:-4])

### Use the following loop to check the form of remane output
# before running the actual rename loop 

# NOTE:  uncomment loop with os.remane to rename the files 
for file in list_dir:
	n = int(file[3:-4])
	#print(n)
	nn = "vid_" + str("%05d" %(n)) + ".mp4"
	print(nn)


# RENAME

for file in list_dir:
        src = os.path.join(files_dir, file)
	n = int(file[3:-4])
        #print(n)
        dest = os.path.join(files_dir, "vid_" + str("%05d" %(n)) + ".mp4")
        os.rename(src,dest)

# check renamed files
list2 = sorted(os.listdir(files_dir))
for f in list2:
	print(f)
