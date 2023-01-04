from django.contrib import admin
from django.urls import include, path

from . import views
from .views import my_profile, invites_received_view, profiles_list_view, invite_profiles_list_view, send_invitation, remove_from_friends, accept_invitation, reject_invitation

app_name = 'louslist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('', include('main.urls')),
    path('login/', views.LoginView.as_view(), name='login'),

    
    #path('', include('main.urls')),
    #path('login', include('main.urls')),   
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('<str:department>', views.DepartmentView.as_view(), name='department'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('myprofile/', my_profile, name='my-profile-view'),
    path('processClass/', views.processClass, name="processClass"),
    path('logout/', views.logout_user, name='logout'),
    path('schedule/', views.ScheduleView, name='schedule'),
    path('my-invites/', invites_received_view , name='my-invites-view'),
    path('all-profiles/', views.ProfileListView.as_view() , name='all-profiles-view'),
    path('to-invite/', invite_profiles_list_view , name='invite-profiles-view'),
    path('send_invite/', send_invitation, name='send-invite'),
    path('remove_friend/', remove_from_friends, name='remove-friend'),
    path('my-invites/accept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
    path('profiles/<str:userid>', views.profilesView, name='profiles'),
    path('schedules/<str:userid>', views.schedulesView, name='schedules'),
    #path('login', include('main.urls')),
    path('addComment/', views.addComment, name="addComment"),
    path('search/', views.searchView, name='search'),
    path('friendSearch/', views.friendSearchView, name='friendSearch'),

]