from django.db import migrations
from django.contrib.auth.models import User

def create_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')  # Use this method to get the User model
    User.objects.create(username='user1', email='user1@example.com')
    User.objects.create(username='user2', email='user2@example.com')

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # Depends on the last migration of the auth app
    ]

    operations = [
        migrations.RunPython(create_users, migrations.RunPython.noop),
    ]