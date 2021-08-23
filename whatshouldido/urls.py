from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'whatshouldido'

urlpatterns = [
    #Main Page
    path('',views.index,name='index'),
    path('auth/logout/', LogoutView.as_view(),name='logout'),
    path('search',views.StudygroupsView.as_view(),name='groupsearch'),
    path('search/<int:pk>',views.join,name='join'),

    #Pop-up
    path('error/',views.error,name='error'),

    #Personal Page
    path('userinfo/',views.userinfo,name='userinfo'),
    path('calendar/',views.calendar,name='calendar'),

    #Group Feature Page
    path('group/<int:pk>/writearticle',views.writearticle, name='writearticle'),
    path('group/<int:pk>',views.groupinfo, name='group'),
    path('test',views.managegroup,name='managegroup'), # How?
    path('group/makegroup/',views.makegroup,name='makegroup'),
]