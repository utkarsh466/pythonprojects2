from flask import Flask,request,jsonify

app = Flask(__name__)

lists=[{"Contact":"9987644456","Name":"Raju","done":False,"id":1},{"Contact":"9876543222","Name":"Rahul","done":False,"id":2}]

@app.route('/add-data',methods=['POST'])

def add_task():
    if not request.json:
        return jsonify({"Status":"ERROR","Message":"Please enter/provide the data!!"},404)
    list={
        "id":lists[-1]["id"]+1,
        "Name":request.json['Name'],
        "Contact":request.json['Contact'],
        "done":False

    }
    lists.append(list)
    return jsonify({"Status":"Success","Message":"Contact added to the list successfully!!"}) 

@app.route('/get_data')

def get_data():

    return jsonify({"Data":lists})


if __name__ == "__main__":
    app.run(debug=True)    