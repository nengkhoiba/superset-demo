FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}
SESSION_COOKIE_SAMESITE = None
ENABLE_PROXY_FIX = True
PUBLIC_ROLE_LIKE_GAMMA = True
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}
SECRET_KEY = "jkhsdhuh23oeh8y238ehjonwh"
CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ['http://superset:8088','http://localhost:8088']
}
OVERRIDE_HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
TALISMAN_ENABLED = False
ENABLE_CORS = True
HTTP_HEADERS={"X-Frame-Options":"ALLOWALL"}
WTF_CSRF_ENABLED = False