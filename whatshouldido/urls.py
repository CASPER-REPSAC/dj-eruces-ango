from django.urls import path
from . import views

app_name = 'whatshouldido'

urlpatterns = [
    #Main Page
    path('',views.index,name='index'),
    path('error/',views.error,name='error'),
    path('signup/',views.signup, name='signup'), #for social login
    path('logout/',views.logout, name='logout'),
    path('start/',views.main,name='main'),
    path('asdf/',views.calendardetail,name='calendardetail'),
    path('',views.groupsearch,name='groupsearch'),

    #Personal Page
    path('userinfo/',views.userinfo,name='userinfo'),

    #Group Feature Page
    path('group/<int:pk>/writearticle',views.writearticle, name='writearticle'),
    path('group/<int:pk>',views.groupinfo, name='group'),
    path('/test',views.managegroup,name='managegroup'), # How?
    path('group/makegroup/',views.makegroup,name='makegroup'),
]