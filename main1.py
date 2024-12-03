from flask import Flask, json, jsonify, request

app = Flask(__name__)

dic = [
    {'id': '1', 'name': 'abc'},
    {'id': '2', 'name': 'xyz'},
    {'id': '3', 'name': 'mno'}
]

@app.route('/', methods=["GET"])
def home():
    return jsonify(dic)

@app.route('/add',methods=["POST"])
def adding():
    nextId=int(dic[-1]['id']) +1
    data=request.get_json()
    name=data['name']

    if name is None:
        return jsonify({ 'error': 'Invalid name'}), 404
    dic.append({'id' : str(nextId), 'name':name})
    return jsonify({'id' : str(nextId), 'name':name}), 200

@app.route('/edit/<int:id>', methods=["PUT"])
def update(id):
    data=request.get_json()
    
    for item in dic:           
        if int(item['id']) == id:
            item['name']=data['name']            
            return jsonify(item), 200
    else:
        return jsonify({ 'error': 'Invalid id'}), 404

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    for item in dic:        
        if int(item['id'])==id:       
            dic.remove(item)
            return jsonify({'deleted': 'success'}), 200
    else:
        return jsonify({ 'error': 'Invalid id'}), 404

@app.route('/<int:id>',methods=['GET'])
def get_employee(id):
    for item in dic:
        if int(item['id'])==id :
            return jsonify(item), 200
    else:
        return jsonify({ 'error': 'id not found'}), 404


if __name__ == '__main__':
    print("debugging")
    app.run(debug=True,port=5000)
