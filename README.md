# Django-React Product Hub

Welcome to the Django-React Product Hub application! This project is aimed at creating a platform where users can authenticate,
search for items, and make selections, with all changes being stored in an SQLite database.

## Features

- User Authentication: Allow users to register and log in securely.
- Item Search: Enable users to search for items within the application.
- Selection Management: Allow users to select items and manage their choices.
- Database Storage: Store user selections and other relevant information in an SQLite database.

## Setup

1. Clone the repository to your local machine:
    git clone https://github.com/syedaakash/django-react-product-hub.git
   
3. Navigate to the project directory:
    cd product_hub
   
4. **Set up the Django backend:**
  - Install required Python packages:
     pip install -r requirements.txt
  - Apply database migrations:
    python manage.py migrate
  - Run the development server:
    python manage.py runserver
    
4. **changes made in settings.py**
    INSTALLED_APPS = [
    ...
    'base.apps.BaseConfig',

    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    "corsheaders",
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

MIDDLEWARE = [
    ...

    "corsheaders.middleware.CorsMiddleware",

    ...
]

CORS_ALLOW_ALL_ORIGINS = True


5. **Set up the React frontend:**
  - Navigate to the frontend directory:
    cd frontend
  - Install Node.js dependencies:
    npm install
  - Start the React development server:
    npm start
    
