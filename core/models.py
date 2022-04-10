from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name  
class Startup(models.Model):
    email=models.EmailField(max_length=200,null=True,blank=True)
    owner=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    use_of_funds=models.TextField(null=True, blank=True)
    problem=models.TextField(null=True, blank=True)
    solution=models.TextField(null=True, blank=True)
    edge=models.TextField(null=True, blank=True)
    RModel=models.TextField(null=True, blank=True)
    name=models.CharField(max_length=100)
    equity=models.FloatField(null=True, blank=True)
    investment=models.FloatField(null=True, blank=True)
    valuation=models.FloatField(null=True, blank=True)
    pfy=models.CharField(max_length=100,null=True, blank=True)
    revenue_pfy=models.FloatField(null=True, blank=True)
    revenue_total=models.FloatField(null=True, blank=True)
    profit_pfy=models.FloatField(null=True, blank=True)
    profit_total=models.FloatField(null=True, blank=True)
    short_term_debt=models.FloatField(null=True, blank=True)
    net_margin=models.FloatField(null=True, blank=True)
    gross_margin=models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    team=models.TextField(null=True, blank=True)
    teamimage=models.ImageField(upload_to='images', blank=True)
    edge=models.TextField(null=True, blank=True)
    site=models.URLField(null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name    
class Teammember(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100, null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    link=models.URLField(null=True, blank=True)
    company = models.ForeignKey(to=Startup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(upload_to='images', blank=True)    
    name=models.CharField(max_length=100, null=True)
    mob=models.IntegerField(null=True)
    typee=models.CharField(max_length=100, null=True)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



