import urllib.request
import datetime
import json

client_id = 'cKNXupFRnY9nLqMEx_d3'
client_secret = 'YAYjMXNIMY'

def main():
    node = 'news'  # 크롤링 대상
    srcText = input('검색어를 입력하세요: ')
    cnt = 0
    jsonResult = []

    # Naver Search API 호출
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    if not jsonResponse:
        print("API 호출 실패")
        return

    total = jsonResponse.get('total', 0)
    while jsonResponse and jsonResponse.get('display', 0) != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        # 다음 페이지로 이동
        start = jsonResponse.get('start', 1) + jsonResponse.get('display', 0)
        jsonResponse = getNaverSearch(node, srcText, start, 100)

    print('전체 검색 : %d건' % total)

    # JSON 파일로 저장
    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)

    print("가져온 데이터 : %d건" % cnt)
    print('%s_naver_%s.json SAVED' % (srcText, node))


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success" % datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node_path = "%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + "/" + node_path + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
    title = post.get('title', '').replace('<b>', '').replace('</b>', '')  # HTML 태그 제거
    description = post.get('description', '').replace('<b>', '').replace('</b>', '')
    org_link = post.get('originallink', '')
    link = post.get('link', '')

    try:
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        pDate = ''

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })


if __name__ == "__main__":
    main()
