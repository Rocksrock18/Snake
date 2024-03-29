from Snake import Snake
from GeneticAlgorithm import GeneticAlgorithm as ga
import numpy as np
import time
import copy

class Population():
    def __init__(self):
        pass
    def simulate_generations(self, num_generations):
        #number of snakes in a population
        sol_per_pop = 200
        #number of nodes in input layer
        num_input_layer = 9
        #number of nodes in hidden layer 1
        num_HL_1 = 18
        #number of nodes in hidden layer 2
        num_HL_2 = 18
        #number of nodes in output layer
        num_output_layer = 4
        #number of parents per generation
        num_parents = 20

        #generates population of snakes with randomly assigned weights
        new_population = []
        for i in range(sol_per_pop):
            np.random.seed()
            weights = []
            weights.append(np.random.randn(num_input_layer,num_HL_1))
            weights.append(np.random.randn(num_HL_1,num_HL_2))
            weights.append(np.random.randn(num_HL_2,num_output_layer))
            new_population.append(weights)
        #simulates a generation of snakes. Repeats depending on how many generations are being simulated.
        for generation in range(num_generations):
            print("\n\nGeneration: " + str(generation+1))
            scores = []
            sum = 0
            #simulates a single generation
            for member in range(len(new_population)):
                snake = Snake(False,new_population[member])
                final_score = snake.new_game()
                scores.append(final_score)
                sum += final_score
            parents = []
            best_score = max(scores)
            #Determines best performers, who will become parents of next generation
            print("\nBest performers:")
            for i in range(num_parents):
                max_value = max(scores)
                max_index = scores.index(max_value)
                parents.append(new_population[max_index])
                scores[max_index] = -1000000000
                print(max_value)
            #fills in rest of new generation with new children
            new_population = ga.crossover(parents, (sol_per_pop-num_parents), num_parents, .1)
            #prints generation results
            print("\n\nGeneration " + str(generation+1) + " results:\nHighest Score: " + str(best_score) + "\nAverage score: " + str(sum/sol_per_pop))
            time.sleep(1)
        snake.reset_window()
        return new_population[0]
    #simulates a single snake game
    def simulate_snake(self, snake_prototype):
        snake = Snake(False,snake_prototype)
        final_score = snake.new_game()
        print("\nFinal score: " + str(final_score))
        time.sleep(1)
        snake.reset_window()

        

