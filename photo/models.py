from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from tagging.fields import TagField
# Create your models here.

class Photo(models.Model):
    # 외래키 -> 참조키!!! 외래키 설정할 때는 어떤 모델의 주 키를 사용할건지 정해야함 장고 규칙임
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='image')
    #이렇게 동적으로 가져 올 수 있음 (user의 기본 설정은 아이디 비번 이메일 더 이상 하려면 기본을 확장해야함 저건 바뀔 수 있으니까 유저모델이라는 매소드 사용
    #on delete는 유저를 삭제하면 같이 올라간 애들을 어쩔거냐고 물어보는거임
    #cascad는 유저 지우면 포토도 다 지우겠다는 거임
    #related name은 내 페이지에서 내꺼만 뜨게 하려고 쓰는거 나라는 객체.이미지스 하면 내가 올린이미지만 뙇 하고 나옴
    #파이썬에서 사진 쓰려면 pip install pillow (터미널에 이렇게! 해서


    image = models.ImageField(upload_to='images/%Y/%m/%d')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tag = TagField()

    class Meta: #innerclass 옵션 클래스라고 생각해도 갠춘할듯
        ordering = ['-updated'] #최신 업데이트 된 애들부터 데려오겠다! (db옵션 )
        #db에 적용할 변경사항 찾기  python manage.py makemigrations photo
        #해당 변경사항 적용하기     python manage.py migrate photo
    def __str__(self):
        return self.author.username + " "+self.created.strftime("%Y -%m-%d %H :%M:%S")

    def get_absolute_url(self):
        return reverse_lazy('photo:photo_detail', args=[self.id])

#모델의 역할은 디비에 어떻게 할건지 하는고야 두번쨰 쓰는것같은데 그러하다고 한다음에는 터미널에서 migrate

#json 어떻게 제공할지 정해야함


