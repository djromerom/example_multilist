from flask import Flask, render_template
from files import Files
from doublelinklist import DoubleLinkedList
from country import Country
from department import Department
from city import City
app=Flask(__name__)

f = Files()
multilist = f.read_divipola("DIVIPOLA.csv")
multilist.print_multilist()
@app.route('/')
def root():

   markers=[
   {
   'lat':10.919033,

   'lon':-74.870385,
   'popup':'GALAPA'
    }
   ]
   
   markers = f.get_markers(multilist)
  
   return render_template(
        'index.html',
        markers=markers
    )
   
   
if __name__ == '__main__':
    paises = DoubleLinkedList()
    colombia = Country(1, "Colombia")
    peru = Country(2, "Peru")
    paises.append(colombia)
    paises.append(peru)

    # Crear sublistas
    cund = Department(1, "Cundinamarca")
    bogota = City(1, "Bogota")

    dep_list = paises.add_child(colombia, cund)
    dep_list.add_child(cund, bogota)

    paises.print_multilist()

    
    
    #f.read_file("DIVIPOLA.csv")
    app.run(host="localhost", port=8081, debug=True)