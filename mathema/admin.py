from django.contrib import admin

from .models import Curriculum, Objetivo, Suporte, TipoSuporte, Topico, TopicoAtividade, \
    Atividade, TopicoSuporte, User, Answer

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Objetivo)
admin.site.register(Suporte)
admin.site.register(TipoSuporte)
admin.site.register(Topico)
admin.site.register(TopicoSuporte)
admin.site.register(TopicoAtividade)
admin.site.register(Atividade)
admin.site.register(Answer)