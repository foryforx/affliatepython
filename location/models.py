from __future__ import unicode_literals

from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles
# Create your models here.
"""
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
"""
class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(blank=False,max_digits=19, decimal_places=10)
    latitude = models.DecimalField(blank=False,max_digits=19, decimal_places=10)
    class Meta:
        ordering = ('created','longitude','latitude')
    def __str__(self):
        return self.longitude + self.latitude 
