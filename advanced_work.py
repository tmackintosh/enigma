import collections

from advanced_helpers.bigram_fitness import bigram_fitness
from advanced_helpers.find_ring_settings import optimise_rotor_setting
from advanced_helpers.find_rotor_configuration import find_rotor_configuration
from advanced_helpers.get_best_rotors import get_best_rotors
from helpers.get_string_form import get_string_form
from enigma import EnigmaMachine

code = "OZLUDYAKMGMXVFVARPMJIKVWPMBVWMOIDHYPLAYUWGBZFAFAFUQFZQISLEZMYPVBRDDLAGIHIFUJDFADORQOOMIZPYXDCBPWDSSNUSYZTJEWZPWFBWBMIEQXRFASZLOPPZRJKJSPPSTXKPUWYSKNMZZLHJDXJMMMDFODIHUBVCXMNICNYQBNQODFQLOGPZYXRJMTLMRKQAUQJPADHDZPFIKTQBFXAYMVSZPKXIQLOQCVRPKOBZSXIUBAAJBRSNAFDMLLBVSYXISFXQZKQJRIQHOSHVYJXIFUZRMXWJVWHCCYHCXYGRKMKBPWRDBXXRGABQBZRJDVHFPJZUSEBHWAEOGEUQFZEEBDCWNDHIAQDMHKPRVYHQGRDYQIOEOLUBGBSNXWPZCHLDZQBWBEWOCQDBAFGUVHNGCIKXEIZGIZHPJFCTMNNNAUXEVWTWACHOLOLSLTMDRZJZEVKKSSGUUTHVXXODSKTFGRUEIIXVWQYUIPIDBFPGLBYXZTCOQBCAHJYNSGDYLREYBRAKXGKQKWJEKWGAPTHGOMXJDSQKYHMFGOLXBSKVLGNZOAXGVTGXUIVFTGKPJU"
rotors = ["I", "II", "III", "IV", "V"]


# possible_config = find_rotor_configuration(code, rotors)
possible_config = [
    ['IV II V', 0.026243182184691613, 'M D Q'], 
    ['II IV III', 0.026219725557461403, 'B A E'], 
    ['I II III', 0.02621386140065385, 'N E P'], 
    ['V III IV', 0.02621386140065385, 'C S X'], 
    ['II V III', 0.02620213308703874, 'M V L']  ]

top_rotors = get_best_rotors(possible_config)
possible_config = find_rotor_configuration(code, top_rotors)

for rotor_config in top_rotors:
    print(possible_config)

    for enigma_state in possible_config:
        machine = EnigmaMachine(get_string_form(rotor_config), "A", initial_positions = enigma_state[2])

        optimal_rotor_setting = optimise_rotor_setting(machine, 1, code)[0]
        machine.starting_rotor.setting = optimal_rotor_setting[1]

        optimal_rotor_setting = optimise_rotor_setting(machine, 2, code)[0]
        machine.starting_rotor.left_connection.setting = optimal_rotor_setting[1]

        encoded = machine.encode(code)
        print(bigram_fitness(encoded))