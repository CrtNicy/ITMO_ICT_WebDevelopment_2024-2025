# warriors_app/urls.py

from django.urls import path

from .views import (
    WarriorListView, WarriorCreateView, WarriorDetailView, WarriorUpdateView, WarriorDeleteView,
    ProfessionListView, ProfessionCreateView, ProfessionDetailView, ProfessionUpdateView, ProfessionDeleteView,
    SkillListView, SkillCreateView, SkillDetailView, SkillUpdateView, SkillDeleteView,
    WarriorsByProfessionView, WarriorsBySkillView, WarriorSkillsView
)

urlpatterns = [
    # Админка
    #path('admin/', admin.site.urls),

    # Войны
    path('warriors/', WarriorListView.as_view(), name='warriors_all'),
    path('warrior/create/', WarriorCreateView.as_view(), name='warrior_create'),
    path('warrior/<int:pk>/', WarriorDetailView.as_view(), name='warrior_detail'),
    path('warrior/<int:pk>/update/', WarriorUpdateView.as_view(), name='warrior_update'),
    path('warrior/<int:pk>/delete/', WarriorDeleteView.as_view(), name='warrior_delete'),
    path('warriors/by_profession/<int:profession_id>/', WarriorsByProfessionView.as_view(),
         name='warriors_with_professions'),
    path('warriors/by_skill/<int:skill_id>/', WarriorsBySkillView.as_view(), name='warriors_with_skills'),
    path('warriors/<int:warrior_id>/skills/', WarriorSkillsView.as_view(), name='warriors_skills'),

    # Профессии
    path('professions/', ProfessionListView.as_view(), name='professions_all'),
    path('profession/create/', ProfessionCreateView.as_view(), name='profession_create'),
    path('profession/<int:pk>/', ProfessionDetailView.as_view(), name='profession_detail'),
    path('profession/<int:pk>/update/', ProfessionUpdateView.as_view(), name='profession_update'),
    path('profession/<int:pk>/delete/', ProfessionDeleteView.as_view(), name='profession_delete'),

    # Навыки
    path('skills/', SkillListView.as_view(), name='skills_all'),
    path('skill/create/', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    path('skill/<int:pk>/update/', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill_delete'),
]
