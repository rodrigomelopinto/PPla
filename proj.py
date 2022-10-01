import sys

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
    graphString = graphString + "|" + s_edge[0] + "," + s_edge[2] + "\n"
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
    scenarioString = scenarioString + "|" + s_pos[0] + "," + s_pos[2] + "\n"
    i+=1

scenarioString = scenarioString + "|];\n"

scenariofile.readline()
i = 0
scenarioString = scenarioString + "goal = ["
while(i < n_agents):
    s_goal = scenariofile.readline()
    scenarioString = scenarioString + "|" + s_goal[0] + "," + s_goal[2] + "\n"
    i+=1

scenarioString = scenarioString + "|];"

scenario.write(scenarioString)

graphfile.close()
scenariofile.close()
graph.close()
scenario.close()