import json
import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud

# Step 1: 데이터 로드
input_file = 'C:/Programing/BigData/5_data/etnews.kr_facebook_2016-01-01_2018-08-01_4차 산업혁명.json'

# JSON 파일 읽기
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: 'message' 키 데이터 추출 및 전처리
message = ''
for item in data:
    if 'message' in item:
        message += re.sub(r'[^\w]', ' ', item['message']) + ' '

# Step 3: 명사 추출
okt = Okt()
nouns = okt.nouns(message)

# Step 4: 단어 빈도 계산
word_count = Counter(nouns)

# 1자 이상의 단어만 필터링
filtered_word_count = {word: count for word, count in word_count.items() if len(word) > 1}

# 상위 10개 키워드 출력
print("상위 10개 키워드:")
for word, count in Counter(filtered_word_count).most_common(10):
    print(f"{word}: {count}")

# Step 5: 히스토그램 생성
font_path = "c:/Windows/fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(12, 6))
plt.bar(filtered_word_count.keys(), filtered_word_count.values(), color='skyblue')
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.title('한글 뉴스 기사 키워드 빈도수')
plt.xticks(rotation=45)
plt.show()

# Step 6: 워드클라우드 생성
wc = WordCloud(font_path=font_path, background_color="ivory", width=800, height=600)
cloud = wc.generate_from_frequencies(filtered_word_count)

plt.figure(figsize=(10, 10))
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
plt.title('한글 뉴스 기사 워드클라우드')
plt.show()
