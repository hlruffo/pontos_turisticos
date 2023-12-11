"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions


from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontosTuristicosViewSet
from enderecos.api.viewsets import EnderecoViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet)
#router.register(r'pontoturistico', PontosTuristicosViewSet, basename='PontosTuristicos') -> usado para
#sobreescrever get_queryset
router.register(r'atracoes', AtracaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'enderecos', EnderecoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Pontos Turísticos",
        default_version='v1',
        description="API do sistema de pontos turísticos",
        contact=openapi.Contact(email="hugo.ruffo@brilliantmachine.com.br"),
    ),
    public=True,
    #permission_classes=(permissions.DjangoModelPermissionsOrAnonReadOnly,),
)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    
    #links para documentação
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
