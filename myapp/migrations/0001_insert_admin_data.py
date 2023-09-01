from django.db import migrations
from django.contrib.auth.hashers import make_password

def insert_admin_data(apps, schema_editor):
    Administrator = apps.get_model('myapp', 'Administrator')
    Administrator.objects.create(username='Kasasa Trevor', password=make_password('Kasasa@2022'), remember_token='your_token')

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', ''),
    ]

    operations = [
        migrations.RunPython(insert_admin_data),
    ]
