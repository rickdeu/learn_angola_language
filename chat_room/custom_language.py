import django.conf.locale
from django.conf import global_settings


gettext_noop = lambda s: s

EXTRA_LANG_INFO = {
    'um': {
        'bidi': True, 
        'code': 'um',
        'name': 'Umbundu',
        'name_local': 'Umbundu',
    },
        'na': {
        'bidi': True, 
        'code': 'na',
        'name': 'Nhaneka',
        'name_local': 'Nhaneka',
    },
            'kim': {
        'bidi': True, 
        'code': 'kim',
        'name': 'Kimbundo',
        'name_local': 'Kimbundo',
    },
        'kik': {
        'bidi': True, 
        'code': 'kik',
        'name': 'Kikongo',
        'name_local': 'Kikongo',
    },
       'ngu': {
        'bidi': True, 
        'code': 'ngu',
        'name': 'Ngaguela',
        'name_local': 'Ngaguela',
    },
    
}

#LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO


global_settings.LANGUAGES = global_settings.LANGUAGES + [("um",'Umbundu')]
global_settings.LANGUAGES = global_settings.LANGUAGES + [("na",'Nhaneka')]
global_settings.LANGUAGES = global_settings.LANGUAGES + [("kim",'Kimbundo')]
global_settings.LANGUAGES = global_settings.LANGUAGES + [("kik",'Kikongo')]
global_settings.LANGUAGES = global_settings.LANGUAGES + [("ngu",'Ngaguela')]

