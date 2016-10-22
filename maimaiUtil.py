# -*- coding=utf-8 -*-
"""
Utilities for buy and sell .
"""

def buy_1(odds_set):
    # self.ticket_bucket = {
    #     0: {0: (odds_set[0], 1.0/3)},
    #     1: {0: (odds_set[1], 1.0/3)},
    #     2: {0: (odds_set[2], 1.0/3)}
    # }
    # self.store_operation(1, 0, odds_set[0], 1.0/3)
    # self.store_operation(1, 1, odds_set[1], 1.0/3)
    # self.store_operation(1, 2, odds_set[2], 1.0/3)

    margin = 1/odds_set[0] + 1/odds_set[1] + 1/odds_set[2]
    stake0 = 1/odds_set[0]/margin * 1
    stake1 = 1/odds_set[1]/margin * 1
    stake2 = 1/odds_set[2]/margin * 1

    stake_set = [stake0, stake1, stake2]

    return stake_set


def pick_odds_set(odds_sets):





    pass











def compute_changing_rate(ticket_odds, market_odds):
    """
    Compute changing rate

    :param ticket_odds: odds when this ticket was bought
    :param market_odds: current market odds
    :return: rate of win or loss
    """
    try:
        if ticket_odds > market_odds:
            return (ticket_odds - market_odds) / (market_odds * (ticket_odds - 1)) + 1
        else:
            return ticket_odds / market_odds - 1
    except ZeroDivisionError:
        return 0



