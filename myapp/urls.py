from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("login/",views.login),
    path("register/",views.register),
    path('addcustomer',views.addreg),
    path('dashboard/',views.dash),
    path('checklog',views.check_login),
    path('forot/',views.forg),
    path('checkupdate',views.forgotpas),
    path('bbb',views.balnc),
    path('adddata',views.amtadd),
    path('withdr',views.withdraw),
    path('send',views.sendmoney),

    
]
