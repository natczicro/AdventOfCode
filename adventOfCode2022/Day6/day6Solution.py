file1=open('input', 'r')


data = file1.read().rstrip()
print(len(data))

def checkIfMarker(markerList):
  if len(markerList) == len(set(markerList)):
    return True
  else:
    return False

markerList=[]
for i in range(len(data)):
  if i > 3:
    markerList.pop(0)

    
  markerList.append(data[i])

  if checkIfMarker(markerList) and i>3:
    print(i)
    break

markerList=[]
for i in range(len(data)):
  if i > 13:
    markerList.pop(0)

    
  markerList.append(data[i])

  if checkIfMarker(markerList) and i>13:
    print(i)
    break