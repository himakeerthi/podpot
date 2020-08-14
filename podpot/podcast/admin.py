from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(User)
admin.site.register(UserLinks)
admin.site.register(PodcastTags)
admin.site.register(Genre)
admin.site.register(Podcast)
admin.site.register(PodcastGuest)
admin.site.register(PodcastPlaylist)
admin.site.register(UserPreferences)
admin.site.register(UserFavPodcast)
admin.site.register(UserFavPlaylist)
admin.site.register(UserFavGenre)

