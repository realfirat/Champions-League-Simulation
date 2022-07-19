from team import Team
from prettytable import PrettyTable
import random
import match_system

# Setting the teams
barcelona = Team("Barcelona", "Spain", 0.95)
madrid = Team("Real Madrid", "Spain", 0.95)
psg = Team("PSG", "France", 0.85)
manchester = Team("Manchester United", "UK", 0.85)
liverpool = Team("Liverpool", "UK", 0.75)
bayern = Team("Bayern Munich", "Germany", 0.75)
juventus = Team("Juventus", "Italy", 0.65)
manccity = Team("Manchester City", "UK", 0.65)
chelsea = Team("Chelsea", "UK", 0.55)
borussia = Team("Borussia Dortmund", "Germany", 0.55)
milan = Team("AC Milan", "Italy", 0.45)
lokomotiv = Team("Lokomotiv Moskva", "Russia", 0.45)
porto = Team("Porto", "Portugal", 0.35)
ajax = Team("Ajax", "Holland", 0.35)
brugge = Team("Club Brugge", "Belgium", 0.25)
besiktas = Team("Beşiktaş", "Turkey", 0.25)

# generating the groups
all_teams = [barcelona, madrid, psg, manchester, liverpool, bayern, juventus, manccity, chelsea, borussia, milan,
             lokomotiv, porto, ajax, brugge, besiktas]
group_a = []
group_b = []
group_c = []
group_d = []

for team in all_teams:
    while team not in group_a and team not in group_b and team not in group_c and team not in group_d:
        rand_int = random.randint(0, 3)
        if rand_int == 0 and len(group_a) < 4:
            group_a.append(team)
        elif rand_int == 1 and len(group_b) < 4:
            group_b.append(team)
        elif rand_int == 2 and len(group_c) < 4:
            group_c.append(team)
        elif rand_int == 3 and len(group_d) < 4:
            group_d.append(team)

# printing the groups
all_groups = [group_a, group_b, group_c, group_d]
print()
print("  GROUPS:  ")
print("--------------------")
for group in all_groups:
    if group == group_a:
        group_table_a = PrettyTable()
        group_table_a.field_names = ["GROUP A", "Country"]
        group_table_a.align["GROUP A"] = "l"
        for team in group:
            group_table_a.add_row([team.name, team.nation])
    elif group == group_b:
        group_table_b = PrettyTable()
        group_table_b.field_names = ["GROUP B", "Country"]
        group_table_b.align["GROUP B"] = "l"
        for team in group:
            group_table_b.add_row([team.name, team.nation])
    elif group == group_c:
        group_table_c = PrettyTable()
        group_table_c.field_names = ["GROUP C", "Country"]
        group_table_c.align["GROUP C"] = "l"
        for team in group:
            group_table_c.add_row([team.name, team.nation])
    elif group == group_d:
        group_table_d = PrettyTable()
        group_table_d.field_names = ["GROUP D", "Country"]
        group_table_d.align["GROUP D"] = "l"
        for team in group:
            group_table_d.add_row([team.name, team.nation])

print(group_table_a)
print(group_table_b)
print(group_table_c)
print(group_table_d)


# generating matches
matches = []
matches_text = []
for group in all_groups:
    matches.append([group[0], group[1]])
    matches.append([group[0], group[2]])
    matches.append([group[0], group[3]])
    matches.append([group[1], group[2]])
    matches.append([group[1], group[3]])
    matches.append([group[2], group[3]])

    matches_text.append([group[0].name, group[1].name])
    matches_text.append([group[0].name, group[2].name])
    matches_text.append([group[0].name, group[3].name])
    matches_text.append([group[1].name, group[2].name])
    matches_text.append([group[1].name, group[3].name])
    matches_text.append([group[2].name, group[3].name])

# generating scores of the matches
print()
print()
print("MATCHES & RESULTS: ")
print("--------------------")
for m in matches:
    match_system.match(m[0], m[1])

# Generating groups' matches' results
group_a_standing = {
    group_a[0]: [group_a[0].points, group_a[0].average],
    group_a[1]: [group_a[1].points, group_a[1].average],
    group_a[2]: [group_a[2].points, group_a[2].average],
    group_a[3]: [group_a[3].points, group_a[3].average]
}
group_b_standing = {
    group_b[0]: [group_b[0].points, group_b[0].average],
    group_b[1]: [group_b[1].points, group_b[1].average],
    group_b[2]: [group_b[2].points, group_b[2].average],
    group_b[3]: [group_b[3].points, group_b[3].average]
}
group_c_standing = {
    group_c[0]: [group_c[0].points, group_c[0].average],
    group_c[1]: [group_c[1].points, group_c[1].average],
    group_c[2]: [group_c[2].points, group_c[2].average],
    group_c[3]: [group_c[3].points, group_c[3].average]
}
group_d_standing = {
    group_d[0]: [group_d[0].points, group_d[0].average],
    group_d[1]: [group_d[1].points, group_d[1].average],
    group_d[2]: [group_d[2].points, group_d[2].average],
    group_d[3]: [group_d[3].points, group_d[3].average]
}

group_a_standing = sorted(group_a_standing.items(), key=lambda item: item[1], reverse=True)
group_b_standing = sorted(group_b_standing.items(), key=lambda item: item[1], reverse=True)
group_c_standing = sorted(group_c_standing.items(), key=lambda item: item[1], reverse=True)
group_d_standing = sorted(group_d_standing.items(), key=lambda item: item[1], reverse=True)
all_group_standings = [group_a_standing, group_b_standing, group_c_standing, group_d_standing]


# printing group results
print()
print()
print("STANDINGS: ")

group_a_table = PrettyTable()
group_b_table = PrettyTable()
group_c_table = PrettyTable()
group_d_table = PrettyTable()
group_a_table.field_names = ["GROUP A", "Points", "Average"]
group_b_table.field_names = ["GROUP B", "Points", "Average"]
group_c_table.field_names = ["GROUP C", "Points", "Average"]
group_d_table.field_names = ["GROUP D", "Points", "Average"]

i = 0
for group in all_group_standings:
    if group == group_a_standing:
        for key, value in group:
            group_a_table.add_row([key.name, value[0], value[1]])
    elif group == group_b_standing:
        for key, value in group:
            group_b_table.add_row([key.name, value[0], value[1]])
    elif group == group_c_standing:
        for key, value in group:
            group_c_table.add_row([key.name, value[0], value[1]])
    elif group == group_d_standing:
        for key, value in group:
            group_d_table.add_row([key.name, value[0], value[1]])

group_a_table.align["GROUP A"] = "l"
group_b_table.align["GROUP B"] = "l"
group_c_table.align["GROUP C"] = "l"
group_d_table.align["GROUP D"] = "l"
print(group_a_table)
print(group_b_table)
print(group_c_table)
print(group_d_table)

# GENERATING FINALS

quarter_final_matches = []
quarter_final_matches.append([group_a_standing[0][0], group_d_standing[1][0]])
quarter_final_matches.append([group_a_standing[1][0], group_d_standing[0][0]])
quarter_final_matches.append([group_b_standing[0][0], group_c_standing[1][0]])
quarter_final_matches.append([group_b_standing[1][0], group_c_standing[0][0]])

print()
print()
print("QUARTER FINAL RESULTS: ")
print("--------------------")

quarter_winners = []
for match in quarter_final_matches:
    quarter_winners.append(match_system.qualify(match[0], match[1]))

print()
print()
print("HALF FINAL RESULTS: ")
print("--------------------")

half_final_matches = []
half_winners = []
half_final_matches.append([quarter_winners[0], quarter_winners[3]])
half_final_matches.append([quarter_winners[1], quarter_winners[2]])
for match in half_final_matches:
    half_winners.append(match_system.qualify(match[0], match[1]))

print()
print()
print("FINAL RESULT: ")
print("--------------------")

final_match = []
final_match.append([half_winners[0], half_winners[1]])
winner = match_system.qualify(final_match[0][0], final_match[0][1])

print()
print()
print("WINNER: ")
print("--------------------")
print(f"{winner.name} won The Champions League!\n{winner.name}'s statistics are:\nWin: {winner.win}\nLose: {winner.lose}")





