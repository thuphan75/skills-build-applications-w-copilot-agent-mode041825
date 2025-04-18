from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data for users
        users = [
            {"_id": ObjectId(), "username": "john_doe", "email": "john_doe@example.com", "password": "password123"},
            {"_id": ObjectId(), "username": "jane_smith", "email": "jane_smith@example.com", "password": "password123"},
        ]
        db.users.insert_many(users)

        # Insert test data for teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert test data for activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": 30},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Insert test data for leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert test data for workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Run", "description": "A quick morning run to start the day."},
            {"_id": ObjectId(), "name": "Evening Yoga", "description": "Relaxing yoga session in the evening."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))