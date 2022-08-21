# BattleShip

This is a simple Python project to recreate the classic game BattleShip using Object Oriented Programming Principles. 
In its current state, it is meant to be played to two players - 'first' and 'second'.

Players can place ships by calling the place_ship() method with the following parameters:
 - Player name: 'first' or 'second'
 - Length of ship: 
 - Starting Coordinate for placement ('A1' - 'J10')
 - Orientation: 'R' for horizontal placement and 'C' for vertical
 
Once placed, players can fire torpedos at the opponent by calling the fire_torpedo() method with the following parameters:
 - The player whose turn it is to fire ('first' or 'second')
 - The coordinate at which the player wishes to fire a torpedo
 
The display_grid() method can be used to display a visual ASCII board in the terminal for players to track hit's and misses on their own board.
This method takes a single parameter, the player whose board you wish to display and prints said board.

E.G Board:  (View readMe as raw file to view accurate visual output)  
    1  2  3  4  5  6  7  8  9  10  
A: [-][-][-][-][-][-][-][-][-][-]  
B: [-][-][-][-][-][-][-][-][-][-]  
C: [-][-][-][-][-][-][-][-][-][-]  
D: [-][-][-][-][-][-][-][-][-][-]  
E: [-][-][-][-][-][-][-][-][-][-]  
F: [-][-][-][-][-][-][-][-][-][-]  
G: [-][-][-][-][-][-][-][-][-][-]  
H: [-][-][-][-][-][-][-][-][-][-]  
I: [-][-][-][-][-][-][-][-][-][-]  
J: [-][-][-][-][-][-][-][-][-][-]  

'first' player places two ships:  
    1  2  3  4  5  6  7  8  9  10  
A: [X][X][X][X][-][-][-][-][-][-]  
B: [-][-][-][-][X][-][-][-][-][-]  
C: [-][-][-][-][X][-][-][-][-][-]  
D: [-][-][-][-][X][-][-][-][-][-]  
E: [-][-][-][-][X][-][-][-][-][-]  
F: [-][-][-][-][-][-][-][-][-][-]  
G: [-][-][-][-][-][-][-][-][-][-]  
H: [-][-][-][-][-][-][-][-][-][-]  
I: [-][-][-][-][-][-][-][-][-][-]  
J: [-][-][-][-][-][-][-][-][-][-]  

'second' player fires a torpedo at 'A1'  
    1  2  3  4  5  6  7  8  9  10  
A: [*][X][X][X][-][-][-][-][-][-]  
B: [-][-][-][-][X][-][-][-][-][-]  
C: [-][-][-][-][X][-][-][-][-][-]  
D: [-][-][-][-][X][-][-][-][-][-]  
E: [-][-][-][-][X][-][-][-][-][-]  
F: [-][-][-][-][-][-][-][-][-][-]  
G: [-][-][-][-][-][-][-][-][-][-]  
H: [-][-][-][-][-][-][-][-][-][-]  
I: [-][-][-][-][-][-][-][-][-][-]  
J: [-][-][-][-][-][-][-][-][-][-]  

