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
# possible_config = find_rotor_configuration(code, top_rotors)
possible_config = [
    ['II V III', 0.026219725557461403, 'M V L'], 
    ['II III V', 0.026190404773423638, 'H R D'], 
    ['II III V', 0.02613176320534811, 'L S I'], 
    ['III II V', 0.026114170734925446, 'K R N'], 
    ['II V III', 0.02610830657811789, 'J H W'] ]

best_settings = []

def fitness_value(a):
    return a[3]

for enigma_state in possible_config:
    machine = EnigmaMachine(enigma_state[0], "A", initial_positions = enigma_state[2])

    optimal_rotor_setting_1 = optimise_rotor_setting(machine, 1, code)[0]
    machine.starting_rotor.setting = optimal_rotor_setting_1[1]

    optimal_rotor_setting_2 = optimise_rotor_setting(machine, 2, code)[0]
    machine.starting_rotor.left_connection.setting = optimal_rotor_setting_2[1]

    encoded = machine.encode(code)
    fitness = bigram_fitness(encoded)
    state = [enigma_state[0], enigma_state[2], [optimal_rotor_setting_1, optimal_rotor_setting_2], fitness]
    best_settings.append(state)

best_settings.sort(key = fitness_value)
print(best_settings)