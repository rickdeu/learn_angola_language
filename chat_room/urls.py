from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path(_('api/'), include('base.api.urls')),
    path('rosetta/', include('rosetta.urls')),
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
