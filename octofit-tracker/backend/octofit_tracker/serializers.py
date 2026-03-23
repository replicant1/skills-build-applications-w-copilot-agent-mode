from rest_framework import serializers
from .models import User, Team, Workout, Activity, Leaderboard


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.id)
    def get_team(self, obj):
        return str(obj.team.id) if obj.team else None
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id)
    class Meta:
        model = Team
        fields = ['id', 'name']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    workout = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id)
    def get_user(self, obj):
        return str(obj.user.id)
    def get_workout(self, obj):
        return str(obj.workout.id)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'workout', 'duration', 'timestamp']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id)
    def get_user(self, obj):
        return str(obj.user.id)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score']
