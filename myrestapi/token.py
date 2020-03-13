from rest_framework_simplejwt.tokens import AccessToken,TokenBackendError, RefreshToken,TokenError

def generate_refreshtoken(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def generate_accesstoken(user):
    access = AccessToken.for_user(user)
    return {
        'refresh': str(access),
        'access': str(access.access_token),
    }