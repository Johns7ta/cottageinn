from django.db import models
from django.contrib.auth.models import User
import datetime

# lookup Django field types online
# Create your models here.
class Person(models.Model):
    EMPLOYEE = 'e'
    MEMBER = 'm'

    PERSONTYPE_CHOICES = (
        (EMPLOYEE, 'Employee'),
        (MEMBER, 'Member'),
    )

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
    birth_date = models.DateField('birth date', default="", null=True)
    persontype = models.CharField(max_length=1, choices=PERSONTYPE_CHOICES, default=MEMBER)

    def __unicode__(self):
        return '%s' % (self.user)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['user']


class Member(models.Model):
    memberid = models.ForeignKey(Person)
    order = models.ManyToManyField("Order", null=True)

    def __unicode__(self):
        return '%s' % (self.memberid)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ['memberid',]


class Order(models.Model):
    WHITEONE = 'White 1'
    WHITETWO = 'White 2'
    WHITETHREE = 'White 3'
    WHITEFOUR = 'White 4'
    WHITEFIVE = 'White 5'
    WHITESIX = 'White 6'
    WHITESEVEN = 'White 7'
    WHITEEIGHT = 'White 8'
    WHITENINE = 'White 9'
    BLUEONE = 'Blue 1'
    BLUETWO = 'Blue 2'
    BLUETHREE = 'Blue 3'
    BLUEFOUR = 'Blue 4'
    BLUEFIVE = 'Blue 5'
    BLUESIX = 'Blue 6'
    BLUESEVEN = 'Blue 7'
    BLUEEIGHT = 'Blue 8'
    BLUENINE = 'Blue 9'
    REDTEN = 'Red 10'
    REDELEVEN = 'Red 11'
    REDTWELVE = 'Red 12'
    REDTHIRTEEN = 'Red 13'
    REDFOURTEEN = 'Red 14'
    REDFIFTEEN = 'Red 15'
    REDSIXTEEN = 'Red 16'
    REDSEVENTEEN = 'Red 17'
    REDEIGHTEEN = 'Red 18'
    HOLENUM_CHOICES = (
        (WHITEONE, 'White Hole 1'),
        (WHITETWO, 'White Hole 2'),
        (WHITETHREE, 'White Hole 3'),
        (WHITEFOUR, 'White Hole 4'),
        (WHITEFIVE, 'White Hole 5'),
        (WHITESIX, 'White Hole 6'),
        (WHITESEVEN, 'White Hole 7'),
        (WHITEEIGHT, 'White Hole 8'),
        (WHITENINE, 'White Hole 9'),
        (BLUEONE, 'Blue Hole 1'),
        (BLUETWO, 'Blue Hole 2'),
        (BLUETHREE, 'Blue Hole 3'),
        (BLUEFOUR, 'Blue Hole 4'),
        (BLUEFIVE, 'Blue Hole 5'),
        (BLUESIX, 'Blue Hole 6'),
        (BLUESEVEN, 'Blue Hole 7'),
        (BLUEEIGHT, 'Blue Hole 8'),
        (BLUENINE, 'Blue Hole 9'),
        (REDTEN, 'Red Hole 10'),
        (REDELEVEN, 'Red Hole 11'),
        (REDTWELVE, 'Red Hole 12'),
        (REDTHIRTEEN, 'Red Hole 13'),
        (REDFOURTEEN, 'Red Hole 14'),
        (REDFIFTEEN, 'Red Hole 15'),
        (REDSIXTEEN, 'Red Hole 16'),
        (REDSEVENTEEN, 'Red Hole 17'),
        (REDEIGHTEEN, 'Red Hole 18'),
    )


    orderdate = models.DateTimeField(auto_now_add = True, default=datetime.datetime.now)
    comments = models.CharField(max_length=70, default="", null=True)
    course = models.CharField(max_length=20, default="White Course")
    holenum = models.PositiveIntegerField(max_length=2, default=1)
    paymenttype = models.CharField(max_length=30, default="", null=True, blank=True)
    amount = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.00)
    buyer = models.ForeignKey(User)
    is_closed = models.DateTimeField("is_closed", default=None, blank=True, null=True)

    def __unicode__(self):
        return '%d' % (self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['orderdate', 'holenum']

class OrderItem(models.Model):
    itemid = models.ForeignKey("Item")
    qty = models.PositiveIntegerField(default=0)
    orderid = models.ForeignKey("Order")

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


class ItemList(models.Model):
    categoryid = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length = 50, default="")

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Item List'
        verbose_name_plural = 'Items List'
        ordering = ['name', 'categoryid']

class Item(models.Model):
    sku = models.CharField(max_length=200, null=True, blank=True, default="")
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.00)
    #active = models.BooleanField(default=True)
    name = models.CharField(max_length = 50, default="")
    itemcat = models.ForeignKey("ItemCategory")
    photo = models.ImageField(upload_to = 'itemphotos')
    #need to download Python PIL imaging system to use ImageField

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['name', 'price']

class ItemCategory(models.Model):
    name = models.CharField(max_length = 50, default="")
    active = models.BooleanField(default = True)
    description = models.CharField(max_length = 100, default="")
    photo = models.ImageField(upload_to = 'itemphotos')

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name',]

#tablename_id(primary key)






