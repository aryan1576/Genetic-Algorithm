""" 
    A genetic algorithm code to find the minima of any function.
    Here first we have to decide the number of variables present in the objective function.
    once that calculated , we can take the value of population count , number of iterations , max and min
    values of the variables accordingly """




from random import randint, random
from operator import add

def individual(length, min, max):
    'Create a member of the population.'
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual):
    """
    Determine the fitness of an individual.
    Since we are doing minimum optimisation , the lower the value the better the answer

    individual: the individual to evaluate
    """
    a=[]
    for i in individual:
       a.append(i)
    x=a[0]
    y=a[1]
    fit= -(2*x*x + 3*y*(x-2*y)/((x+y)*(x+y)+5))


    return fit

def grade(pop):
    'Find average fitness for a population.'
    summed = 0
    for x in pop:
        summed = summed + fitness(x)

    return summed / (len(pop) * 1.0)

def evolve(pop, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            child = male[:1] + female[1:] # Assigning some part of male and female to the child
            children.append(child)
    parents.extend(children)
    return parents

print('To find the maxima of the following function')
print('f(x,y)= 2x^2 + 3y(x-2y)/((x+y)^2+5)')

p_count = int(input('Enter the population count : '))
i_length = 2
i_min = int(input('Enter the lower limit of the variables : '))
i_max = int(input('Enter the upper limit of the variables : '))
iteration = int(input('Enter the number of iterations : '))
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p),]
for i in range(iteration):
    p = evolve(p)
    fitness_history.append(grade(p))
    print (abs(grade(p)))
graded = [(fitness(x), x) for x in p ]
i=0
graded = sorted(graded)
for g in graded:                       # To print the final solution
    if i==0 :
         print (abs(g[0]),g[1])
    else :
         break
    i=i+1
