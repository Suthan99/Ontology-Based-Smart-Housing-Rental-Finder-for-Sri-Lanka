from flask import Flask, render_template, request, redirect, url_for
from rdflib import Graph, Namespace, URIRef
from pyvis.network import Network
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ONTO_PATH = os.path.join(BASE_DIR, "..", "ontology", "HousingRentalOntology.rdf")

g = Graph()
g.parse(ONTO_PATH, format="xml")

EX = Namespace("http://www.semanticweb.org/sivasuthan/ontologies/2026/sri-lanka-housing-rental#")

def load_graph(path):
    global g
    g = Graph()
    g.parse(path, format="xml")

@app.route("/", methods=["GET","POST"])
def index():
    results=[]
    best=None

    if request.method=="POST":
        tenant=request.form.get("tenant_type","").lower()
        city=request.form.get("city","").lower()

        q=f'''
        PREFIX ex: <{EX}>
        SELECT ?prop ?city WHERE {{
            ?prop ex:locatedIn ?city .
        }}
        '''
        for r in g.query(q):
            prop_lbl=r.prop.split("#")[-1]
            city_lbl=r.city.split("#")[-1]

            score=0
            if city and city_lbl.lower()==city: score+=2
            if tenant and tenant in prop_lbl.lower(): score+=2

            if score>0 or (not tenant and not city):
                results.append({
                    "tenant": tenant.capitalize() if tenant else "Any",
                    "property": prop_lbl,
                    "city": city_lbl,
                    "score": score
                })

        results=sorted(results, key=lambda x: x["score"], reverse=True)
        if results:
            best=results[0]

    return render_template("index.html", results=results, best=best)

@app.route("/upload", methods=["POST"])
def upload():
    file=request.files["ontology"]
    path=os.path.join(BASE_DIR, file.filename)
    file.save(path)
    load_graph(path)
    return redirect(url_for("index"))

@app.route("/graph")
def graph():
    net=Network(height="750px", width="100%", directed=True)
    nodes=set()

    def color(node):
        if node in ["Colombo","Kandy","Galle"]: return "orange"
        if "Apartment" in node or "House" in node or "Room" in node: return "green"
        if "Student" in node or "Family" in node or "Professional" in node: return "blue"
        return "gray"

    for s,p,o in g:
        def lbl(x):
            return x.split("#")[-1] if isinstance(x, URIRef) else str(x)

        s_lbl=lbl(s); p_lbl=lbl(p); o_lbl=lbl(o)

        if s_lbl not in nodes:
            net.add_node(s_lbl, label=s_lbl, color=color(s_lbl))
            nodes.add(s_lbl)
        if o_lbl not in nodes:
            net.add_node(o_lbl, label=o_lbl, color=color(o_lbl))
            nodes.add(o_lbl)

        net.add_edge(s_lbl, o_lbl, label=p_lbl)

    out=os.path.join(BASE_DIR,"kg.html")
    net.write_html(out)
    return open(out,encoding="utf-8").read()

if __name__=="__main__":
    app.run(debug=True)
