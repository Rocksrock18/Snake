import numpy as np
import copy

class GeneticAlgorithm():
    def sigmoid(x):
        return 1/(1+np.exp(-x))
    def relu(x):
        if x < 0:
            return 0
        return x

    def full_forward_prop(curr_pop, initial_inputs):
        inputs = initial_inputs
        for i in range(len(curr_pop)):
            member = curr_pop[i]
            inputs = GeneticAlgorithm.one_layer_prop(member, inputs)
        #gets max value of output nodes, then returns the index.
        max_value = max(inputs)
        return inputs.index(max_value)

    def one_layer_prop(member, inputs):
        new_inputs = []
        for i in range(len(member[0])):
            z = 0
            for j in range(len(member)):
                z += inputs[j]*member[j][i]
            new_inputs.append(GeneticAlgorithm.relu(z))
        return new_inputs

    def crossover(new_pop, num_additions, num_parents, mutation_rate):
        children = copy.deepcopy(new_pop)
        for i in range(num_additions):
            np.random.seed()
            new_member = copy.deepcopy(new_pop[i%num_parents])
            parent2_copy = copy.deepcopy(new_pop[(i+1)%num_parents])
            for j in range(len(new_member)):
                for k in range(len(new_member[j][0])):
                    for m in range(len(new_member[j])):
                        choice = np.random.random_sample()
                        if choice > .85:
                            new_gene =  GeneticAlgorithm.mutate(parent2_copy[j][m][k],mutation_rate)
                            new_member[j][m][k] = new_gene
                        else:
                            new_gene = GeneticAlgorithm.mutate(new_member[j][m][k],mutation_rate)
                            new_member[j][m][k] = new_gene
            children.append(new_member)
        return children

    def mutate(gene, mutation_rate):
        mutation = np.random.random_sample()
        if mutation < mutation_rate:
            gene += np.random.randn()
        return gene