# Sunrisers
##   project number: 02
1. Nishanth reddy, Devi Reddy
2. Saikiran, Doddapaneni
3. Yeshwanth reddy, Anumula
## Links: - [GitHub repo](https://github.com/saikirandd/sunrisers/issues/3)
          
  - [issues link](https://github.com/saikirandd/sunrisers/issues/)
## project Introduction: 
Our project covers about wheather in major cities of Australia.
## Data source: 
 Data is of size of aboot 13.5 mb in CSV format.Data is strucutred. It has 142190 rows and 24 columns.
## Big data problems
 Question 1: For each location, find avg rainfall
  
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
