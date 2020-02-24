# Sunrisers
##   project number: 02
1. Nishanth reddy, Devi Reddy(nishanthreddy122@gmail.com)
2. Saikiran, Doddapaneni(saikirandoddapaneni@gmail.com)
3. Yeshwanth reddy, Anumula(yeshwanthreddy76@gmail.com)
## course 
44517-02
## Links: 
- [GitHub repo](https://github.com/saikirandd/sunrisers/issues/3)
          
 - [issues link](https://github.com/saikirandd/sunrisers/issues/)
## project Introduction: 
Our project is about weather in major cities of Australia, that includes temperature, wind speed, pressure, rainfall.
## Data source: 
 
- [weather data source](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package)
 , data is of size 13.5 mb, which is in CSV format. Data is strucutred. It has 142190 rows and 11 columns. It is updated every year. Data is reliable.
 
## Commands
1. To run Mapper code: 
```
Type "python 1mapper.py" in powershell or terminal
```
1. To run Reducer code: 
```
Type "python 3reducer.py" in powershell or terminal
```
 
## Big data problems

### Sai Kiran Doddapaneni
1. Question 1: For each location, find avg rainfall
  
 Solution:
 Mapper input: 
| 12/1/2008 | Albury | 13.4 | 22.9 | 0.6 | NA | NA | W | 44 | W | WNW | 20 | 24 | 71 | 22 | 1007.7 | 1007.1 | 8 | NA | 16.9 | 21.8 | No | 0 | No |
|-----------|--------|------|------|-----|----|----|---|----|---|-----|----|----|----|----|--------|--------|---|----|------|------|----|---|----|





Mapper output:
 |location|  Rainfall|
 |---------|----------|
 |Albury |    0.6|
 
 Reducer output:
 |location |avg rainfall|
 |---------|-----|
 |Albury| 1.95|
 
 chart: bar graph.
 
 - ![AvgRain](https://github.com/saikirandd/sunrisers/blob/master/Images/avgRain.PNG)
 
  ### Mapper screenshot
 - ![mapper](https://github.com/saikirandd/sunrisers/blob/master/data/Sai%20Kiran%20Doddapaneni/mapper_console_screenshot.png)
 ### Reducer screenshot
 - ![reducer](https://github.com/saikirandd/sunrisers/blob/master/data/Sai%20Kiran%20Doddapaneni/reducer_console_screenshot.png)
 
 
### Yeshwanth Reddy Anumula 

2. Question 2: For each location, find highest recorded MaxTemp.
 
 Solution:
 Mapper input: 
| 12/1/2008 | Albury | 13.4 | 22.9 | 0.6 | NA | NA | W | 44 | W | WNW | 20 | 24 | 71 | 22 | 1007.7 | 1007.1 | 8 | NA | 16.9 | 21.8 | No | 0 | No |
|-----------|--------|------|------|-----|----|----|---|----|---|-----|----|----|----|----|--------|--------|---|----|------|------|----|---|----|



Mapper output:
 |location|  MaxTemp|
 |---------|----------|
 |Albury |    22.9|
 
 Reducer output:
 |location |highest MaxTemp|
 |---------|-----|
 |Albury| 44.8|
 
 chart : Bar graph
 
 - ![Max temp](https://github.com/saikirandd/sunrisers/blob/master/Images/Highest.JPG)
 ### Mapper screenshot
 - ![mapper](https://github.com/saikirandd/sunrisers/blob/master/data/Yeshwanth%20Reddy%20Anumula/Screenshot%20(81).png)
 ### Reducer screenshot
 - ![reducer](https://github.com/saikirandd/sunrisers/blob/master/data/Yeshwanth%20Reddy%20Anumula/Screenshot%20(82).png)
 
### Nishanth Reddy Devi Reddy
3. Question 3: For each location, find lowest recorded MinTemp
 
  Solution:
 Mapper input: 
| 12/1/2008 | Albury | 13.4 | 22.9 | 0.6 | NA | NA | W | 44 | W | WNW | 20 | 24 | 71 | 22 | 1007.7 | 1007.1 | 8 | NA | 16.9 | 21.8 | No | 0 | No |
|-----------|--------|------|------|-----|----|----|---|----|---|-----|----|----|----|----|--------|--------|---|----|------|------|----|---|----|


Mapper output:
 |location|  MinTemp|
 |---------|----------|
 |Albury |    13.4|
 
 Reducer output:
 |location |lowest MinTemp|
 |---------|-----|
 |Albury| -2.8|
  ### Mapper screenshot
 - ![mapper](https://github.com/saikirandd/sunrisers/blob/master/data/Nishanth%20Reddy%20Devi%20Reddy/mapper_screenshot.png)
 ### Reducer screenshot
 - ![reducer](https://github.com/saikirandd/sunrisers/blob/master/data/Nishanth%20Reddy%20Devi%20Reddy/reducer_screenshot.png)
 
 chart: Bargraph
 - ![LowestRecordedTemperature](https://github.com/saikirandd/sunrisers/blob/master/Images/LowestTemperatureRecorded.png)
 
 
 
