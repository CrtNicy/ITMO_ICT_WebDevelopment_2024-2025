# warriors_app/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Warrior, Profession, Skill, SkillOfWarrior
from .serializers import WarriorSerializer, ProfessionSerializer, SkillSerializer, SkillOfWarriorSerializer

# Войны

class WarriorListView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    name = 'warriors_all'

class WarriorCreateView(generics.CreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    name = 'warrior_create'

class WarriorDetailView(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    name = 'warrior_detail'

class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    name = 'warrior_update'

class WarriorDeleteView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    name = 'warrior_delete'

# Профессии

class ProfessionListView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    name = 'professions_all'

class ProfessionCreateView(generics.CreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    name = 'profession_create'

class ProfessionDetailView(generics.RetrieveAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    name = 'profession_detail'

class ProfessionUpdateView(generics.UpdateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    name = 'profession_update'

class ProfessionDeleteView(generics.DestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    name = 'profession_delete'

# Навыки

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skills_all'

class SkillCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_create'

class SkillDetailView(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_detail'

class SkillUpdateView(generics.UpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_update'

class SkillDeleteView(generics.DestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    name = 'skill_delete'

# Дополнительные Фильтры

class WarriorsByProfessionView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    name = 'warriors_with_professions'

    def get_queryset(self):
        profession_id = self.kwargs['profession_id']
        return Warrior.objects.filter(profession__id=profession_id)

class WarriorsBySkillView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    name = 'warriors_with_skills'

    def get_queryset(self):
        skill_id = self.kwargs['skill_id']
        return Warrior.objects.filter(skill__id=skill_id).distinct()

class WarriorSkillsView(generics.RetrieveAPIView):
    serializer_class = SkillOfWarriorSerializer
    name = 'warriors_skills'

    def get(self, request, warrior_id):
        try:
            warrior = Warrior.objects.get(pk=warrior_id)
        except Warrior.DoesNotExist:
            return Response({"Error": "Warrior not found"}, status=status.HTTP_404_NOT_FOUND)
        skills = SkillOfWarrior.objects.filter(warrior=warrior)
        serializer = self.get_serializer(skills, many=True)
        return Response({"Skills": serializer.data}, status=status.HTTP_200_OK)
