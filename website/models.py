from re import A
from django.db import models
from django.conf import settings
from django.utils import timezone

class Userdate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    height = models.FloatField(
        blank=False,
        null=False)

    weight = models.FloatField(
        blank=False,
        null=False)
    
    created_date = models.DateTimeField(default=timezone.now)

    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.weight) + '/' + str(self.height)

    @property
    def bmi(self):
        calculation = self.weight / (self.height / 100)**2
        ans = round(calculation, 1)

        if ans > 40:
            comment = "めちゃくちゃデブやで！"
        elif ans > 30:
            comment = "デブ！"
        elif ans > 25:
            comment = "ちょっと太り気味よ"
        elif ans > 18.5:
            comment = "ナイススタイル！！　その状態を維持して！！"            
        elif ans > 16:
            comment = "スレンダーだね"
        else:
            comment = "痩せすぎよ！"

        return [str(ans), str(comment)]



    # userdate.user = User.objects.first()
    # userdate.user = User.objects.get(pk=4)
    # https://qiita.com/uenosy/items/54136aff0f6373957d22 テーブル同士の連結にはまった。参考サイトはここ