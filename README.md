# Astar
How to use: To run just open the .py file and run it. Then enter the cost you want to test, then the environment you want to see it on.From there you can see it display the path, it will then ask you if you want to stop it, to do so just type stop. Otherwise, any other input will make it ask you to enter a new cost and environment number. The application will show as unresponsive, but it will display change when you enter a new cost or environment after the stop check. It will continue to loop until you choose to stop it. For the first environment the cost values ranged from 723 - 1404. Before 723 no path is found, after 1404 the path stays the same. For the second environment the cost values ranged from 794 - 1175. Before 794 no path is found, after 1175 the path stays the same. 

Description: A program that uses a modified version of the A* algorithm.
Instead of the f-value used in A*, this algorithm uses its own-defined u-value.
f-value: (line distance of the current node to the goal Node) + tentative g score
u-value: (cost - tentative g score) / (line distance of the current node to the goal Node)
There is a constraint added in modified A* algorithm that decides which nodes should not be expanded as it has a higher cost than budget C.
