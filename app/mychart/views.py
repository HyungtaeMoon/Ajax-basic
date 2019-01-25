from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_comic_info


def index(request):
    return render(request, 'mychart/index.html')


# def data_json(request):
#     comic = get_comic_info(183559, '신의 탑')
#     return JsonResponse({
#         'labels': [ep['title'] for ep in comic['ep_list']],
#         'datasets': [{
#             'label': '평점',
#             'backgroundColor': 'rgba(255, 99, 132, 0.5)',
#             'borderColor': 'rgba(255, 99, 132, 1)',
#             'pointBackgroundColor': 'rgba(255, 99, 132, 1)',
#             'pointBorderColor': '#fff',
#             'data': [ep['rating'] for ep in comic['ep_list']],
#         }],
#     })
class WebtoonChartJSONView(BaseLineChartView):
    def __init__(self):
        super().__init__()
        self.comic = get_comic_info(183559, '신의 탑')

    def get_labels(self):
        # x 축에 반환하는 episode 갯수
        return [ep['title'] for ep in self.comic['ep_list']]

    def get_providers(self):
        # datasets 의 이름
        #   차트의 데이터 제목
        return ['평점']

    def get_data(self):
        # return 되는 실제 데이터
        #   [[ep['rating], [ep['rating']] 처럼 2개의 리스트를
        #   중복으로 가져서 처리
        return [
            [ep['rating'] for ep in self.comic['ep_list']],
        ]

    def get_colors(self):
        yield (255, 99, 132)


data_json = WebtoonChartJSONView.as_view()
