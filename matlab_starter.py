import pickle

import LoadData
import WhoScoreInvestor

GameData = LoadData.GameData



mode = 'w'


def getGameData():
    if mode == 'w':
        game_data = GameData.get_data_from_mysql(sql='SELECT CAST(WIN310_EUROPE_ID as UNSIGNED) FROM t_crawler_win310 where START_DATE_TIME > "2016-09-17 00:00:00" order by START_DATE_TIME')

        pickle.dump(game_data, open("game_data.p", "wb"))
    elif mode == 'r':
        game_data = matlab_get_data()
    else:
        game_data=[]

    return game_data


def matlab_get_data():
    gamedata = pickle.load(open('game_data.p', 'rb'))
    return gamedata


def process_one_game(game):

    i = WhoScoreInvestor.WhoScoreInvestor(game, strong_team=True)
    i.game_processing()
    return i


## demo for MATLAB calling py.XXX.search(...)
def helloworld():
    return "Matlab says: 'Hello Python.'"


if __name__ == "__main__":

    game_data = getGameData()
    print(game_data)

    for i in range(200):
        it = process_one_game(game_data[i])
        print(it.operation_list)
        print(it.result_dict)

