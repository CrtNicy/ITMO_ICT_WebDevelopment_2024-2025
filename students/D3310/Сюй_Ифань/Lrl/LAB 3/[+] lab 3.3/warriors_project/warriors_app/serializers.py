# warriors_app/serializers.py

from rest_framework import serializers
from .models import Warrior, Profession, Skill, SkillOfWarrior

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id", "title", "description"]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "title"]

class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill_id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        source='skill',
        write_only=True
    )
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = SkillOfWarrior
        fields = ['skill_id', 'skill', 'level']

    def validate_level(self, value):
        if value < 1:
            raise serializers.ValidationError("Уровень навыка должен быть положительным числом.")
        return value

class WarriorSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    profession_id = serializers.PrimaryKeyRelatedField(
        queryset=Profession.objects.all(),
        write_only=True,
        source='profession'
    )
    skills = SkillOfWarriorSerializer(many=True, write_only=True, required=False)
    skill_details = SkillOfWarriorSerializer(source='skillofwarrior_set', many=True, read_only=True)
    race_display = serializers.CharField(source='get_race_display', read_only=True)

    class Meta:
        model = Warrior
        fields = [
            "id",
            "race",
            "race_display",
            "name",
            "level",
            "profession",
            "profession_id",
            "skills",
            "skill_details",
        ]

    def create(self, validated_data):
        skills_data = validated_data.pop('skills', [])
        warrior = Warrior.objects.create(**validated_data)
        for skill_data in skills_data:
            SkillOfWarrior.objects.create(
                warrior=warrior,
                skill=skill_data['skill'],
                level=skill_data['level']
            )
        return warrior

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills', [])
        profession = validated_data.pop('profession', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if profession is not None:
            instance.profession = profession

        instance.save()

        if skills_data:
            # Удаляем существующие навыки
            instance.skill.clear()
            # Добавляем новые навыки с уровнями
            for skill_data in skills_data:
                SkillOfWarrior.objects.create(
                    warrior=instance,
                    skill=skill_data['skill'],
                    level=skill_data['level']
                )

        return instance
