from src import __version__


ELASTIC_APM = {
    'SERVER_URL': 'http://apm_p:8200',
    'SERVICE_NAME': "apm_test",
    'SERVICE_VERSION': __version__,
    'ENVIRONMENT': 'local',
    'TRANSACTIONS_IGNORE_PATTERNS': ['/hc']
}

