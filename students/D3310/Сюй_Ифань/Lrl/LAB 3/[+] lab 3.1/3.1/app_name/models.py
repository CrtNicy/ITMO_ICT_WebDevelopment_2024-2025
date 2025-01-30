from django.db import models

class Avtovladelec(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя владельца")

    def __str__(self):
        return self.name

class Udoverenie(models.Model):
    avtovladelec = models.OneToOneField(Avtovladelec, on_delete=models.CASCADE, related_name="udoverenie")
    date_issued = models.DateField(verbose_name="Дата выдачи удостоверения")

    def __str__(self):
        return f"Удостоверение {self.avtovladelec.name}"

class Avto(models.Model):
    marka = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель автомобиля")
    color = models.CharField(max_length=50, verbose_name="Цвет автомобиля")

    def __str__(self):
        return f"{self.marka} {self.model}"

class Vladenie(models.Model):
    avtovladelec = models.ForeignKey(Avtovladelec, on_delete=models.CASCADE, related_name="vladenie_avto")
    avto = models.ForeignKey(Avto, on_delete=models.CASCADE, related_name="vladenie_avtovladelec")
    year = models.IntegerField(verbose_name="Год владения")

    def __str__(self):
        return f"{self.avtovladelec.name} владеет {self.avto.marka} {self.avto.model} с {self.year} года"
