from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


#url urlpatterns

urlpatterns=[
    path('',views.index, name='index'),
    path('project/post/',views.post,name='post'),
    path('logout/',views.logout,name='logout'),
    path('user/profile/',views.profile,name='profile'),
    path('project/',views.project_detail,name='details'),
    path('search/projects/results/',views.search,name="search"),
    path('api/projects/',views.ProjectList.as_view()),
    path('api/profile/',views.ProfileList.as_view()),
    path('token/', obtain_auth_token),
    path('developer/api/',views.apiView,name='api'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)