from django.db import models

class User(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
    
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    password = models.CharField(
        max_length=50,
        blank=False,
        null=False,)

    mail = models.EmailField(
        unique=True)
    
    def __str__(self):
        return self.name

class Userdate(models.Model):
    user = models.ForeignKey(
        User,
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