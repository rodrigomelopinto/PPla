include "alldifferent.mzn";
include "graph.dzn";
include "scenario.dzn";

int: n_agents;
int: n_edges;
int: n_vertices;
int: makespan = 20;

set of int: AgentsRange = 1..n_agents;
set of int: MakespanRange = 1..makespan;

array[1..n_edges,1..2] of int: edges;

%array[0..n_vertices-1] of var 0..n_vertices-1: v;

array[1..n_agents,1..2] of int: start;
array[1..n_agents,1..2] of int: goal;

array[1..makespan,1..n_agents] of var 1..n_vertices: pos;


constraint forall(i in MakespanRange)(
                                    alldifferent([pos[i,j]| j in AgentsRange]));

solve satisfy;

