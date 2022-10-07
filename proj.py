import sys
#from minizinc import Instance, Model, Solver

def get_bounds(gr, st, go):
    max = 0
    sum = 0
    j=0
    while(j < len(st)):
        path_ind = 0
        visited = {st[j]}
        paths = [[st[j]]]

        if st[j] == go[j]:
            if(max < len(paths)):
                max = len(paths)
            print("ola")
            sum = sum + len(paths)
            j+=1
            continue
            
        while path_ind < len(paths):
            curr_path = paths[path_ind]
            next_vertices = gr[curr_path[-1]]
            
            if go[j] in next_vertices:
                curr_path.append(go[j])
                print(curr_path)
                if(max < len(curr_path)):
                    max = len(curr_path)
                sum = sum + len(curr_path)
                break
    
            for next_vertice in next_vertices:
                if not next_vertice in visited:
                    new_path = curr_path[:]
                    new_path.append(next_vertice)
                    paths.append(new_path)
                    visited.add(next_vertice)
            
            path_ind += 1
        j+=1
    return [max,sum]

graphfile = open(sys.argv[1],"r")
scenariofile = open(sys.argv[2],"r")
graph = open("graph.dzn","w")
scenario = open("scenario.dzn","w")

c = graphfile.readline()
while(c[0] == '#'):
    c = graphfile.readline()

n_vertices = int(c)
g = {}
i=1
while i <= n_vertices:
    g[str(i)] = []
    i+=1
n_edges = int(graphfile.readline())

graphString = "n_vertices = " + str(n_vertices) + ";\n"
graphString = graphString + "n_edges = " + str(n_edges) + ";\n"

adj = []

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

    adj = adj + [[e1,e2]]
    graphString = graphString + "|" + e1 + "," + e2 + "\n"
    i+=1

graphString = graphString + "|];\n"

for i in range(len(adj)):
    g[str(adj[i][0])]= g[str(adj[i][0])] + [adj[i][1]]
    g[str(adj[i][1])]= g[str(adj[i][1])] + [adj[i][0]]

c = scenariofile.readline()
while(c[0] == '#'):
    c = scenariofile.readline()

n_agents = int(c)

scenarioString = "n_agents = " + str(n_agents) + ";\n"

start = []

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
    start = start + [p2]

scenarioString = scenarioString + "];\n"

scenariofile.readline()
goal = []
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
    goal = goal + [g2]

scenarioString = scenarioString + "];"

bounds = get_bounds(g,start,goal)
if(n_vertices - n_agents <= 2):
    bounds[1] = bounds[1]*2
print(bounds)
graphString = graphString + "lower_bound = " + str(bounds[0]) + ";\n"
graphString = graphString + "upper_bound = " + str(bounds[1]) + ";\n"

graph.write(graphString)
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