from django.db import models

# Create your models here.
STATE_CHOICES = [
    ('andaman', 'Andaman & Nicobar Islands'),
    ('arunachal', 'Arunachal Pradesh'),
    ('assam', 'Assam & Meghalaya'),
    ('nagaland', 'Nagaland, Manipur, Mizoram, Tripura'),
    ('himlayan', 'Sub Himalayan West Bengal & Sikkim'),
    ('gangetic', 'Gangetic West Bengal'),
    ('orissa', 'Orissa'),
    ('jharkhand', 'Jharkhand'),
    ('bihar', 'Bihar'),
    ('eastup', 'East Uttar Pradesh'),
    ('westup', 'West Uttar Pradesh'),
    ('uttarakhand', 'Uttarakhand'),
    ('haryana', 'Haryana, Delhi & Chandigarh'),
    ('punjab', 'Punjab'),
    ('hp', 'Himachal Pradesh'),
    ('jk', 'Jammu & Kashmir'),
    ('westraj', 'West Rajasthan'),
    ('eastraj', 'East Rajasthan'),
    ('westmp', 'West Madhya Pradesh'),
    ('eastmp', 'East Madhya Pradesh'),
    ('gujarat', 'Gujarat Region'),
    ('saurashtra', 'Saurashtra & Kutch'),
    ('konkan', 'Konkan & Goa'),
    ('madhyamaharashtra', 'Madhya Maharashttra'),
    ('matathwada', 'Matathwada'),
    ('vidarbha', 'Vidarbha'),
    ('chhattisgarh', 'Chhattisgarh'),
    ('andhra', 'Coastal Andhra Pradesh'),
    ('telangana', 'Telangana'),
    ('rayalseema', 'Rayalseema'),
    ('tn', 'Tamil Nadu'),
    ('ckarnataka', 'Coastal Karnataka'),
    ('nkarnataka', 'North Interior Karnataka'),
    ('skarnataka', 'South Interior Karnataka'),
    ('kerala', 'Kerala'),
    ('lakshadweep', 'Lakshadweep'),

    ]
class State(models.Model):
    rainfall = models.CharField(max_length=10)
    warning = models.TextField(max_length=1000)
    state = models.CharField(max_length=6, choices=STATE_CHOICES)


