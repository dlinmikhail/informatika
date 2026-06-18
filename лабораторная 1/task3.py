
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 #индекс относительно которого будут разделены команды

first_team = list_players[:middle_index] #первая команда
second_team = list_players[middle_index:] #вторая команда

print(first_team)
print(second_team)