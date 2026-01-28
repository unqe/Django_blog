#!/usr/bin/env python
"""Create Site record for django.contrib.sites"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from django.contrib.sites.models import Site

# Create or update Site with id=1
site, created = Site.objects.get_or_create(
    id=1,
    defaults={
        'domain': 'django-bl0g.herokuapp.com',
        'name': 'Django Blog'
    }
)

if created:
    print(f"✓ Created Site: {site.domain} (id={site.id})")
else:
    # Update existing site
    site.domain = 'django-bl0g.herokuapp.com'
    site.name = 'Django Blog'
    site.save()
    print(f"✓ Updated Site: {site.domain} (id={site.id})")

print(f"\nAll sites in database:")
for s in Site.objects.all():
    print(f"  - id={s.id}, domain={s.domain}, name={s.name}")
