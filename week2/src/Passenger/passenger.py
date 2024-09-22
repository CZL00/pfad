import datetime
import matplotlib.pyplot as plt
import csv

#When I try to reference to the chart that contain data like the example does, I failed, after I search online, that's the method that I can open the file
file_path = r'C:\Users\Administrator\Desktop\pfad\week2\src\Passenger\statistics_on_daily_passenger_traffic.csv'

with open(file_path, newline='', encoding='UTF-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    
    data = []
    for row in spamreader:
        try:
            date_str = row[0]
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
            
            inbound_passengers = int(row[4])
            outbound_passengers = int(row[5])

            data.append((date, inbound_passengers, outbound_passengers))
            print(f'{date} -- Inbound: {inbound_passengers}, Outbound: {outbound_passengers}')
        except ValueError as e:
            print(f"Error processing row: {row}. Error: {e}")

fig, ax = plt.subplots()

ax.plot([record[0] for record in data], [record[1] for record in data],label='Inbound Passengers')
ax.plot([record[0] for record in data], [record[2] for record in data],label='Outbound Passengers')

ax.legend()

plt.show()
