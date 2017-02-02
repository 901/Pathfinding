# Pathfinding
CS440 Assignment 1 that uses A\*, Weighted A\* and Uniform cost search to traverse a maze with different terrain properties

To run the project:
1) Clone the directory<br>
2) run <pre><code> python grid.py </pre></code>

<b> Commands to follow when the program is running </b>
<ol>
  <li>Press (g) to generate a new map</li>
  <li>Press (l) to load a map in the /gen/ folder - see command line interface to enter name of map</li>
  <li>Press (s) to save a map in the /gen/ folder - see command line internface to enter name of map</li>
  <li>Press (e) to generate new Start/Goal vertices - RED = start, BLUE = goal</li>
  <li>Press (a) to prepare A\* search - see command line interface to set your Heuristic
    <ol>
    <li>Enter 1 for Manhattan Distance</li>
    <li>Enter 2 for Euclidean Distance</li>
    <li>Enter 3 for Octile Distance</li>
    <li>Enter 4 for Chebyshev Distance</li>
    <li>Enter 5 for Straight-Diagonal Distance</li>
    <li>Enter 6 for Best (minimum of all) Distance</li>
    </ol>
  </li>
  <li>Press (u) to run Uniform-Cost Search</li>
  <li>Press (w) to prepare Weighted A\* search - see command line interface for weight and Heuristic Choices
   <ol>
      <li>Enter 1 for Manhattan Distance</li>
      <li>Enter 2 for Euclidean Distance</li>
      <li>Enter 3 for Octile Distance</li>
      <li>Enter 4 for Chebyshev Distance</li>
      <li>Enter 5 for Straight-Diagonal Distance</li>
      <li>Enter 6 for Best (minimum of all) Distance</li>
      <li>Then enter a weight >= 1</li>
   </ol>
  </li>
  <li>Press (v) to see the fringe and which nodes were visited in the search</li>
  </ol>
<br>

<b>On the map:</b>
Using your arrow keys, you can explore the map to see which cell contains which terrain. If a cell is on the fringe/visited list,<br>
You can also explore its f(n), g(n) and h(n) values on the sidebar.<br>
<i>Terrain Key</i>
<ol>
  <li>1 = unblocked regular cell</li>
  <li>2 = hard-to-traverse cell</li>
  <li>a = highway unblocked regular</li>
  <li>b = highway hard-to-traverse</li>
</ol>
*See PDF for how the map was generated*


  

  
