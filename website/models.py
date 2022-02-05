from django.db import models
from django.conf import settings

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

    def __str__(self):
        return str(self.weight) + '/' + str(self.height)

    @property
    def bmi(self):
        calculation = self.weight / (self.height / 100)**2
        ans = round(calculation, 1)
        return str(ans)

    # userdate.user = User.objects.first()
    # userdate.user = User.objects.get(pk=4)
    # https://qiita.com/uenosy/items/54136aff0f6373957d22 テーブル同士の連結にはまった。参考サイトはここ