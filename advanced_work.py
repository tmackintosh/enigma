import math
from advanced_helpers.find_plugboard import find_plugboard

from advanced_helpers.n_gram_fitness import n_gram_fitness
from classes.PlugLead import PlugLead

from advanced_helpers.get_best_rotors import get_best_rotors
from advanced_helpers.find_rotor_configuration import find_rotor_configuration
from advanced_helpers.find_ring_settings import find_ring_settings

from helpers.get_setting import get_setting

from enigma import EnigmaMachine

code = "EZMZMAIBMKAREGVODBCPNCFUQRDTGBFZFVWQLHPBCLFDXWMXRDPFGINCSWLLPVGYQZPETGBFDMZBPAAZETKMLWSDDJDAMKSKPRKQSXVCEVCSNZVUILBMAQWSCOPFPQHWQQLHGLWSWLCFXFNQWLUDVDFGBLVXOBEFUUKWYHOROXYKFHCUORYLVPAZAXBJZQHUYKSDZDPSVXLNWUMYUCWXWBPBODLAKKRFEXKRWYQSTIZIFIRRZJDGDYPNFKEHOIJXIISETTPJPSFGURBDUORFTRRJUDMEDTSVHKHQKXYSINHKOGNEHFFJZWAMHEHFGHUYPOXEROSBTPKYLFSVSYWTBOJDBHGYMLIRJZEPUQAASMDLKOUOYKALSPMPANVMQXLHKGNPNPMRRDYAZHURRDXQWUDPBRDTGWZBKNGFAVCMGDMVSQSIRFDEQVZAJUHZDEXFCNJWKQJEJTEXFMVVXVXWEJBFSOUOWYFAEOBMJJJUQCWVXCDIAULASTLXVWUONFLHQINKUVTOXKXJKDCOMCWBJPRLNGKGYZQUYTMDQBTOMRSWBVUVCMKUSXWPYZRKUSKRBCWBGAFC"
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

# best_plugboard = find_plugboard(top_ring_settings, code)
best_plugboard = [
    ['II V III', 'J H W', '00 00 14', ['AR', 'DM']], 
    ['II III V', 'H R D', '00 16 12', ['RN', 'AP']], 
    ['II V III', 'M V L', '00 13 07', ['AL', 'AC']], 
    ['III II V', 'K R N', '00 16 16', ['NR', 'GY']], 
    ['II III V', 'L S I', '00 23 20', ['UO', 'AN']] ]

best_settings = best_plugboard[0]

machine = EnigmaMachine(best_settings[0], "B", best_settings[2], best_settings[1], best_settings[3])
encrypted = machine.encode(code)
print(encrypted)