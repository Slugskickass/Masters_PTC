import numpy as np
import useful as us
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    noise  = [] #could be called noise
    signal = []
#    background_file = 'data.tif'
#    background = us.createback(background_file)
#    list_files = us.get_file_list('/Volumes/Samsung_T3/Frames tiff')
    list_files = us.get_file_list(sys.argv[1])
    count = 0
    for file_name in list_files:
        # Load in a file
        # Subtract the background from each frame in the array
        # select a region of interest
        # Calculate the std and mean
        # mean_of_data = np.mean(small) SIGNAL
        # noie_data = np.std(small)
        # Store them
        noise.append(count)
        signal.append(count * count)
        count = count + 1
    my_new_noise = np.asarray(noise)
    my_new_signal = np.asarray(signal)
    np.save('noise', my_new_noise)
    np.save('signal', my_new_signal)
    #Save them

#    data = us.loadtiffs('data.tif')
# data_corrrectd = data - background
#    small_data = data[400:500, 450:550, :]