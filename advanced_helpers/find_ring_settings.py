from advanced_helpers.index_of_coincidence import index_of_coincidence

def fitness_value(a):
    return a[2]

def optimise_rotor_setting(machine, rotor_number, code):
    rotor = machine.starting_rotor
    starting_position = rotor.position

    top_fitness_states = []

    while rotor_number > 1:
        rotor = rotor.left_connection

    for i in range (0, 26):
        rotor.setting = i
        rotor.position = (starting_position + i) % 26
        
        encrypted = machine.encode(code)
        fitness = index_of_coincidence(encrypted)

        state = [rotor_number, i, fitness]

        top_fitness_states.append(state)
        top_fitness_states.sort(key = fitness_value, reverse = True)

        if len(top_fitness_states) > 5:
            top_fitness_states.pop()

    return top_fitness_states