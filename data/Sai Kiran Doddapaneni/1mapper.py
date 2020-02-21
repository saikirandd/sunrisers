# taking input from weather.txt
input = open("weather.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    date, location, mintemp, maxtemp, rainfall, winddirection, windspeed, humidity, presssure, tempat9, Raintoday  = datalist
    # mapping location and rainfall in those locations   
    output.write(location + "\t" + rainfall+ "\n")

input.close()
output.close()