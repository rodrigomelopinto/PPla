include "alldifferent.mzn";
include "graph.dzn";
include "scenario.dzn";

int: n_agents;
int: n_edges;
int: n_vertices;
int: makespan = 0;

array[1..n_edges,1..2] of int: edges;

%array[0..n_vertices-1] of var 0..n_vertices-1: v;

array[1..n_agents,1..2] of int: start;
array[1..n_agents,1..2] of int: goal;

%array[1..makespan,1..n_agents,1..n_vertices] of var 0..1: pos;

%constraint alldifferent(pos);
solve satisfy;
%constraint alldifferent(v);

