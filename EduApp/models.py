from datetime import datetime
from django.db import models
from django.db.models.fields import CharField, TextField

#! TODO:
# ?*  regions
# ?*  schools
# ?*  courses
# ?*  groups
# ?*  teachers
# ?*  clients
# ?*  parents
# ?  tests
# ?*  lessons
# ?*  attentions


# * regions

class regions(models.Model):

    region_name_choose = (
        ('tashkent',    "Toshkent"),
        ('karklp',      "Qoraqalpog’iston Respublikasi"),
        ('andijan',     "Andijon viloyati"),
        ('bukhara',     "Buxoro viloyati"),
        ('jizzax',      "Jizzax viloyati"),
        ('qarsh',       "Qashqadaryo viloyati"),
        ('navoi',       "Navoiy viloyati"),
        ('namagan',     "Namangan viloyati"),
        ('samarkand',   "Samarqand viloyati"),
        ('surxandar',   "Surxondaryo viloyati"),
        ('sirdar',      "Sirdaryo viloyati"),
        ('tash_obl',    "Toshkent viloyati"),
        ('fergana',     "Farg’ona viloyati"),
        ('xorezm',      "Xorazm viloyati")
    )

    region_name = models.CharField(
        'Viloyatni tanglang', max_length=255, choices=region_name_choose)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = 'Vilayat'
        verbose_name_plural = '#0 Vilayatlar'


# * schools

class schools(models.Model):

    region_id = models.ForeignKey(regions, on_delete=models.CASCADE,
                                  null=False, blank=True, verbose_name='Viloyatni tanglang')
    school_name = models.CharField('Uquv markaz moni', max_length=50)
    address = models.CharField('Adresini kititing', max_length=100)
    director = models.CharField('Direktor FIO :', max_length=100)
    longitude = models.CharField(
        'Geologicheskiy uzunlik', max_length=255, blank=True)
    latitude = models.CharField(
        'Geologicheskiy kenglik', max_length=255, blank=True)

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'Uquv markaz'
        verbose_name_plural = '#1 Uquv markazlar'


# * courses

class courses(models.Model):

    school_name_id = models.ForeignKey(
        schools, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Uquv markaz nomi")
    cours_name = models.CharField('Kurs nomi', max_length=255)
    dic = models.TextField('Kurs xaqida')
    prise = models.BigIntegerField('Kurs narxi', max_length=6)

    def __str__(self):
        return str(self.school_name_id) + ' ' + str(self.cours_name) + ' ' + str(self.prise)

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = '#2 Kurslar'


# * groups

class groups(models.Model):

    courses_id = models.ForeignKey(
        courses, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Qaysi kursni grupasi")
    group_name = models.CharField('Grupani nomi', max_length=100)
    group_start = models.DateTimeField(
        'Grupa darsga kelish vaqti', help_text="Ota-onalar bilishi uchun")
    group_end = models.DateTimeField('Grupa darsdan ketishi')

    def __str__(self):
        return str(self.group_name)

    class Meta:
        verbose_name = 'Grupa'
        verbose_name_plural = '#3 Grupalar'


# * teachers

class teachers(models.Model):

    groups_id = models.ForeignKey(groups, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Qaysi kursni ustozi")
    teacher_fio = models.CharField('FIO', max_length=255, unique=True)
    skill = models.CharField('Qobiliyati', max_length=255)
    mobile = models.CharField('Telefon raqam', max_length=13, unique=True)
    email = models.EmailField('Email', max_length=255)
    telegram = models.CharField('Telegram', max_length=255)
    linkedin = models.CharField('Linkedin', max_length=255, blank=True)
    github = models.CharField('Github ', max_length=255, blank=True)

    def __str__(self):
        return str(self.groups_id) + ' ' + str(self.teacher_fio)

    class Meta:
        verbose_name = 'Ustoz'
        verbose_name_plural = '#4 Ustozlar'


# * clients

class clients(models.Model):

    groups_clients_id = models.ForeignKey(
        groups, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Qaysi kursni uquvchisi")
    user_name = models.CharField('Uquvchini FIO', max_length=150, unique=True)
    contc = models.CharField('Telefon raqam', max_length=13)
    id_cart_seria = models.CharField('Pasport seriasi', max_length=2, unique=True)
    id_cart_num = models.BigIntegerField('Pasport seriasi', max_length=7, unique=True)
    address = models.CharField('Adresini kititing', max_length=100)
    password = models.CharField('Parol', max_length=255, null=True)

    def __str__(self):
        return str(self.groups_clients_id) + ' ' + str(self.user_name) + ' ' + str(self.contc)

    class Meta:
        verbose_name = 'Uquvchi'
        verbose_name_plural = '#5 Uquvchilar'


# * parents

class parents(models.Model):

    clients_id = models.ForeignKey(clients, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kimni ota-onasi")
    parent_name = models.CharField('Otasini FIO', max_length=150, blank=True, unique=True) #! delete black
    phone = models.CharField('Telefon raqam', max_length=13, unique=True)
    address = models.CharField('Adresini kititing', max_length=100)
    password = models.CharField('Parol', max_length=255, null=True)

    def __str__(self):
        return str(self.clients_id) + ' ' + str(self.parent_name) + ' ' + str(self.phone)

    class Meta:
        verbose_name = 'Ota-ona'
        verbose_name_plural = '#6 Ota-onalar'


# * lessons

class lessons(models.Model):

    groups_les_id = models.ForeignKey(groups, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Qaysi grupaga dars buladi")
    les_theme = models.CharField('Dars mavzusi', max_length=100)
    les_date = models.DateField('Dars kuni', default=datetime.today)
    les_start = models.TimeField('Dars boshlanish vaqti')
    les_end = models.TimeField('Dars tugashi vaqti')

    def __str__(self):
        return str(self.les_theme) + ' ' + str(self.les_date) + ' ' + str(self.les_start)

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = '#7 Darslar'


# * attentions

class attentions(models.Model):

    lesson_atten_id = models.ForeignKey(
        lessons, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Qaysi dars")
    clients_atten_id = models.ForeignKey(
        clients, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Uquvchi ismi")
    date_atten = models.DateField('Dars kuni', default=datetime.today)

    def __str__(self):
        return 'Shu ' + str(self.date_atten) + ' kuni ' + str(self.clients_atten_id) + ' darsda bolmadi'

    class Meta:
        verbose_name = 'Monitoring'
        verbose_name_plural = '#8 Monitoringlar'


class tests(models.Model):

    group = models.ForeignKey(groups, on_delete=models.CASCADE, verbose_name="Qaysi grupani testi")
    question = models.TextField('Savolni kriting')
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    true = models.IntegerField('Tugri javobni IDsini kiting')

    def __str__(self):
        return str(self.group) + ' ' + str(self.question) + ' ' + str(self.true)

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = '#9 Testlar'
