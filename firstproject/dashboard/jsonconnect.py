import json
import mysql.connector

json_data= open('data.json').read()
json_obj= json.loads(json_data) #convert strong into object

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pfe"
)
cursor = conn.cursor()

for item in json_obj:
    category= item.get("category") 
    objectif1= item.get("objectif1")
    objectif2= item.get("objectif2")
    objectif3= item.get("objectif3")
    objectif4= item.get("objectif4")
    objectif5= item.get("objectif5")
    objectif6= item.get("objectif6")
    objectif7= item.get("objectif7")
    objectif8= item.get("objectif8")
    question1= item.get("question1")
    question2= item.get("question2")
    question3= item.get("question3")
    question4= item.get("question4")
    question5= item.get("question5")
    question6= item.get("question6")
    question7= item.get("question7")
    question8= item.get("question8")
    question9= item.get("question9")
    question10= item.get("question10")
    question11= item.get("question11")
    question12= item.get("question12")
    question13= item.get("question13")
    question14= item.get("question14")
    question15= item.get("question15")
    question16= item.get("question16")
    question17= item.get("question17")
    question18= item.get("question18")
    question19= item.get("question19")
    question20= item.get("question20")
    question21= item.get("question21")
    question22= item.get("question22")
    question23= item.get("question23")
    question24= item.get("question24")
    cursor.execute( "INSERT INTO dashboard_categories VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (category,objectif1,objectif2,objectif3,objectif4,objectif5,objectif6,objectif7,objectif8,question1,question2,question3,question4,question5,question6,
    question7,question8,question9,question10,question11,question12,question13,question14,question15,question16,question17,question18,question19,question20,
    question21,question22,question23,question24))
conn.commit()
conn.close()

    

    
            

    
    


