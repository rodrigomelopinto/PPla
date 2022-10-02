import sys
#from minizinc import Instance, Model, Solver

graphfile = open(sys.argv[1],"r")
scenariofile = open(sys.argv[2],"r")
graph = open("graph.dzn","w")
scenario = open("scenario.dzn","w")

n_vertices = int(graphfile.readline())
n_edges = int(graphfile.readline())

graphString = "n_vertices = " + str(n_vertices) + ";\n"
graphString = graphString + "n_edges = " + str(n_edges) + ";\n"

i=0
graphString = graphString + "edges = ["
while(i < n_edges):
    s_edge = graphfile.readline()
    j=0
    e1 = ""
    while(s_edge[j] != ' '):
        e1 = e1 + s_edge[j]
        j += 1
    j+=1
    e2=""
    while(s_edge[j] != '\n'):
        e2 = e2 + s_edge[j]
        j += 1

    graphString = graphString + "|" + e1 + "," + e2 + "\n"
    i+=1

graphString = graphString + "|];"
graph.write(graphString)

n_agents = int(scenariofile.readline())

scenarioString = "n_agents = " + str(n_agents) + ";\n"

scenariofile.readline()
i=0
scenarioString = scenarioString + "start = ["
while(i < n_agents):
    s_pos = scenariofile.readline()
    j=0
    while(s_pos[j] != ' '):
        j += 1
    j+=1
    p2=""
    while(s_pos[j] != '\n'):
        p2 = p2 + s_pos[j]
        j += 1
    if(i != n_agents - 1):
        scenarioString = scenarioString + p2 + ","
    else:
        scenarioString = scenarioString + p2
    i+=1

scenarioString = scenarioString + "];\n"

scenariofile.readline()
i = 0
scenarioString = scenarioString + "goal = ["
while(i < n_agents):
    s_goal = scenariofile.readline()
    j=0
    while(s_goal[j] != ' '):
        j += 1
    j+=1
    g2=""
    while(s_goal[j] != '\n'):
        g2 = g2 + s_goal[j]
        j += 1
    if(i != n_agents - 1):
        scenarioString = scenarioString + g2 + ","
    else:
        scenarioString = scenarioString + g2
    i+=1

scenarioString = scenarioString + "];"

scenario.write(scenarioString)

graphfile.close()
scenariofile.close()
graph.close()
scenario.close()
'''
# Load n-Queens model from file
mapf = Model("./Projeto.mzn")
# Find the MiniZinc solver configuration for Gecode
gecode = Solver.lookup("gecode")
# Create an Instance of the n-Queens model for Gecode
instance = Instance(gecode, mapf)

result = instance.solve()
# Output the array q
print(result["q"])'''