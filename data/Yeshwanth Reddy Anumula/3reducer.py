s = open("01.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  location, maxtemp = data

  if location != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = location 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue = max(thisValue,float(maxtemp))

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
