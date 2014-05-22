from django.db import models
from geopy import geocoders

class Entry(models.Model):

    added_by = models.CharField(max_length = 10)
    added_date = models.DateField(auto_now=False, auto_now_add = True)
    venue_type = models.BooleanField()
    venue_name = models.CharField(max_length = 50)
    street_address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 5)
    lng = models.DecimalField(decimal_places = 10, max_digits = 13, blank = True)
    lat = models.DecimalField(decimal_places = 10, max_digits = 13, blank = True)
    geo_address = models.CharField(max_length = 100, blank = True)
    score = models.IntegerField(default=0)
    
    def save(self, force_insert=False):
        location = "%s %s %s %s" % (self.street_address, self.city, self.state, self.zipcode)
        g = geocoders.GoogleV3()

        if not self.lat or not self.lng or not self.geo_address:
            geo_address, (lat, lng) = g.geocode("%s" %(location))
            self.lat = lat
            self.lng = lng
            self.geo_address = geo_address
        
        super(Entry, self).save()
        
    def __unicode__(self):
        return self.venue_name