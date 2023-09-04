import json

# 기본 형태의 JSON 파일
default_data = {
  "N1": [],
  "N2": [],
  "N3": [],
  "N4": [],
  "N5": []
}

output_file = "vocabulary.json"

try:
    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    # 파일이 존재하지 않을 경우 기본 형태로 초기화
    data = default_data

with open('vocabulary.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

print(len(lines))
for idx, line in enumerate(lines):
    line = line.strip()
    parts = line.split("[")

    # Kanji 추출
    kanji = parts[1].split("]")[0] if "[" in line else "None"

    # Onyomi 추출
    Onyomi = parts[0] if "[" in line else line.split("N")[0]
        
    # class 추출
    class_info = line.split(",")[0][-2:].strip()

    # mean 추출
    mean = line.split(",")[1].strip()


    # JSON에 삽입
    if class_info in data:
        data[class_info].append({
            "Onyomi": Onyomi,
            "Kanji": kanji,
            "mean": mean
        })

    #print("한자: {}\n의미: {}\n레벨: {}\n온요미: {}\nindex:{}\n-----------------\n".format(kanji,mean,class_info,Onyomi,idx))
    #print(kanji, class_info, mean, parts[0])

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


