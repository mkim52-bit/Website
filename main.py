import urllib.request
import urllib.parse
import json
import bottle 
import sqlite3

@bottle.route("/")
def start():
  return bottle.static_file("index.html",root=".")
@bottle.route("/main.js")
def get():
  return bottle.static_file("main.js",root=".")

url = "https://opendata.maryland.gov/api/views/8kn6-62x4/rows.json?accessType=DOWNLOAD"
response = urllib.request.urlopen(url)
content = response.read().decode()
connection = sqlite3.connect("SRfile")
cursor = connection.cursor()
a = json.loads(content)
cursor.execute("CREATE TABLE IF NOT EXISTS Srates (city,rate,race,year)")

header = False
for i in a["data"]:
  if header == True:
    cursor.execute("INSERT INTO Srates VALUES(?,?,?,?)",(i[8],i[9],i[10],i[11]))
    
  header = True
@bottle.route("/makeBar")
def Bar(): # x = months
  
  b = []
  z = {}
  y = []
  x = []
  rows = cursor.execute("SELECT * FROM Srates")
  for row in rows:
    if row[0] != "State" and row[0] != "Talbot":
      
      y.append(row[0])#City
      x.append(row[1])#rate
    
     

  z["type"] = 'bar'
  z["x"]=x
  z["y"]=y
  z["orientation"] = "h"
  
  b.append(z)
  json.dumps(b)
  
  
  return json.dumps(b) 

@bottle.post("/makeBar2")
def Bar2(): # x = months
  content = bottle.request.body.read()
    #print(content)
  content = content.decode()
    #print(content)
  content = json.loads(content)
  if content["Bar"] == 2:
    b = []
    z = {}
    y = []
    x = []
    rows = cursor.execute("SELECT * FROM Srates")
    for row in rows:
      x.append(row[0])#Rate
      y.append(row[1])#City

    z["type"] = 'bar'
    z["x"]=x
    z["y"]=y
    z["orientation"] = "h"
  
    b.append(z)
    json.dumps(b)
  
  
  return json.dumps(b) 

@bottle.post("/makeBarR")
def Bar3(): # x = months
  content = bottle.request.body.read()
    #print(content)
  content = content.decode()
    #print(content)
  content = json.loads(content)
  if content["Bar"] == 2:
    b = []
    z = {}
    y = []
    x = []
    rows = cursor.execute("SELECT * FROM Srates")
    for row in rows:
      y.append(row[0])#Rate
      x.append(row[1])#City

    z["type"] = 'bar'
    z["x"]=x
    z["y"]=y
    z["orientation"] = "h"
  
    b.append(z)
    json.dumps(b)
  
  
  return json.dumps(b) 

@bottle.route("/makePie")
def Pie():
  b = []
  z = {}
  y = [] 
  x = []
  rows = cursor.execute("SELECT * FROM Srates")
  for row in rows:
    y.append(row[1])#Rate
    x.append(row[3])#Years
  z["values"] = y
  z["labels"] = x
  z["type"] = "pie"
  b.append(z)
  return json.dumps(b)

@bottle.post("/makePie2")
def Pie2():
  content = bottle.request.body.read()
    #print(content)
  content = content.decode()
    #print(content)
  content = json.loads(content)
  if content["Key"] == "value":
    b = []
    z = {}
    y = [] 
    x = []
    rows = cursor.execute("SELECT * FROM Srates")
    for row in rows:
      y.append(row[1])#Rate
      x.append(row[2])#Race
    z["values"] = y
    z["labels"] = x
    z["type"] = "pie"
    b.append(z)
    return json.dumps(b)

@bottle.post("/makePie3")
def Pie3():
  content = bottle.request.body.read()
    #print(content)
  content = content.decode()
    #print(content)
  content = json.loads(content)
  if content["Key"] == "value":
    b = []
    z = {}
    y = [] 
    x = []
    rows = cursor.execute("SELECT * FROM Srates")
    for row in rows:
      y.append(row[1])#Rate
      x.append(row[3])#Race
    z["values"] = y
    z["labels"] = x
    z["type"] = "pie"
    b.append(z)
    return json.dumps(b)




connection.commit()

bottle.run(host="0.0.0.0",port=8080,debug=True)




