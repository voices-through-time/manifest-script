import os
import csv
from PIL import Image

# Only edit the things in the VARIABLES box - leave everything else UNLESS you want to run the resize method

##################### VARIABLES #############################
path = './records/A_FH_A_03_005_006/' # change this path to where the digitised documents are
volume = "006" # the name of the volume 
title = "A_FH_A_03_005_006" # the title of the records
date_range = "June 1764-May 1767" # The date range for the records
csv_path = "records/subcoms_006.csv" # path for the manifest to end up
##################### VARIABLES END #############################





# this is a method to resize the images - don't edit any of this
def resize():
	for item in dirs:
		# print(path+item)
		if os.path.isfile(path+item):
			try:
				im = Image.open(path+item)
				print('proccessing image')
				f, e = os.path.splitext(path+item)
				im.thumbnail((1500,2200))
				# import code; code.interact(local=dict(globals(), **locals()))
				im.save(f + '.jpg', 'JPEG', quality=90)
			except: 
				print("not an image")
#####    end of image resizing method #####






######## The code that actually runs starts below this line ######

dirs = os.listdir( path ) # this grabs where you are

# TO RUN THE RESIZE METHOD - remove the hashtag on the line below if the images need resizing!
resize()


## Then, we write the manifest! (don't edit anything here)
with open(csv_path, 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(["subject number","internal_id","title","group_id","volume","date range","source","owner","filename"])
		for path, dirs, files in os.walk(path):
				for filename in files:
						# import code; code.interact(local=dict(globals(), **locals()))
						group = filename[18:25]
						filewriter.writerow([os.path.splitext(filename)[0], #subject number
                           			 os.path.splitext(filename)[0], #internal id
                                 title, #title
                                 title + "_" + group ,#group id
                                 volume,#volume
                                 date_range,#daterange
                                 "London_Metropolitan_Archives",#source
                                 "Coram_Archive",#owner
                                 filename]) #filename

print('Well done - created manifest!')