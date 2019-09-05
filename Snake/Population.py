from Snake import Snake
from GeneticAlgorithm import GeneticAlgorithm as ga
import numpy as np
import time
import copy

class Population():
    def __init__(self):
        pass
    def simulate_generations(self, num_generations):
        sol_per_pop = 200

        num_input_layer = 9

        num_HL_1 = 18

        num_HL_2 = 18

        num_output_layer = 4

        num_parents = 20

        pop_size = (sol_per_pop,num_input_layer,num_HL_1,num_HL_2,num_output_layer)

        print(pop_size)

        initial_inputs = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

        #generates population of snakes with randomly assigned weights
        new_population = []
        for i in range(sol_per_pop):
            np.random.seed()
            weights = []
            weights.append(np.random.randn(num_input_layer,num_HL_1))
            weights.append(np.random.randn(num_HL_1,num_HL_2))
            weights.append(np.random.randn(num_HL_2,num_output_layer))
            new_population.append(weights)
        
        for generation in range(num_generations):
            print("\n\nGeneration: " + str(generation+1))
            scores = []
            sum = 0
            for member in range(len(new_population)):
                snake = Snake(False,new_population[member])
                final_score = snake.new_game()
                #print("Snake: " + str(member+1) + " Score: " + str(final_score))
                scores.append(final_score)
                sum += final_score
            parents = []
            best_score = max(scores)
            print("\nBest performers:")
            for i in range(num_parents):
                max_value = max(scores)
                max_index = scores.index(max_value)
                parents.append(new_population[max_index])
                scores[max_index] = -1000000000
                print(max_value)
            new_population = ga.crossover(parents, (sol_per_pop-num_parents), num_parents, .1)
            print("\n\nGeneration " + str(generation+1) + " results:\nHighest Score: " + str(best_score) + "\nAverage score: " + str(sum/sol_per_pop))
            time.sleep(1)
        snake.reset_window()
        return new_population[0]
    def simulate_snake(self, snake_prototype):
        snake = Snake(False,snake_prototype)
        final_score = snake.new_game()
        print("\nFinal score: " + str(final_score))
        time.sleep(1)
        snake.reset_window()

        

