import numpy as np
import copy

class GeneticAlgorithm():
    #relu function
    def relu(x):
        if x < 0:
            return 0
        return x
    #performs a full forward propogation of the neural network
    def full_forward_prop(curr_pop, initial_inputs):
        inputs = initial_inputs
        #len(curr_pop) = (number of layers in neural network) - 1
        for i in range(len(curr_pop)):
            member = curr_pop[i]
            inputs = GeneticAlgorithm.one_layer_prop(member, inputs)
        #gets max value of output nodes, then returns the index.
        max_value = max(inputs)
        return inputs.index(max_value)
    #propogates through one layer of the neural network
    def one_layer_prop(member, inputs):
        new_inputs = []
        #generates all output node values
        for i in range(len(member[0])):
            z = 0
            #adds up all input nodes and their associated weights to a given output node
            for j in range(len(member)):
                z += inputs[j]*member[j][i]
            #output node is assigned the relu of the summation
            new_inputs.append(GeneticAlgorithm.relu(z))
        #returns the values of the output nodes which will become the input nodes of the next layer
        return new_inputs

    def crossover(new_pop, num_additions, num_parents, mutation_rate):
        children = copy.deepcopy(new_pop)
        for i in range(num_additions):
            #seeds random number generator
            np.random.seed()
            #creates deep copies to avoid changing parents
            new_member = copy.deepcopy(new_pop[i%num_parents])
            parent2_copy = copy.deepcopy(new_pop[(i+1)%num_parents])
            #loops through every weight in a given neural network to create new neural network
            for j in range(len(new_member)):
                for k in range(len(new_member[j][0])):
                    for m in range(len(new_member[j])):
                        #determines if gene from parent 1 or 2 will be used, then mutates gene and adds it to the child
                        choice = np.random.random_sample()
                        if choice > .85:
                            new_gene =  GeneticAlgorithm.mutate(parent2_copy[j][m][k],mutation_rate)
                            new_member[j][m][k] = new_gene
                        else:
                            new_gene = GeneticAlgorithm.mutate(new_member[j][m][k],mutation_rate)
                            new_member[j][m][k] = new_gene
            #adds new member to population
            children.append(new_member)
        return children

    def mutate(gene, mutation_rate):
        #decides if gene will be mutated
        mutation = np.random.random_sample()
        if mutation < mutation_rate:
            gene += np.random.randn()
        return gene