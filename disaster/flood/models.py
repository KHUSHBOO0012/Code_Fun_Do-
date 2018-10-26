from django.db import models

# Create your models here.
STATE_CHOICES= [
    ('andaman', 'ANDAMAN & NICOBAR ISLANDS'),
    ('arunachal', 'ARUNACHAL PRADESH'),
    ('assam', 'ASSAM & MEGHALAYA'),
    ('nagaland', 'NAGA MANI MIZO TRIPURA'),
    ('himlayan', 'SUB HIMALAYAN WEST BENGAL & SIKKIM'),
    ('gangetic', 'GANGETIC WEST BENGAL'),
    ('orissa', 'ORISSA'),
    ('jharkhand', 'JHARKHAND'),
    ('BIHAR', 'BIHAR'),
    ('eastup', 'EAST UTTAR PRADESH'),
    ('westup', 'WEST UTTAR PRADESH'),
    ('uttarakhand', 'UTTARAKHAND'),
    ('haryana', 'HARYANA DELHI & CHANDIGARH'),
    ('punjab', 'PUNJAB'),
    ('hp', 'HIMALACHAL PRADESH'),
    ('jk', 'JAMMU & KASHMIR'),
    ('westraj', 'WEST RAJASTHAN'),
    ('eastraj', 'EAST RAJASTHAN'),
    ('westmp', 'WEST MADHYA PRADESH'),
    ('eastmp', 'EAST MADHYA PRADESH'),
    ('gujarat', 'GUJARAT REGION'),
    ('saurashtra', 'SAURASHTRA & KUTCH'),
    ('konkan', 'KONKAN & GOA'),
    ('madhyamaharashtra', 'MADHYA MAHARASHTRA'),
    ('matathwada', 'MATATHWADA'),
    ('vidarbha', 'VIDARBHA'),
    ('chhattisgarh', 'CHHATTISGARH'),
    ('andhra', 'COASTAL ANDHRA PRADESH'),
    ('telangana', 'TELANGANA'),
    ('rayalseema', 'RAYALSEEMA'),
    ('tn', 'TAMIL NADU'),
    ('ckarnataka', 'COASTAL KARNATAKA'),
    ('nkarnataka', 'NORTH INTERIOR KARNATAKA'),
    ('skarnataka', 'SOUTH INTERIOR KARNATAKA'),
    ('kerala', 'KERALA'),
    ('lakshadweep', 'LAKSHADWEEP'),

    ]
class State(models.Model):
    rainfall = models.CharField(max_length=10)
    warning = models.TextField(max_length=1000)
    state = models.CharField(max_length=6, choices=STATE_CHOICES)


