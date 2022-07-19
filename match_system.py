import random


def match(first_team, second_team):
    first_team_luck_factor = random.uniform(1, 1.3)
    second_team_luck_factor = random.uniform(1, 1.3)
    first_team_goal = int(first_team.power * random.randint(0, 5) * first_team_luck_factor)
    second_team_goal = int(second_team.power * random.randint(0, 5) * second_team_luck_factor)

    if first_team_goal == second_team_goal:
        print(f"{first_team.name} {first_team_goal}  -  {second_team_goal} {second_team.name}")
        first_team.points += 1
        second_team.points += 1
        first_team.tie += 1
        second_team.tie += 1

    elif first_team_goal > second_team_goal:
        print(f"{first_team.name} {first_team_goal}  -  {second_team_goal} {second_team.name}")
        first_team.points += 3
        first_team.win += 1
        second_team.lose += 1
        first_team.average += first_team_goal - second_team_goal
        second_team.average += second_team_goal - first_team_goal

    elif first_team_goal < second_team_goal:
        print(f"{first_team.name} {first_team_goal}  -  {second_team_goal} {second_team.name}")
        second_team.points += 3
        first_team.lose += 1
        second_team.win += 1
        first_team.average += first_team_goal - second_team_goal
        second_team.average += second_team_goal - first_team_goal


def qualify(first_team, second_team):
    first_team_luck_factor = random.uniform(1, 1.3)
    second_team_luck_factor = random.uniform(1, 1.3)
    first_team_goal = int(first_team.power * random.randint(0, 5) * first_team_luck_factor)
    second_team_goal = int(second_team.power * random.randint(0, 5) * second_team_luck_factor)

    if first_team_goal == second_team_goal:
        first_team_penalty_score = 0
        second_team_penalty_score = 0
        for n in range(5):
            first_team_luck_factor = random.randint(3 * int(first_team.power * 10), 100)
            second_team_luck_factor = random.randint(3 * int(second_team.power * 10), 100)
            if first_team_luck_factor > 50:
                first_team_penalty_score += 1
            if second_team_luck_factor > 50:
                second_team_penalty_score += 1

        while first_team_penalty_score == second_team_penalty_score:
            first_team_luck_factor = random.randint(3 * int(first_team.power * 10), 100)
            second_team_luck_factor = random.randint(3 * int(second_team.power * 10), 100)
            if first_team_luck_factor > 50:
                first_team_penalty_score += 1
            if second_team_luck_factor > 50:
                second_team_penalty_score += 1

        if first_team_penalty_score > second_team_penalty_score:
            print(f"{first_team.name} {first_team_penalty_score + first_team_goal} (P)  -  (P) {second_team_penalty_score + second_team_goal} {second_team.name}  (Penalties)")
            first_team.win += 1
            second_team.lose += 1
            return first_team

        elif first_team_penalty_score < second_team_penalty_score:
            print(f"{first_team.name} {first_team_penalty_score + first_team_goal} (P)  -  (P) {second_team_penalty_score + second_team_goal} {second_team.name} (Penalties)")
            first_team.lose += 1
            second_team.win += 1
            return second_team


    elif first_team_goal > second_team_goal:
        print(f"{first_team.name} {first_team_goal}  -  {second_team_goal} {second_team.name}")
        first_team.win += 1
        second_team.lose += 1
        return first_team

    elif first_team_goal < second_team_goal:
        print(f"{first_team.name} {first_team_goal}  -  {second_team_goal} {second_team.name}")
        first_team.lose += 1
        second_team.win += 1
        return second_team
