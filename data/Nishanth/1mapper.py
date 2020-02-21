input = open("weather.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    date, location, mintemp, maxtemp, rainfall, winddirection, windspeed, humidity, presssure, tempat9, Raintoday  = datalist
   # mintemp of each locaton
    output.write(location + "\t" + mintemp + "\n")

input.close()
output.close()