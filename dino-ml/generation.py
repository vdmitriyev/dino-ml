from scanner import Scanner
from network import Network
from time import sleep
import numpy as np
#import pykeyboard
#from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
import copy

class Generation:

    def __init__(self):
        self.__genomes = [Network(name='ANNID#{0}'.format(str(i))) for i in range(12)]
        self.__best_genomes = []

    def execute(self):
        #k = pykeyboard.PyKeyboard()
        keyboard = Controller()
        scanner = Scanner()
        scanner.find_game()
        for genome in self.__genomes:
            print ('\n' + '-'*25 + '\n')
            print ('Try network: {0}'.format(genome.name))
            scanner.reset()
            #keyboard.press('r')
            #keyboard.press('r')
            print('Restart the game')
            sleep(1)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            while True:
                try:
                    print('find_next_obstacle')
                    obs = scanner.find_next_obstacle()
                    inputs = [obs['distance'] / 1000, obs['length'], obs['speed'] / 10]
                    print (inputs)
                    outputs = genome.forward(np.array(inputs, dtype=float))
                    if outputs[0] > 0.55:
                        keyboard.press(Key.space)
                        keyboard.release(Key.space)
                except Exception as ex:
                    print('Exception: {0}'.format(str(ex)))
                    break
            print('Update fitness!')
            genome.fitness = scanner.get_fitness()

    def keep_best_genomes(self):
        self.__genomes.sort(key=lambda x: x.fitness, reverse=True)
        self.__genomes = self.__genomes[:4]
        self.__best_genomes = self.__genomes[:]

    def mutations(self):
        while len(self.__genomes) < 10:
            genome1 = random.choice(self.__best_genomes)
            genome2 = random.choice(self.__best_genomes)
            self.__genomes.append(self.mutate(self.cross_over(genome1, genome2)))
        while len(self.__genomes) < 12:
            genome = random.choice(self.__best_genomes)
            self.__genomes.append(self.mutate(genome))

    def cross_over(self, genome1, genome2):
        new_genome = copy.deepcopy(genome1)
        other_genome = copy.deepcopy(genome2)
        cut_location = int(len(new_genome.W1) * random.uniform(0, 1))
        for i in range(cut_location):
            new_genome.W1[i], other_genome.W1[i] = other_genome.W1[i], new_genome.W1[i]
        cut_location = int(len(new_genome.W2) * random.uniform(0, 1))
        for i in range(cut_location):
            new_genome.W2[i], other_genome.W2[i] = other_genome.W2[i], new_genome.W2[i]
        return new_genome

    def __mutate_weights(self, weights):
        if random.uniform(0, 1) < 0.2:
            return weights * (random.uniform(0, 1) - 0.5) * 3 + (random.uniform(0, 1) - 0.5)
        else:
            return 0

    def mutate(self, genome):
        new_genome = copy.deepcopy(genome)
        new_genome.W1 += self.__mutate_weights(new_genome.W1)
        new_genome.W2 += self.__mutate_weights(new_genome.W2)
        return new_genome
