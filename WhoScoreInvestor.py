# -*- coding=utf-8 -*-
import maimaiUtil
import Strategy
Strategy = Strategy.Strategy


class WhoScoreInvestor(Strategy):
    """
    A WhoScoreInvestor will set up a certain strong/weak team at beginning and then buy every option of ticket equally.
    Only When the team which is set up scored earlier than the opposite, the investor would cash out all the tickets.
    """

    def __init__(self, game_data, strong_team=False, co_action=True):
        Strategy.__init__(self, game_data)
        self.result_dict['strategy_args'] = {
            'strong_team': strong_team
        }
        self.strong_team = strong_team
        self.co_action = co_action

        self.score = '0-0'

    def buy_ticket(self, odds_set):
        """
        Buy all tickets at the beginning

        :param odds_set: list of odds
        """
        if self.money <= 0 or odds_set[-2] == 'Run':
            return


        stake_set = maimaiUtil.buy_1(odds_set)

        self.ticket_bucket = {
            0: {0: (odds_set[0], stake_set[0])},
            1: {0: (odds_set[1], stake_set[1])},
            2: {0: (odds_set[2], stake_set[2])}
        }
        self.store_operation(1, 0, odds_set[0], stake_set[0])
        self.store_operation(1, 1, odds_set[1], stake_set[1])
        self.store_operation(1, 2, odds_set[2], stake_set[2])


        # self.ticket_bucket = {
        #     0: {0: (odds_set[0], 1.0/3)},
        #     1: {0: (odds_set[1], 1.0/3)},
        #     2: {0: (odds_set[2], 1.0/3)}
        # }
        # self.store_operation(1, 0, odds_set[0], 1.0/3)
        # self.store_operation(1, 1, odds_set[1], 1.0/3)
        # self.store_operation(1, 2, odds_set[2], 1.0/3)


        self.invest = 1
        self.money = 0

        if self.strong_team ^ (odds_set[0] < odds_set[2]):
            self.score = '0-1'
        else:
            self.score = '1-0'

    def cash_out(self, odds_set):
        """
        Cash out all tickets when one team scored

        :param odds_set: list of odds
        """
        if odds_set[-2] == 'Run' and odds_set[-1] == self.score:
            total = 0
            for option in self.ticket_bucket:
                for ticket in self.ticket_bucket[option]:
                    (odds, invest) = self.ticket_bucket[option][ticket]
                    try:
                        total += odds / odds_set[option] * invest
                        percentage = Strategy.compute_changing_rate(odds, odds_set[option])
                        self.store_operation(0, option, odds, invest, odds_set[option], percentage)
                    except Exception as e:
                        print e
                        print odds_set
                        print self.result_dict
                        exit(2)

            self.winning += total
            self.ticket_bucket = {0: {}, 1: {}, 2: {}}
