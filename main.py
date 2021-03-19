import numpy as np
import useful as us
import matplotlib.pyplot as plt
import sys



if __name__ == '__main__':
    noise = []
    signal = []
    background = us.createback(sys.argv[2])
    list_files = us.get_file_list(sys.argv[1])
    for file_name in list_files:
        # Load in a file
        data = us.loadtiffs(file_name)

        # Subtract the background from each frame in the array
        new_data = np.zeros(np.shape(data))
        for I in range(np.shape(data)[2]):
            new_data[:, :, I] = data[:, :, I] - background

        # select a region of interest
        selected_data = new_data[100:200, 100:200, :]

        # Calculate the std and mean
        signal.append(np.mean(selected_data))
        noise.append(np.std(selected_data))

    np.save('signal', np.asarray(signal))
    np.save('noise', np.asarray(noise))

