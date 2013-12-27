from django.db import models
from django.contrib.auth.models import User
import datetime

# lookup Django field types online
# Create your models here.

class Customer(models.Model):
    ALABAMA = 'AL'
    ALASKA = 'AK'
    ARIZONA = 'AZ'
    ARKANSAS = 'AR'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GA'
    HAWAII = 'HI'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    IOWA = 'IA'
    KANSAS = 'KS'
    KENTUCKY = 'KY'
    LOUISIANA = 'LA'
    MAINE = 'ME'
    MARYLAND = 'MD'
    MASSACHUSETTS = 'MA'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSISSIPPI = 'MS'
    MISSOURI = 'MO'
    MONTANA = 'MT'
    NEBRASKA = 'NE'
    NEVADA = 'NV'
    NEWHAMPSHIRE = 'NH'
    NEWJERSEY = 'NJ'
    NEWMEXICO = 'NM'
    NEWYORK = 'NY'
    NORTHCAROLINA = 'NC'
    NORTHDAKOTA = 'ND'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODEISLAND = 'RI'
    SOUTHCAROLINA = 'SC'
    SOUTHDAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VERMONT = 'VT'
    VIRGINA = 'VA'
    WASHINGTON = 'WA'
    WESTVIRGINIA = 'WV'
    WISCONSIN = 'WI'
    WYOMING = 'WY'

    STATE_CHOICES = (
        (ALABAMA, 'Alabama'),
        (ALASKA, 'Alaska'),
        (ARIZONA, 'Arizona'),
        (ARKANSAS, 'Arkansas'),
        (CALIFORNIA, 'California'),
        (COLORADO, 'Colorado'),
        (CONNECTICUT, 'Connecticut'),
        (DELAWARE, 'Delaware'),
        (FLORIDA, 'Florida'),
        (GEORGIA, 'Georgia'),
        (HAWAII, 'Hawaii'),
        (IDAHO, 'Idaho'),
        (ILLINOIS, 'Illinois'),
        (INDIANA, 'Indiana'),
        (IOWA, 'Iowa'),
        (KANSAS, 'Kansas'),
        (KENTUCKY, 'Kentucky'),
        (LOUISIANA, 'Louisiana'),
        (MAINE, 'Maine'),
        (MARYLAND, 'Maryland'),
        (MASSACHUSETTS, 'Massachusetts'),
        (MICHIGAN, 'Michigan'),
        (MINNESOTA, 'Minnesota'),
        (MISSISSIPPI, 'Mississippi'),
        (MISSOURI, 'Missouri'),
        (MONTANA, 'Montana'),
        (NEBRASKA, 'Nebraska'),
        (NEVADA, 'Nevada'),
        (NEWHAMPSHIRE, 'New Hampshire'),
        (NEWJERSEY, 'New Jersey'),
        (NEWMEXICO, 'New Mexico'),
        (NEWYORK, 'New York'),
        (NORTHCAROLINA, 'North Carolina'),
        (NORTHDAKOTA, 'North Dakota'),
        (OHIO, 'Ohio'),
        (OKLAHOMA, 'Oklahoma'),
        (OREGON, 'Oregon'),
        (PENNSYLVANIA, 'Pennsylvania'),
        (RHODEISLAND, 'Rhode Island'),
        (SOUTHCAROLINA, 'South Carolina'),
        (SOUTHDAKOTA, 'South Dakota'),
        (TENNESSEE, 'Tennessee'),
        (TEXAS, 'Texas'),
        (UTAH, 'Utah'),
        (VERMONT, 'Vermont'),
        (VIRGINA, 'Virgina'),
        (WASHINGTON, 'Washington'),
        (WESTVIRGINIA, 'West Virgina'),
        (WISCONSIN, 'Wisconsin'),
        (WYOMING, 'Wyoming')
    )

    user = models.OneToOneField(User)
    address = models.CharField(max_length=50, default="", null=True)
    city = models.CharField(max_length=60, default="", null=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default="MI", null=True)
    country = models.CharField(max_length=50, default="United States", null=True)
    zipcode = models.PositiveIntegerField(default=0, null=True)
    phnumber = models.CharField(max_length=15, default="")

    def __unicode__(self):
        return '%s' % (self.user)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['user']


#tablename_id(primary key)






