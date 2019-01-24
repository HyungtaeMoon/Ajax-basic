import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_comic_info(comic_id, comic_title):
    ep_list = []
    for page in range(1, 6):    # 최대 5페이지
        params = {
            'titleId': comic_id,
            'page': page,
        }
        resp = requests.get('http://comic.naver.com/webtoon/list.nhn', params=params)
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        for tr in soup.select('#content table tr'):
            try:
                link = tr.select('.title a[href*=detail]')[0]
                rating = tr.select('.rating_type strong')[0].text
                date = tr.select('.num')[0].text
            # try 문에서 요소 선택이 잘못되었을 경우에 대한 예외처리로
            #   하나의 태그 요소라도 없는 태그 요소를 선택하면 ep_list 에 빈 리스트가 return 됨
            except IndexError:
                continue

            # a tag 에서 에피소드를 추출하여 text 로 변환
            #   ex) 330화
            title = link.text
            # urljoin() 을 사용하여 url 주소를 연결
            #   url = resp.request.url + link['href']
            url = urljoin(resp.request.url, link['href'])

            ep = {
                'title': title,
                'url': url,
                'rating': rating,
                'date': date,
            }
            # 새로 들어오는 ep 가 ep_list 안에 있다면
            #   return 을 이용하여 ep 를 날림
            if ep in ep_list:
                return ep_list

            ep_list.append(ep)

    return {
        'title': comic_title,
        'ep_list': ep_list,
    }
