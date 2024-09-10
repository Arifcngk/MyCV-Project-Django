from django.db import models


class About(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Adınız")
    surname=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Soyadınız")
    work_status=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="İş Statüsü")
    description=models.TextField(max_length=300, blank=True,null=True,default="",verbose_name="Kendinden Bahset")
    updated_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Güncelleme Tarihi")
    created_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Oluşturulma Tarihi")


def __str__(self):
    return f"About Setting {self.name}"


class Meta:
    verbose_name_plural="About Settings"
    verbose_name="About Setting"
    ordering=['name']

    def __str__(self):
        return self.name 


class Skill(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Yetenek Adı")
    percentage=models.IntegerField(default=0,verbose_name="Yüzde")
    proccess_color=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Renk")
    updated_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Güncelleme Tarihi")
    created_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Oluşturulma Tarihi")


def __str__(self):
    return self.name

class Meta:
    verbose_name_plural="Skill Settings"
    verbose_name="Skill Setting"
    ordering=['name']

    def __str__(self):
        return self.name   
    




class Images(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default="", verbose_name="Resim Alanı")
    image = models.ImageField(upload_to="images/", blank=True, null=True, default="", verbose_name="Resim")
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name="Güncelleme Tarihi")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Oluşturulma Tarihi")  # auto_now_add güncellenme tarihi için daha uygun olabilir

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Images Settings"
        verbose_name = "Images Setting"
        ordering = ['name']





class ServicesName(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yetenek")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"
        ordering = ['name']

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    skills = models.ManyToManyField(ServicesName, related_name='services', verbose_name="Yetenekler")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"
        ordering = ['title']
