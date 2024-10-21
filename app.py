from flask import Flask, jsonify
from rdflib import Graph

app = Flask(__name__)

# Load ontology
g = Graph()
g.parse("sandwich_website/Sandwich.rdf", format="xml")

# API endpoint để lấy thông tin về sandwich
@app.route('/api/sandwiches', methods=['GET'])
def get_sandwiches():
    sandwiches = []
    query = """
    SELECT ?sandwich ?name
    WHERE {
      ?sandwich rdf:type :Sandwich .
      ?sandwich :name ?name .
    }
    """
    qres = g.query(query)
    for row in qres:
        sandwiches.append({"uri": str(row.sandwich), "name": str(row.name)})
    return jsonify(sandwiches)

if __name__ == '__main__':
    app.run(debug=True)
