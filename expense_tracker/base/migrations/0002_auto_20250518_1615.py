from django.db import migrations

def create_initial_categories(apps, _):
    Category = apps.get_model('base', 'Categories')
    initial = [
    ("Pets", "Pets"),
    ("Bills", "Bills"),
    ("Travel", "Travel"),
    ("Apartment", "Apartment"),
    ("Shopping", "Shopping"),
    ("Gym", "Gym"),
    ("Date", "Date"),
    ("Extra", "Extra"),
    ("Saving", "Saving"),
    ]
    for key, _ in initial:
        Category.objects.create(name=key, amount=0)

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
