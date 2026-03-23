from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', team=dc),
        ]

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        w2 = Workout.objects.create(name='Running', description='Cardio workout')

        # Create activities
        Activity.objects.create(user=users[0], workout=w1, duration=30)
        Activity.objects.create(user=users[1], workout=w2, duration=45)
        Activity.objects.create(user=users[2], workout=w1, duration=20)
        Activity.objects.create(user=users[3], workout=w2, duration=60)

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
