import json
import random
def set_my_vocabulary():
  '''
  자신의 단어장이 없으면 만들고 단어장에 20개의 새로운 단어를 추가합니다.
  '''
  my_account_voca = {
    'vocabulary':[]
  }

  #단어장 난이도 조정
  voca_class = "N1"
  #한번에 불러오는 단어의 갯수
  voca_number = 20

  output_file = "my_vocabulary.json"

  try:
      with open(output_file, "r", encoding="utf-8") as f:
          my_voca_data = json.load(f)
  except FileNotFoundError:
      # 파일이 존재하지 않을 경우 기본 형태로 초기화
      my_voca_data = my_account_voca

  try:
      with open("vocabulary.json", "r", encoding="utf-8") as f:
          voca_data = json.load(f)
  except FileNotFoundError:
      # 파일이 존재하지 않을 경우
      print("단어장이 존재하지 않습니다. 단어장의 경로를 확인해주세요.")

  voca_size = len(voca_data[voca_class])
    
  for _ in range(voca_number):
    idx = random.randint(0, voca_size)
    # 중복 선정 방지 코드
    while voca_data[voca_class][idx] in my_voca_data["vocabulary"]: idx = random.randint(0, voca_size)
    my_voca_data["vocabulary"].append(voca_data[voca_class][idx])

  # my_vocabulary 초기화
  with open(output_file, "w", encoding="utf-8") as f:
      json.dump(my_voca_data, f, indent=2, ensure_ascii=False)

def read_my_voca():
  output_file = "my_vocabulary.json"
  try:
      with open(output_file, "r", encoding="utf-8") as f:
          return json.load(f)
  except FileNotFoundError:
    # 파일이 존재하지 않을 경우 기본 형태로 초기화
    set_my_vocabulary()
    f = open(output_file, "r", encoding="utf-8")
    return json.load(f)