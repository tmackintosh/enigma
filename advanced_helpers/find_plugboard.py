import math

from classes.PlugLead import PlugLead

from helpers.get_setting import get_setting
from advanced_helpers.n_gram_fitness import n_gram_fitness

from enigma import EnigmaMachine

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_plugboard(config, code):
    best_plugs = []

    for settings in config:
        ring_settings = "00 " + get_setting(settings[2][0]) + " " + get_setting(settings[2][1])
        machine = EnigmaMachine(settings[0], "B", ring_settings, settings[1])
        max_plugs = 2
        plugs = []

        for i in range (0, max_plugs):
            max_plug = None
            max_fitness = math.inf

            for first_plug in alphabet:
                for second_plug in alphabet:
                    if first_plug == second_plug:
                        continue

                    machine.plugboard.add(PlugLead(first_plug + second_plug))
                    encoded = machine.encode(code)

                    file = "data/trigrams.txt"
                    fitness = n_gram_fitness(encoded, file)

                    if fitness < max_fitness:
                        max_fitness = fitness
                        
                        if max_plug is not None:
                            machine.plugboard.remove(PlugLead(max_plug))

                        max_plug = first_plug + second_plug
                    else:
                        machine.plugboard.remove(PlugLead(first_plug + second_plug))

                    print(max_plug, first_plug)

            plugs.append(max_plug)
        
        state = [settings[0], settings[1], ring_settings, plugs]
        best_plugs.append(state)

    return best_plugs