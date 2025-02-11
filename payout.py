import numpy as np


# Function to return the potential payout using the odds and amount wagered.
def calculate_payout(odds_str, amount_bet):
    try:
        odds = float(odds_str)
        if odds >= 100:
            payout = amount_bet * (odds / 100)
            return round(payout, 2)
        else:
            payout = amount_bet / (abs(odds) / 100)
            return round(payout, 2)
    except ValueError:
        return "Invalid odds format. Please enter a valid number."



def calculate_bet_amount(odds_str, desired_return):
    try:
        odds = float(odds_str)
        if odds >= 100:
            bet_amount = desired_return / (odds / 100)
            return round(bet_amount, 2)
        else:
            bet_amount = desired_return * (abs(odds) / 100)
            return round(bet_amount, 2)
    except ValueError:
        return "Invalid odds format. Please enter a valid number."

# Example usage:
# odds = "+110"
# amount_bet = 50.0
# potential_payout = calculate_payout(odds, amount_bet)
# print(f"The potential payout for a bet of ${amount_bet} at odds {odds} is ${potential_payout}")

# # Example usage:
# odds = "+110"
# desired_return = 100.0
# required_bet_amount = calculate_bet_amount(odds, desired_return)
# print(f"To win ${desired_return} with odds {odds}, you need to bet ${required_bet_amount}")



# bonus_bet = 500

# both_lines = (-105, -120)

# potential_wins = (calculate_payout(both_lines[0], bonus_bet), calculate_payout(both_lines[1], bonus_bet))
# hedge_amounts = (calculate_bet_amount(both_lines[1], potential_wins[0] + bonus_bet), calculate_bet_amount(both_lines[0], potential_wins[1] + bonus_bet))
# total_net = ()

# print(f"You have a bonus bet of ${bonus_bet}.")
# print(f"The lines are {both_lines}.")
# print(f"The potential wins are {potential_wins}")
# print(f"The amounts needed to hedge your bets are {hedge_amounts}")



# for x in range(100):

#     bonus = 500
#     hedge = 345
#     both_lines = (-105, -120)

#     # (first_win, first_loss, second_win, second_loss)
#     possible_payouts = ((calculate_payout(both_lines[0], bonus) + bonus) - hedge,
#                         (calculate_payout(both_lines[1], hedge) + hedge),
#                         (calculate_payout(both_lines[1], bonus) + bonus) - hedge,
#                         (calculate_payout(both_lines[0], hedge) + hedge))

#     ave = ((possible_payouts[0] + possible_payouts[1]) / 2, (possible_payouts[2] + possible_payouts[3]) / 2)
#     dist = (abs(possible_payouts[0] - possible_payouts[1]), abs(possible_payouts[2] - possible_payouts[3]))

#     payout = (calculate_payout(both_lines[0], bonus) + bonus) - hedge

#     print(f"Bonus on first and it wins: ${payout}")

#     payout = (calculate_payout(both_lines[1], hedge) + hedge)

#     print(f"Bonus on first and it loses: ${payout}")

#     payout = (calculate_payout(both_lines[1], bonus) + bonus) - hedge

#     print(f"Bonus on second and it wins: ${payout}")

#     payout = (calculate_payout(both_lines[0], hedge) + hedge)

#     print(f"Bonus on second and it loses: ${payout}")



#     print(dist[0])
#     print(x)
#     print(ave)
#     print(dist)


def calculate_best_hedge(bonus, both_lines): 
    distances = []
    distance_hedge = []

    for hedge in range(bonus * 2):
        possible_payouts = ((calculate_payout(both_lines[0], bonus) + bonus) - hedge,
                            (calculate_payout(both_lines[1], hedge) + hedge),
                            (calculate_payout(both_lines[1], bonus) + bonus) - hedge,
                            (calculate_payout(both_lines[0], hedge) + hedge))


        dist = abs(possible_payouts[0] - possible_payouts[1])

        distances.append(dist)

        distance_hedge.append((dist, hedge))

    a = np.array(distances)
    mymin = np.argmin(a) + 1
    print(mymin)
    print(distance_hedge[mymin][1])
    return np.argmin(a)


    




bonus = 10000
both_lines = (-125, -105)


hedge = calculate_best_hedge(bonus, both_lines)

# # (first_win, first_loss, second_win, second_loss)
# possible_payouts = ((calculate_payout(both_lines[0], bonus) + bonus) - hedge,
#                     (calculate_payout(both_lines[1], hedge) + hedge),
#                     (calculate_payout(both_lines[1], bonus) + bonus) - hedge,
#                     (calculate_payout(both_lines[0], hedge) + hedge))

# ave = ((possible_payouts[0] + possible_payouts[1]) / 2, (possible_payouts[2] + possible_payouts[3]) / 2)
# dist = (abs(possible_payouts[0] - possible_payouts[1]), abs(possible_payouts[2] - possible_payouts[3]))

# # payout = (calculate_payout(both_lines[0], bonus) + bonus) - hedge

# # print(f"Bonus on first and it wins: ${payout}")

# # payout = (calculate_payout(both_lines[1], hedge) + hedge)

# # print(f"Bonus on first and it loses: ${payout}")

# # payout = (calculate_payout(both_lines[1], bonus) + bonus) - hedge

# # print(f"Bonus on second and it wins: ${payout}")

# # payout = (calculate_payout(both_lines[0], hedge) + hedge)

# # print(f"Bonus on second and it loses: ${payout}")



# print(dist[0])
# print(possible_payouts)



