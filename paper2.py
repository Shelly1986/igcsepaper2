Days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
Readings = [[0]*24 for i in range(7)]
AverageTemp = []
sum_temperatures = 0
sum_average_temperatures = 0

for days in range(0,1):
    sum_temperatures = 0
    for temp in range(0,4):
        temperature = int(input("Please enter the temperature"))
        while temperature <-20 or temperature>50:
            temperature = int(input("Invalid. Enter within the range"))
        Readings[days][temp] = temperature
        sum_temperatures = sum_temperatures + temperature
    average_temperature_day = sum_temperatures/24
    print("The average temperature in celcius for ",Days[days], "is: ",average_temperature_day)
    AverageTemp.append(average_temperature_day)
    print("The average temperature in Fahrenheit for ",Days[days],"is: ", (average_temperature_day*9/5)+32)

for temperatures in range(len(AverageTemp)):
    sum_average_temperatures = sum_average_temperatures + AverageTemp[temperatures]

average_temperature_whole_week = sum_average_temperatures/7
print("Average temp for the whole week in Celcius is: ", average_temperature_whole_week)
print("Average temp for the whole week in fahrenheit is: ", (average_temperature_whole_week*9/5)+32)

    
            
        
