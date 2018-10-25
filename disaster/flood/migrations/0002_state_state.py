# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state',
            field=models.CharField(choices=[('andaman', 'Andaman & Nicobar Islands'), ('arunachal', 'Arunachal Pradesh'), ('assam', 'Assam & Meghalaya'), ('nagaland', 'Nagaland, Manipur, Mizoram, Tripura'), ('himlayan', 'Sub Himalayan West Bengal & Sikkim'), ('gangetic', 'Gangetic West Bengal'), ('orissa', 'Orissa'), ('jharkhand', 'Jharkhand'), ('bihar', 'Bihar'), ('eastup', 'East Uttar Pradesh'), ('westup', 'West Uttar Pradesh'), ('uttarakhand', 'Uttarakhand'), ('haryana', 'Haryana, Delhi & Chandigarh'), ('punjab', 'Punjab'), ('hp', 'Himachal Pradesh'), ('jk', 'Jammu & Kashmir'), ('westraj', 'West Rajasthan'), ('eastraj', 'East Rajasthan'), ('westmp', 'West Madhya Pradesh'), ('eastmp', 'East Madhya Pradesh'), ('gujarat', 'Gujarat Region'), ('saurashtra', 'Saurashtra & Kutch'), ('konkan', 'Konkan & Goa'), ('madhyamaharashtra', 'Madhya Maharashttra'), ('matathwada', 'Matathwada'), ('vidarbha', 'Vidarbha'), ('chhattisgarh', 'Chhattisgarh'), ('andhra', 'Coastal Andhra Pradesh'), ('telangana', 'Telangana'), ('rayalseema', 'Rayalseema'), ('tn', 'Tamil Nadu'), ('ckarnataka', 'Coastal Karnataka'), ('nkarnataka', 'North Interior Karnataka'), ('skarnataka', 'South Interior Karnataka'), ('kerala', 'Kerala'), ('lakshadweep', 'Lakshadweep')], default='None', max_length=6),
        ),
    ]
