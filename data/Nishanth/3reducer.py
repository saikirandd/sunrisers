s = open("01.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 99999999999

for line in s:
  data = line.strip().split('\t')
  location, mintemp = data

  if location != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = location 
    thisValue = 99999999999
  
  # apply the aggregation function
  thisValue = min(thisValue,float(mintemp))

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
