# A friend of mine recently introduced me to " The Game of Life " and how programmers around the world have written codes in various languages for its implementation. I too decided to write my own version of the code using Python and have posted as a video its graphical output. Hope I managed to spark your interest and , like me , you too find the simulation extremely captivating and weirdly mesmerizing.

# Brief introduction and explanation :

# " The Game of Life " is a Cellular-automaton , Zero-Player game developed by the late British Mathematician John Horton Conway in 1970.

# This never-ending game is played on a 2-Dimensional orthogonal grid of cells , each of them being in one of two possible states ... Live or Dead. The initial state of the cells , which could be either a random distribution or a human created pattern , constitutes the seed of the game and no further inputs are required then on.

# The game is then started , and with each tick of time , every cell on the grid starts evolving by interacting with eight of its neighbours i.e. the cells that are Horizontally , Vertically or Diagonally adjacent. This automated evolution follows rules of real life cell survival and generation transitions occur based on the simple rules as condensed below ...

# · any live cell with two or three live neighbours survives and lives on to the next generation
# · any live cell with fewer than two live neighbours dies , as if by under-population
# · any live cell with more than three live neighbours dies, as if by over-population
# · any dead cell with exactly three live neighbours becomes a live cell , as if by reproduction
# · all other dead cells stay dead

# Cell Births and Cell Deaths occur simultaneously with each new generation being a pure function of the preceding one. Most initial patterns eventually burn out , producing either stable figures or even patterns that oscillate forever between two or more states. Many also produce patterns that travel indefinitely , constantly moving away from their previous location.
