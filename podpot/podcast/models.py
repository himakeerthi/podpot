from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



#User related

class Country(models.Model):
    a3 = models.CharField(max_length=2, null=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class State(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Language(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    
    email = models.EmailField(unique=True, blank=True, null=True)
    gender = models.CharField(blank=True, null=True,max_length=1,choices=[('M','MALE'), ('F','FEMALE'), ('O', 'OTHER')])
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True, blank=True)  #country code
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    # country name will be given by ip address while creating a user
    private = models.BooleanField(default=False)
    

class UserLinks(models.Model):
    links = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.links}'

#Podcast related


class PodcastTags(models.Model):
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.keyword}'

class Genre(models.Model):
    name = models.CharField(max_length=100)
    ref_genre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    date_published = models.DateTimeField(auto_now=True, db_index=True)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ForeignKey(PodcastTags, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'{self.name} hosted by {self.host} on {self.date_published}'


class PodcastGuest(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.guest} is a guest of podcast {self.podcast.name}'

class PodcastPlaylist(models.Model):
    name = models.CharField(max_length=100)
    podcast = models.ManyToManyField(Podcast)
    created = models.DateTimeField(auto_now=True,db_index=True)
    tags = models.ForeignKey(PodcastTags, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


#User likings

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'{self.user} likes {self.language}'

class UserFavPodcast(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
   

    def __str__(self):
        return f'{self.user} likes {self.podcast.name}'
    

class UserFavPlaylist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    playlist = models.ForeignKey(PodcastPlaylist,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} likes playlist {self.playlist}'

class UserFavGenre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} likes genre {self.genre.name}'