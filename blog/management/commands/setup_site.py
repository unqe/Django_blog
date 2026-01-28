from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Creates or updates Site record for django.contrib.sites'

    def handle(self, *args, **options):
        site, created = Site.objects.get_or_create(
            id=1,
            defaults={
                'domain': 'django-bl0g.herokuapp.com',
                'name': 'Django Blog'
            }
        )
        
        if not created:
            # Update existing site
            site.domain = 'django-bl0g.herokuapp.com'
            site.name = 'Django Blog'
            site.save()
            self.stdout.write(
                self.style.SUCCESS(f'Updated Site: {site.domain} (id={site.id})')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Created Site: {site.domain} (id={site.id})')
            )
        
        # Show all sites
        self.stdout.write('\nAll sites in database:')
        for s in Site.objects.all():
            self.stdout.write(f'  - id={s.id}, domain={s.domain}, name={s.name}')
