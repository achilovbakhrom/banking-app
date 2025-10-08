from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core_apps.user_profile.models import Profile

User = get_user_model()


class Command(BaseCommand):
    help = "Create profiles for users who don't have one"

    def handle(self, *args, **options):
        users_without_profile = []

        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                users_without_profile.append(user)

        if not users_without_profile:
            self.stdout.write(
                self.style.SUCCESS("All users already have profiles")
            )
            return

        created_count = 0
        for user in users_without_profile:
            Profile.objects.create(user=user)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created profile for user: {user.username}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSuccessfully created {created_count} profile(s)"
            )
        )
