#url들 있을거에여 여기에!

from django.urls import path
from .views import *
app_name = 'photo'

#메인 유알엘에서 여기로 들어 올 수 있게 해야해! ex) 학교문 통과해야 기숙사문을 여는데 우린 지금 기숙사 문만 만든거임
urlpatterns = [
   path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
   path('', PhotoListView.as_view(), name='index'),
   path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
   path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'), #몇번을 수정할지 알려줘야하니까 인트 pk있는게 ㅗㅈㅎ을듯
   path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
   path('tag/<tag>/', TaggedPhotoListView.as_view(), name='tagged_photo_list'),
   path('tag/', TagListView.as_view(), name='tag_list'),


   path('photo/', PhotoList.as_view()),
   path('photo/<int:pk>/', PhotoDetail.as_view()),

]