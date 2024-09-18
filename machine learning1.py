import csv
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Function to read form csv file
def read_csv(path):
    with open(path) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        return data

input_data = read_csv("Data\LCA_inputdata.csv")[1:] # Reading csv file and leaving out the headings

# Creating lists for training data of purity and lifetime
training_purity = [float(row[0]) for row in input_data]
training_lifetime = [float(row[1]) for row in input_data]

plt.scatter(training_purity, training_lifetime)

# Results stores the slope, intercept, r score and standard errors of the regression model
results = stats.linregress(training_purity, training_lifetime)

# The model function takes in a purity percent and returns the predicted lifetime
def model(purity_score):
    return results.slope * purity_score + results.intercept

print(results.rvalue)

# Creating and plotting the regression line
line_x = np.linspace(40, 100, 1000)
line_y = list(map(model, line_x))
plt.plot(line_x, line_y)

output_path = "Data\LCA_outputdata.txt"

# overwrinting the file with new data
with open(output_path, "r+") as file:
    data = file.readlines()

    input_purity = list(map(float, data[1:]))
    output_lifetimes = list(map(model, input_purity))
    output = []
    for i in range(len(input_purity)):
        output.append(f"{input_purity[i]}      {output_lifetimes[i]}\n")
        
    file.seek(26) # Moving to the second line
    file.writelines(output)

print("Data written to LCA_outputdata.txt!")
plt.scatter(input_purity, output_lifetimes)
plt.show()
