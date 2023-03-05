import statistics as stats
import matplotlib.pyplot as plt
import csv

# Reading CSV file with Dictreader
HMC_data = []
with open ("HMC.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        HMC_data.append(row)

i=0
HMC_stdev_data = []
# Structuring while Loop to get Days 1 - 5 
while i <len(HMC_data):
    if i + 1 >= len(HMC_data) or i + 2 >= len(HMC_data) or i + 3 >= len(HMC_data) or i + 4 >= len(HMC_data):
        break
    Day_1 = float(HMC_data[i]["Closing_Price"])
    Day_2 = float(HMC_data[i+1]["Closing_Price"])
    Day_3 = float(HMC_data[i+2]["Closing_Price"])
    Day_4 = float(HMC_data[i+3]["Closing_Price"])
    Day_5 = float(HMC_data[i+4]["Closing_Price"])

    pop_stdev = stats.pstdev([Day_1,Day_2,Day_3,Day_4,Day_5])
    HMC_stdev_data.append(pop_stdev)
    i += 5
week = 0
for stdev in HMC_stdev_data:
    week += 1
    print(f"HMC Week {week} Standard Deviation is :{stdev}")
plt.plot(HMC_stdev_data)
plt.title("Stock Weekly Standard Deviation")
plt.ylabel("STD of CLOSING PRICE")
plt.savefig("HMCSTD.png")
plt.show()