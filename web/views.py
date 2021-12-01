import json

from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import User_gps
from django.core import serializers


# Create your views here.

@csrf_exempt
def Home_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            jsonObject = json.loads(request.body)
            gps = User_gps()
            gps.username = jsonObject.get('name')
            gps.x = jsonObject.get('x')
            gps.y = jsonObject.get('y')
            gps.timestamp = jsonObject.get('timestamp')
            gps.save()

        user_datas = User_gps.objects.all().filter(username=request.user.username).values().order_by("timestamp")
        user_data = []
        for data in user_datas:
            user_data.append([data['x'], data['y'], data['timestamp']])
        print(user_data)
        return render(request, "home.html", {'user_data': user_data})
    else:
        return render(request,"home.html",{'user_data': [[]]})


class KakaoSignInView(View):
    def get(self, request):
        app_key = 'c3d32ec4bf5aefb7ad5585224c87eb91'
        redirect_uri = 'http://localhost:8000/accounts/kakao/login/callback/'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'

        return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}')
