# def solution(players, callings):
#     answer = []
#
#     for call in callings:
#         index = 0
#         for p in players:
#             if p == call:
#                 temp = p
#                 p = players[index - 1]
#                 players[index - 1] = temp
#                 players[index] = p
#                 print(players)
#             else:
#                 index += 1
#
#     answer = players
#     return answer

def solution(players, callings):
    player_map = {}
    for index, player in enumerate(players):
        player_map[player] = index

    for cal in callings:

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
order = solution(players, callings)
print(order)