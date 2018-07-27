# Create a method, which takes the state and gross income as the arguments and return the net income after deducting tax
# based on the state.
# Assume federal tax: 10%
# Assume state tax on your wish

# You don't have to do for all the states, just take 3-4 to solve the purpose of the exercise


def calculate_net_income(state, gross_income):
    state_tax = {'CA': 10, 'NY': 8, 'OR': 9, 'TX': 0}
    net_income = gross_income - (gross_income * .10)
    if state in state_tax:
        net_income = net_income - (gross_income * state_tax[state] / 100)
        return net_income


result = int(calculate_net_income('OR', 150000))
print('Your net income after all the heavy taxes is: ' + str(result))
