from django.db import models


class About(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Adınız")
    surname=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Soyadınız")
    work_status=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="İş Statüsü")
    description=models.TextField(max_length=300, blank=True,null=True,default="",verbose_name="Kendinden Bahset")
    updated_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Güncelleme Tarihi")
    created_date=models.DateTimeField(auto_now=True,blank=True,verbose_name="Oluşturulma Tarihi")


    def __str__(self):
        return f"Hakkımda Ayarları {self.name}"
    
    
    class Meta:
        verbose_name_plural="Hakkımda Ayarları"
        verbose_name="Hakkımda Ayarları"
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
        verbose_name_plural="Yetkinlikler Ayarları"
        verbose_name="Yetkinlikler Ayarları"
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
        verbose_name_plural = "Resim Ayarları"
        verbose_name = "Resim Ayarları"
        ordering = ['name']





class ServicesName(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yetenek")
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Yeteneklerim"
        verbose_name = "Yeteneklerim"
        ordering = ['name']

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    skills = models.ManyToManyField(ServicesName, related_name='services', verbose_name="Yetenekler")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yetkinliklerim Detay Alanı"
        verbose_name = "Yetkinliklerim Detay Alanı"
        ordering = ['title']









class Projects(models.Model):

    title = models.CharField(max_length=100, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to="images/", blank=True, null=True, default="", verbose_name="Resim")
    link = models.URLField(verbose_name="Link")
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name="Güncelleme Tarihi")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Oluşturulma Tarihi")  # auto_now_add güncellenme tarihi için daha uygun olabilir

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projelerim"
        verbose_name = "Projelerim"
        ordering = ['title']





class Quotes(models.Model):
    quotes=models.TextField(max_length=300, blank=True,null=True,default="",verbose_name="Alıntılar")
    quotationer=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Alıntı Sahibi")

    def __str__(self):
        return self.quotes
    class Meta:
        verbose_name_plural="Alıntılar"
        verbose_name="Alıntılar"
        ordering=['quotes']
    
        def __str__(self):
            return self.quotes



class Document(models.Model):
    slug=models.SlugField(max_length=50,blank=True,null=True,default="",verbose_name="Slug")
    documant=models.FileField(upload_to="documant/",blank=True,null=True,default="",verbose_name="Döküman")
    link_text=models.CharField(max_length=50,blank=True,null=True,default="",verbose_name="Link Metni")

    def __str__(self):
        return self.slug
    class Meta:
        verbose_name_plural="Dökümanlar"
        verbose_name="Dökümanlar"
        ordering=['slug']
    
        def __str__(self):
            return self.slug