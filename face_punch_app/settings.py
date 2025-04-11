from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('face_app'),
        'USER': config('admin'),
        'PASSWORD': config('a1vSOFS8AKb1Gp5exNiN'),
        'HOST': config('django.cb0osm6s4goh.ap-south-1.rds.amazonaws.com'),
        'PORT': '5432',
    }
}
