from django.db import models
from django.utils import timezone

class Product(models.Model):
    GENDER_CHOICES = [
        ('பெண்', 'பெண்'),
        ('ஆண்', 'ஆண்'),
    ]

    PREMATURE_CHOICES = [
        ('26-30','26-30'), 
        ('31-39','31-39'),
        ('39','39'),  
    ]

    parentName = models.CharField(max_length=100, default= "unknown")
    date = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=4, choices=GENDER_CHOICES, default='girl')
    premature = models.CharField(max_length=6, choices=PREMATURE_CHOICES, default='26-30')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    submission_date = models.DateTime   Field(default=timezone.now().date())

class BreastfeedingDetail(models.Model):
    parentName = models.CharField(max_length=100, default="unknown")
    startTime = models.TimeField()
    stopTime = models.TimeField()
    breastSide = models.CharField(max_length=100, choices=[('இடது','இடது'),('வலது','வலது'),('இரண்டும்','இரண்டும்'),('இரண்டும் இல்லை','இரண்டும் இல்லை')], default="unknown")
    supplement = models.CharField(max_length=20, choices=[('தாய்ப்பால்', 'தாய்ப்பால்'), ('பவுடர்பால்', 'பவுடர்பால்')])
    painLevel = models.PositiveIntegerField()
    nippleShape = models.CharField(max_length=100, choices=[('வட்ட வடிவ முலைக்காம்பு', 'வட்ட வடிவ முலைக்காம்பு'), ('கூம்புவடிவ முலைக்காம்பு', 'கூம்புவடிவ முலைக்காம்பு')])
    nippleColor = models.CharField(max_length=100, choices=[('கருப்பு நிறம்', 'கருப்பு நிறம்'), ('வெள்ளை நிறம்', 'வெள்ளை நிறம்'), ('சிவப்பு நிறம்', 'சிவப்பு நிறம்')])
    milkBlister = models.CharField(max_length=50, choices=[('இல்லை','இல்லை'),('ஆம்','ஆம்')])
    nippleCracks = models.CharField(max_length=50, choices=[('இல்லை','இல்லை'),('ஆம்','ஆம்')])
    feelings = models.CharField(max_length=20, choices=[('நிம்மதியாக', 'நிம்மதியாக'), ('மகிழ்ச்சியான உணர்வு', 'Hமகிழ்ச்சியான உணர்வு'), ('சோக உணர்வு', 'சோக உணர்வு'), ('தீர்ந்து போன உணர்வு', 'தீர்ந்து போன உணர்வு'), ('கவலை உணர்வு', 'கவலை உணர்வு')])
    presentWeight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    submission_date = models.DateField(default=timezone.now().date())

    def __str__(self):
        return f'Breastfeed Detail: {self.startTime} - {self.stopTime}'
   
class PoopDetail(models.Model):
    TIME_CHOICES = [
        ('திரவ அமைப்பு', 'திரவ அமைப்பு'),
        ('கடினமான அமைப்பு', 'கடினமான அமைப்பு'),
        ('இரத்தம் கலந்த அமைப்பு', 'இரத்தம் கலந்த அமைப்பு'),
    ]

    time = models.TimeField()
    COLOUR_CHOICES = [
        ('கருப்பு நிற மலம்', 'கருப்பு நிற மலம்'),
        ('சிவப்பு நிற மலம்', 'சிவப்பு நிற மலம்'),
        ('மென்மையான மற்றும் அடர் பச்சை நிற மலம்', 'மென்மையான மற்றும் அடர் பச்சை நிற மலம்'),
        ('மஞ்சள் நிற மலம்', 'மஞ்சள் நிற மலம்'),
    ]
    parentName = models.CharField(max_length=100, default= "unknown")
    timing = models.TimeField(default=timezone.now)
    colour = models.CharField(max_length=50, choices=COLOUR_CHOICES)
    texture = models.CharField(max_length=50, choices=TIME_CHOICES)

    submission_date = models.DateField(default=timezone.now().date())

    def __str__(self):
        return f"Poop Detail - Time: {self.time}, Colour: {self.colour}, Texture: {self.texture}"

class UserInfo(models.Model):
    USER_CHOICES = [
        (False, 'இல்லை'),
        (True, 'ஆம்'),
    ]
    name = models.CharField(max_length=100)   
    parent_name = models.CharField(max_length=100, default="unknown")
    pregnant = models.BooleanField(choices=USER_CHOICES, default=False)
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
