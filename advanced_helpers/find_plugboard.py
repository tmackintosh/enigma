import math

from classes.PlugLead import PlugLead

from helpers.get_setting import get_setting
from advanced_helpers.n_gram_fitness import n_gram_fitness

from enigma import EnigmaMachine
from helpers.length_assertion import length_assertion
from helpers.type_assertion import type_assertion

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_plugboard(config, code, max_plugs):
    """
    Takes a configured rotor setting and returns an optimal plugboard
    according to the trigram fitness function for English.

    @param config: a list of rotor configurations
        0:  rotors
        1:  initial positions
        2:  ring settings

    @param code: the code to encrypt and compare how fit the settings are

    @returns a list of leads that matches the best plugboard configuration
    """

    # Method defense
    type_assertion(config, list)
    type_assertion(code, str)
    type_assertion(max_plugs, int)

    best_plugs = []

    for settings in config:
        ring_settings = "00 " + get_setting(settings[2][0]) + " " + get_setting(settings[2][1])
        machine = EnigmaMachine(settings[0], "B", ring_settings, settings[1])
        plugs = []

        for _ in range (0, max_plugs):
            # Keep track of the best plug for this setting and adjust when it's beaten
            max_plug = None
            max_fitness = math.inf

            for first_plug in alphabet:
                # If this letter already has a plug attached
                if machine.plugboard.mappings.get(first_plug) is not None:
                    continue

                for second_plug in alphabet:
                    if machine.plugboard.mappings.get(second_plug) is not None:
                        continue

                    # A plug lead cannot go into itself
                    if first_plug == second_plug:
                        continue
                    
                    machine.plugboard.add(PlugLead(first_plug + second_plug))
                    encoded = machine.encode(code)

                    # Trigram fitness function
                    file = "data/trigrams.txt"
                    fitness = n_gram_fitness(encoded, file)

                    # As trigram scores are negative, a "better" trigram score will be more negative
                    if fitness < max_fitness:
                        max_fitness = fitness
                        
                        # In case this is the first plug
                        if max_plug is not None:
                            machine.plugboard.remove(PlugLead(max_plug))

                        max_plug = first_plug + second_plug
                    else:
                        # Reset the plugboard to how it was before
                        machine.plugboard.remove(PlugLead(first_plug + second_plug))

            # This is the best plug for this iteration, so add it to the board
            # We leave the plug attached for the next iteration
            plugs.append(max_plug)
        
        # Output the state in a format friendly to other methods in the advanced work
        state = [settings[0], settings[1], ring_settings, plugs]
        best_plugs.append(state)

    return best_plugs