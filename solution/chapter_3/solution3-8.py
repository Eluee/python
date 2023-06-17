
# 각 프로그램간의 교집합들의 합집합 = 2개 이상 켜져있던 시간 

def solution(programs):
  program_list = [set(range(program[0], program[1])) for program in programs]
  inter_program = [program_list[i] & program_list[j]  for i in range(3) for j in range(i + 1,3)]
  return len(inter_program[0] | inter_program[1] | inter_program[2])

print(solution([[1, 6], [3, 5], [2, 8]]))

