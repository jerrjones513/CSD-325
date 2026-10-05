import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temps, and low temps from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)
#- Menu/Insructions
while True:
    print("""Sitka Weather Data Menu
    Enter 'highs' to see the high temperatures. 
    Enter 'lows' to see the low temperatures.
    Enter 'exit' to quit the program.
    """)

    choice = input("What temps would you like to view? (or 'exit'): ").lower()
    if choice == 'exit':
        print("Thank you for using the Sitka Weather Data Program. Goodbye!")
        break
    if choice == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
    elif choice == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
    else:
        print("Invalid option. Please enter 'highs', 'lows', or 'exit': ")
        continue

    # Format plot.
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()