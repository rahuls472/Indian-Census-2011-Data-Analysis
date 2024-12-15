from flask import Flask,render_template,request

from datasetworks import datasets

data = datasets()

app = Flask(__name__)




@app.route('/')
def home():

    states = data.AllStates()
    stateswisepop = data.OverallData()
    sexwise = data.SexwisePopulationVisualization().to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})
    Graph = data.overalldataGraph().to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})
    LiteracyRate = data.TotalLiteracyRate().to_html(full_html=False,include_plotlyjs='cdn',config={'scrollZoom': True})

    return render_template('index.html',Allstates=states,overalldata = stateswisepop,chart = Graph,chart2 = sexwise,Graph2 = LiteracyRate)



                                         
@app.route('/Singlestate')
def SingleStateStats():
    statename = request.args.get('state_name')  # Get the state name from the URL
    states = data.AllStates()  # Get all states
    singlestatedata, singlestategraph = data.statewise(statename)  # Get data for the specific state
    return render_template('singlestate.html', Allstates=states, single=singlestatedata, chart=singlestategraph)




@app.route('/SexWiseDistribution')
def SexWiseDistribution():
    statename = request.args.get('state_name')  # Get the state name from the URL
    states = data.AllStates()  # Get all states

    sexwisedata,sexwisedataGraph = data.sexdistribution(statename)
    return render_template('SexDist.html',Allstates=states,data = sexwisedata,Graph = sexwisedataGraph)



@app.route('/LieracyRate')
def LiteracyRate():
    statename = request.args.get('state_name')
    states = data.AllStates()  # Get all states
    LiteracyRateDate,LiteracyRateGraph = data.DistrictWiseLiteracy(statename)
    SexWiseLiteracy = data.maleFemaleLiteracyRate(statename)
    return render_template('Literacy.html',data = LiteracyRateDate,Graph = LiteracyRateGraph,Allstates=states,Graph2 = SexWiseLiteracy)

app.run(debug=True)



