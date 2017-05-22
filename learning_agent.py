from numpy import loadtxt

filename = 'training.txt'

def get_training_data(path, num_weights = 6):
    # Load each line of comma-separated line of data
    data = loadtxt(path, delimiter = ',')
    
    # Load training data into lists
    x_values = data[:2, :num_weights] # Random weights
    y_values = data[:2, num_weights] # Game scores
    
    return x_values, y_values

print(get_training_data(filename))