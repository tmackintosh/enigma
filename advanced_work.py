import collections

from advanced_helpers.bigram_fitness import bigram_fitness
from advanced_helpers.find_ring_settings import find_ring_settings
from advanced_helpers.optimise_ring_setting import optimise_rotor_setting
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
# best_rotor_config = find_rotor_configuration(code, top_rotors)
best_rotor_config = [
    ['II V III', 0.026219725557461403, 'M V L'], 
    ['II III V', 0.026190404773423638, 'H R D'], 
    ['II III V', 0.02613176320534811, 'L S I'], 
    ['III II V', 0.026114170734925446, 'K R N'], 
    ['II V III', 0.02610830657811789, 'J H W'] ]

# top_ring_settings = find_ring_settings(best_rotor_config, code)
top_ring_settings = [
    ['II V III', 'J H W', [0, 14], -1613.469756054], 
    ['II III V', 'H R D', [16, 12], -1609.3527085879996], 
    ['II V III', 'M V L', [13, 7], -1588.9218158320002], 
    ['III II V', 'K R N', [16, 16], -1584.0361097100006], 
    ['II III V', 'L S I', [23, 20], -1541.8206898830003]    ]

