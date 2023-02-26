states_of_India = ['Uttarakhand', 'Uttar Pradesh', 'Madhya Pradesh']
print(states_of_India[1])
print(states_of_India[-1])
states_of_India[1] = 'Uttar-Pradesh'
unknown_states = ['Delhi', 'karnataka', 'Kerela']
states_of_India.extend(unknown_states)   #instead of append
print(states_of_India)

print(len(states_of_India))