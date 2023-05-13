import json
def readAsList(filepath):
  fp = open(filepath,'r')    #list having each line of json as elements
  jsonList = fp.readlines()
  fp.close()
  return jsonList
def readAsListOfDict(filepath):
  fp = open(filepath,'r')    #list having dictionary of objects.
  jsonData = json.load(fp)
  fp.close()
  return jsonData
def printSetosa(jsonList):  #printing the details of only setosa.
  print("\nDetails of flowers of species setosa")
  for i in jsonList:
    if(i['species']=='setosa'):
      print(i)
def sepalAreaAndPetalArea(jsonList): #list to store species names.
  listOfSpeciesName = list()
                             #appeding the different species name to the list.
  for i in jsonList:        
    listOfSpeciesName.append(i['species'])
                             #removing duplicates to get unique speices.
  listOfSpeciesName = list(set(listOfSpeciesName))
                             #list to store sepal and petal area.
  sepalArea = list()
  petalArea = list()
                       #species sepal area and petal area
  for i in listOfSpeciesName:
    for j in jsonList:
      if(j['species']==i):
        sepalArea.append(j['sepalLength']*j['sepalWidth'])
        petalArea.append(j['petalLength']*j['petalWidth'])
    print()
    print(i.capitalize())
                                    #printing minimum and maximum areas.
    print("Maximum Sepal Area in ",i.capitalize()," is ",end="")
    print(round(max(sepalArea),2))
    print("Minimum Petal Area in ",i.capitalize()," is ",end="")
    print(round(min(petalArea),2))
    sepalArea.clear()
    petalArea.clear()
def sortTotalArea(jsonList):
  for i in jsonList:            #adding total area to the each dictionary
    petal=i['petalLength']*i['petalWidth']
    sepal=i['sepalLength']*i['sepalWidth']
    totalArea = (petal)+(sepal)   
    i.update({'totalArea':round(totalArea,2)})
                                #list sorted according to total area
  sortedList = sorted(jsonList,key=lambda i:i['totalArea'])
  print("\nList sorted on the basis of total area")
  for i in sortedList:
    print(i)
filePath = 'iris.json'          #saving the file 
jsonList = readAsList(filePath)
print("List with each line as element\n")
for line in jsonList:
  print(line)
jsonData = readAsListOfDict(filePath)
print("\nList of Dictionaries")
for i in jsonData:
  for key, values in i.items():
    print(key.capitalize()+" : ",values,end=" , ")
  print()
printSetosa(jsonData)      #function call for displaying setosa series
                            #function call for find total sepal and petal area
sepalAreaAndPetalArea(jsonData)  
                            #function to find the total area
sortTotalArea(jsonData)