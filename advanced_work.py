"""
This is a ciphertext-only attack on an enigma cipher.

To run this whole code takes over 20 minutes on my laptop.
To aid assessment, I've written the results from each calculation and used the results to move onto the next stage.
To run this yourself, you may opt to uncomment each function all below. Be warned it takes a long time.
"""

from advanced_helpers.get_best_rotors import get_best_rotors
from advanced_helpers.find_rotor_configuration import find_rotor_configuration
from advanced_helpers.find_ring_settings import find_ring_settings
from advanced_helpers.find_plugboard import find_plugboard

from enigma import EnigmaMachine

code = "EZMZMAIBMKAREGVODBCPNCFUQRDTGBFZFVWQLHPBCLFDXWMXRDPFGINCSWLLPVGYQZPETGBFDMZBPAAZETKMLWSDDJDAMKSKPRKQSXVCEVCSNZVUILBMAQWSCOPFPQHWQQLHGLWSWLCFXFNQWLUDVDFGBLVXOBEFUUKWYHOROXYKFHCUORYLVPAZAXBJZQHUYKSDZDPSVXLNWUMYUCWXWBPBODLAKKRFEXKRWYQSTIZIFIRRZJDGDYPNFKEHOIJXIISETTPJPSFGURBDUORFTRRJUDMEDTSVHKHQKXYSINHKOGNEHFFJZWAMHEHFGHUYPOXEROSBTPKYLFSVSYWTBOJDBHGYMLIRJZEPUQAASMDLKOUOYKALSPMPANVMQXLHKGNPNPMRRDYAZHURRDXQWUDPBRDTGWZBKNGFAVCMGDMVSQSIRFDEQVZAJUHZDEXFCNJWKQJEJTEXFMVVXVXWEJBFSOUOWYFAEOBMJJJUQCWVXCDIAULASTLXVWUONFLHQINKUVTOXKXJKDCOMCWBJPRLNGKGYZQUYTMDQBTOMRSWBVUVCMKUSXWPYZRKUSKRBCWBGAFC"
rotors = ["I", "II", "III", "IV", "V"]

# Brute force all possible rotor configurations and see how fit they are
# possible_config = find_rotor_configuration(code, rotors, 5)
possible_config = [
    ['IV II V', 0.026243182184691613, 'M D Q'], 
    ['II IV III', 0.026219725557461403, 'B A E'], 
    ['I II III', 0.02621386140065385, 'N E P'], 
    ['V III IV', 0.02621386140065385, 'C S X'], 
    ['II V III', 0.02620213308703874, 'M V L']  ]

# Take each of the top x rotor configurations and return the 3 rotors that performed the best
top_rotors = get_best_rotors(possible_config)

# Take the highest performing rotors and rerun the original algorithm to see their best starting positions
# best_rotor_config = find_rotor_configuration(code, top_rotors, 5)
best_rotor_config = [
    ['II V III', 0.026219725557461403, 'M V L'], 
    ['II III V', 0.026190404773423638, 'H R D'], 
    ['II III V', 0.02613176320534811, 'L S I'], 
    ['III II V', 0.026114170734925446, 'K R N'], 
    ['II V III', 0.02610830657811789, 'J H W'] ]

# Take the best rotor settings and their starting positions and find the optimal ring settings for them
# top_ring_settings = find_ring_settings(best_rotor_config, code, 5)
top_ring_settings = [
    ['II V III', 'J H W', [0, 14], -1613.469756054], 
    ['II III V', 'H R D', [16, 12], -1609.3527085879996], 
    ['II V III', 'M V L', [13, 7], -1588.9218158320002], 
    ['III II V', 'K R N', [16, 16], -1584.0361097100006], 
    ['II III V', 'L S I', [23, 20], -1541.8206898830003]    ]

# Take the optimal rotor settings and use hill climbing to find the optimal plugboard combination
# given that we know how many plugs were used in the encryption
# best_plugboard = find_plugboard(top_ring_settings, code, 2)
best_plugboard = [
    ['II V III', 'J H W', '00 00 14', ['AR', 'DM']], 
    ['II III V', 'H R D', '00 16 12', ['RN', 'AP']], 
    ['II V III', 'M V L', '00 13 07', ['AL', 'AC']], 
    ['III II V', 'K R N', '00 16 16', ['NR', 'GY']], 
    ['II III V', 'L S I', '00 23 20', ['UO', 'AN']] ]

# Take the fittest setting and plugboard combination
best_settings = best_plugboard[0]

# Decrypt the cypher
machine = EnigmaMachine(best_settings[0], "B", best_settings[2], best_settings[1], best_settings[3])
encrypted = machine.encode(code)
print(encrypted)