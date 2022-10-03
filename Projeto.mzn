include "alldifferent.mzn";
include "graph.dzn";
include "scenario.dzn";

int: n_agents;
int: n_edges;
int: n_vertices;
int: makespan = 9;

set of int: AgentsRange = 1..n_agents;
set of int: MakespanRange = 1..makespan;
set of int: EdgesRange = 1..n_edges;

array[1..n_edges,1..2] of int: edges;

%array[0..n_vertices-1] of var 0..n_vertices-1: v;

array[1..n_agents] of int: start;
array[1..n_agents] of int: goal;

array[1..makespan,1..n_agents] of var 1..n_vertices: pos;

constraint pos[1,..] == start;
constraint pos[makespan,..] == goal;

%constraint
  %exists(i in MakespanRange) (
   % pos[i,..] == goal
  %);

%constraint forall(i in MakespanRange)(
%                                    alldifferent([pos[i,j]| j in AgentsRange]));

constraint forall(i in MakespanRange)(alldifferent([pos[i,j]| j in AgentsRange]) /\
              forall(j in AgentsRange)(if i != 1 then exists(e in EdgesRange)(edges[e,..] == [pos[i,j],pos[i-1,j]] \/ edges[e,..] ==       [pos[i-1,j],pos[i,j]]) \/ pos[i,j] == pos[i-1,j] endif /\
if i != 1 /\ pos[i,j] != pos[i-1,j] then not(exists(p in [pos[i-1,z]|z in AgentsRange])(pos[i,j] == p)) endif));
              
%constraint forall(i in MakespanRange)(
              %forall(j in AgentsRange)(if i != 1 /\ pos[i,j] != pos[i-1,j] then not(exists(p in [pos[i-1,z]|z in AgentsRange])(pos[i,j] == p)) endif));
              

solve satisfy;




