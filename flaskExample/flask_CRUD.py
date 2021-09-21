from flask import Flask, jsonify, request, make_response
# import json

app = Flask(__name__)

income = [
    {"desc": "salary", "amt": 5000}
]


@app.route("/incomes")
def get_income():
    return jsonify(income)


@app.route("/incomes", methods=['POST'])
def add_income():
    income.append(request.get_json())
    return "Created", 201

#####################################


stock = {
    "fruit": {
        "apple": 100,
        "banana": 45,
        "cherry": 240
    }
}


@app.route("/stock")
def get_stock():
    return make_response(jsonify(stock), 200)


@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    return make_response(jsonify({"error": f"No such {collection}"}), 484)


@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    if collection in stock:
        if member in stock[collection]:
            res = make_response(jsonify({member: stock[collection][member]}), 200)
            return res
        res = make_response(jsonify({"error": f"No such {member}"}), 404)
        return res
    return make_response(jsonify({"error": f"No Such {collection}"}), 404)


@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        original = stock[collection]
        for key, val in req.items():
            if key in original:
                original[key] = val
            else:
                original[key] = val
        # stock[collection] = req  /this will remove old value/
        res = make_response(jsonify({"msg": "collection updated.."}), 200)
        return res
    stock[collection] = req
    res = make_response({"msg": "collection created.."}, 201)
    return res


@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "Deleted..."}), 284)
        return res
    return make_response(jsonify({"Error": "collection not found"}), 404)


@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_member(collection, member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            return make_response(jsonify({"msg": "Deleted member..."}), 200)
        return make_response(jsonify({"Error": "No such member"}), 404)
    return make_response(jsonify({"Error": "Collection not found"}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
