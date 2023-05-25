
def solution(attack, recovery, hp):
    total_damage = attack - recovery
    count = hp/total_damage
    return int(count if count - hp//total_damage == 0 else count + 1)

print(solution(30,10,60))