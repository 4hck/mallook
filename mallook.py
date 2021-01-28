from matplotlib import pyplot as plt
import numpy as np
import datetime
import pickle
import os

#Make a list of possible sizes if not yet in the project folder
if (not os.path.exists("./sizes.pkl")):
    sizes = []
    for i in range(1,1_000_000):
        size = (i**2)*3
        sizes.append(size)
    with open("sizes.pkl","wb") as f:
        pickle.dump(sizes,f)

#Load the list of possible square image sizes for files up to 3TB, for passing into findNearestUnder
with open("sizes.pkl","rb") as f:
    size_list = pickle.load(f)

#Select the nearest list length that satisfies dimensions for a square image [W,H,3] without exceeding
def findNearestUnder(size,size_list):
    for i in range(len(size_list)): 
        if (size>size_list[i]):
            continue
        return (size_list[i-1],i)

#Loop through the categories (benign and malicious), create .png files from them, and save into data/output/ categories
def exeToImg(input_folder='data/input',output_folder='data/output',interpolation='nearest',dpi=300,save_objects=False):
    #iterate through folders in the provided input_folder; make output folders for images (by interpolation and dpi),
    #make output folder for pkl (matplotlib figure object)
    for folder in os.listdir(input_folder):
        input_path = os.path.join(input_folder,folder)
        output_path = os.path.join(output_folder+'/'+folder,interpolation+'_'+str(dpi))
        output_path_pkl = os.path.join(output_folder+'/'+folder,'pkl')
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if not os.path.exists(output_path_pkl):
            os.makedirs(output_path_pkl)

        for filename in os.listdir(input_path):
            print("Converting {} to tensor...".format(filename))
            with open(os.path.join(input_path,filename),'rb') as f:
                byte_array = np.fromfile(f, dtype=np.uint8)
                size = findNearestUnder(byte_array.size,size_list)
                pic = np.reshape(byte_array[:size[0]],(size[1],size[1],3))

                #Append characteristics to a log file called data.csv
                with open(os.path.join(output_folder,'data.csv'),'a') as f:
                    f.write("\n{},{},{},{},{},{},{},{}".format(filename,datetime.datetime.now(),interpolation,\
                        dpi,byte_array.size,size[0],byte_array.size-size[0],(byte_array.size-size[0])/byte_array.size))

            print("Drawing as an image...")
            fig = plt.imshow(pic, interpolation=interpolation)

            print("Saving image to {}".format(output_path))
            plt.savefig(os.path.join(output_path,\
                os.path.splitext(filename)[0]+ '_' + interpolation +\
                '_' + str(dpi) + '_' + '.png'), bbox_inches='tight',dpi=dpi)

            if (save_objects==True):
                print("Saving figure object...")
                with open(os.path.join(output_path_pkl,os.path.splitext(filename)[0] + '.pkl'),"wb") as fp:
                    pickle.dump(fig,fp,protocol=4)

            print("Done with this file.")
            plt.clf()

#Set interpolation, dpi, input location, and output location
interps = ['nearest','lanczos']
dpis = [120,300,600,1200]

#Loop through the options chosen above to create image files
for interp in interps:
    for dpi in dpis:
        exeToImg(interpolation=interp,dpi=dpi)

print("Done with all files.")