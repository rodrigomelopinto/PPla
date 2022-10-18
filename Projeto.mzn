include "alldifferent.mzn";
include "graph.dzn";
include "scenario.dzn";

int: n_agents;
int: n_vertices;
int: makespan;
int: max_adj;

set of int: AgentsRange = 1..n_agents;
set of int: TimeRange = 2..makespan;
set of int: AdjRange = 1..max_adj;

array[1..n_vertices,1..max_adj] of int: adj;
array[1..n_vertices,1..n_agents] of int: dist;

array[1..n_agents] of int: start;
array[1..n_agents] of int: goal;

array[1..makespan,1..n_agents] of var 1..n_vertices: pos;

constraint pos[1,..] == start;

constraint pos[makespan,..] == goal;

constraint forall(i in TimeRange)(alldifferent([pos[i,j]| j in AgentsRange]));

constraint forall(i in TimeRange, j in AgentsRange)(pos[i,j] == pos[i-1,j] \/ exists(v in AdjRange)(adj[pos[i-1,j],v] == pos[i,j]) /\ if pos[i,j] != pos[i-1,j] then not(exists(p in [pos[i-1,z]|z in AgentsRange])(pos[i,j] == p)) endif);

constraint forall(i in TimeRange, j in AgentsRange)(dist[pos[i,j],j] <= makespan - i + 1);
  
solve satisfy;




