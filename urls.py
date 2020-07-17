from django.conf.urls import url
from blogapp import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from rest_framework.schemas import get_schema_view

schema_view=get_schema_view(title='pastbin api')

router = DefaultRouter()
router.register(r'employee', views.employeeviewset)
router.register(r'users1', views.UserViewSet)

# The API URLs are now determined automatically by the router.

app_name = 'blogapp'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),

    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/', views.CreatePostView.as_view(), name='create_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePostView.as_view(), name='updatePost'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.DeletePostView.as_view(), name='DeletePost'),
    url(r'^draft/$', views.DraftListView.as_view(), name='post_draft_view'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve', views.approve_comment, name='approve_comments'),
    url(r'^comment/(?P<pk>\d+)/remove', views.remove_comment, name='delete_comment'),
    url(r'^post/(?P<pk>\d+)/publish', views.publish_post, name='post_publish'),
    url(r'^register/$', views.register, name='Register_Here'),
    url(r'^restpost/$', views.PostList.as_view(), name='POST-LIST'),
    url(r'^employeelist/$', views.Employeelist.as_view(), name='employeelist'),
    url(r'^employeedetail/(?P<pk>\d+)$', views.Employeedetail.as_view(), name='employeedetail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('x/',views.api_root),
    path('', include(router.urls)),
    path('schema/',schema_view)

    ]