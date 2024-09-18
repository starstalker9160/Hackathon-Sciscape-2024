import csv

# reading from given csv file
def read_csv():
    with open("Data\company_sustainability_scores.csv", 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

# overwriting the csv file
def write_csv(rows):
    with open("Data\company_sustainability_scores.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


data = read_csv()
input_data = {}

# defining inputs dictionary
input_data["Company Name"] = [row[0] for row in data[1:]]
input_data["Carbon Footprint"] = [row[1] for row in data[1:]]
input_data["Energy Usage"] = [row[2] for row in data[1:]]
input_data["Water Consumption"] = [row[3] for row in data[1:]]

# function to find score of a company
def score(x: int, y: int, z: int) -> float:
    return (x/1000)**(-2) + y**(5/7) - (z/10000)**2

# defining variables
companies, carbon_footprints, energy_usage, water_consumption = input_data["Company Name"], input_data["Carbon Footprint"], input_data["Energy Usage"], input_data["Water Consumption"]

# creating dictionary of {score of company -> company}
scores_and_companies = {}
for company in companies:
    scores_and_companies[score(int(carbon_footprints[int(company) - 1]), int(energy_usage[int(company) - 1]), int(water_consumption[int(company) - 1]))] = company

scores = list(scores_and_companies)

# sorting in descending order
scores.sort()
scores.reverse()
top_companies = []

for sustainability_score in scores:
    top_companies.append(scores_and_companies[sustainability_score])
print("Top 10 companies are: ")
print(top_companies[:10])

sorted_csv = []
for company in top_companies:
    sorted_csv.append([company,input_data["Carbon Footprint"][int(company) - 1],input_data["Energy Usage"][int(company) - 1],input_data["Water Consumption"][int(company) - 1]])
sorted_csv.insert(0, ["Company Name","Carbon Footprint (tons CO2e)","Energy Usage (GWh)","Water Consumption (m³)"])
write_csv(sorted_csv)
print("Sorted list overwritten at 'company_sustainability_scores.csv'")
