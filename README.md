# Snake

Uses a genetic algorithm with a neural network to train the computer to play snake.

## Game Objective

You play as a snake, where your goal is to become as long as possible.
Eating food makes your snake longer.

* If the snake runs into a wall or itself, it dies.

* If the snake goes 500 moves without getting food, it dies.

### Controls

The snake moves on its own, but its direction is controlled using the arrow keys.

## Training Computer

You can choose to let the computer learn to play.

When doing so, the computer will simulate a number of generations with random snake AIs.

* **Note** - Depending on how many generations you simulate, training can take a long time.

After the training completes, the computer will keep the best snake from the last generation. You can then play a normal game with the trained snake.

### Choosing How Many Generations to Simulate

Depending on how many generations you simulate, you will begin to see different snake behaviors.

* Generations 0-20: Most snakes in these generations die quickly. Best performers typically are very agressive in going for food, but havent learned to avoid themselves. **Time needed: ~20 minutes**
* Generations 20-30: Snakes begin to learn to go for food in a "circle" so that they can avoid their bodies more often. Still normal for most snakes to die quickly. **Time needed: ~45 minutes**
* Generations 30-40: Less and less snakes die quickly, meaning each generation can take a while. Best performers are better at avoiding themselves. **Time needed: ~2 hours**
* Generation 40+: Best performers can reliably avoid themselves in most cases. Progress will likely begin to stagnate after a while. **Time needed: A lot**

### Genetic Algortihm

The computer trains using a genetic algorithm. **Here's how it works:**
1) The computer randomly generates neural networks for a population of 200 snakes. This is the first generation.
2) A snake game is simulated for all 200 snakes in the generation. Each snake gets a score based on its performance.
3) The top 20 scorers become the parents for the next generation. The remaining 180 snakes are replaced with new children.
4) Each child is generated by randomly crossing the genes of 2 parents. Each gene has a chance to randomly mutate.
5) The process repeats for a given number of generations.




## Built With

* Python 3.6

## Authors

* **Jacob Maxson** 

