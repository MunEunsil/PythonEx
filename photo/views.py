from django.shortcuts import render
from .models import Photo
# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  django.contrib.auth.mixins import LoginRequiredMixin
#믹스인,데코레이터 : 접근 권한 제어, 뷰를 실행하기에 앞서 특별한 기능을 붙이는 역할을 함
#믹스인-> 클래스형 뷰
#데코레이터->함수형 뷰

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/list.html'



class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect



class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form): #세이브 전 폼 정보가 올바른지
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/update.html'
    # success_url = '/' 보통은 이렇게 완료하면 시작페이지로! ㅎ ㅏ지만 우린 모델을 만질거랍니닷!

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = '/'

from tagging.views import TaggedObjectList

class TaggedPhotoListView(TaggedObjectList):
    model = Photo
    template_name = 'photo/tagged_photo_list.html'

from django.views.generic import TemplateView

class TagListView(TemplateView):
    template_name = 'photo/tag_list.html'

#API view
from rest_framework import generics
from .serializers import PhotoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

#추가하기가 되도록 하기 위함
class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    authentication_classes = (TokenAuthentication, ) #로그인을 어떤 방식을 제공할거임? 토큰방식으로할거임!
    permission_classes = (IsAuthenticated, IsAuthenticated)# 로그인을 한 사람만 쓸 수 있게 하겠다



