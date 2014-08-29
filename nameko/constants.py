CALL_ID_STACK_CONTEXT_KEY = 'call_id_stack'
AUTH_TOKEN_CONTEXT_KEY = 'auth_token'
LANGUAGE_CONTEXT_KEY = 'language'
USER_ID_CONTEXT_KEY = 'user_id'


NAMEKO_CONTEXT_KEYS = (
    LANGUAGE_CONTEXT_KEY,
    USER_ID_CONTEXT_KEY,
    AUTH_TOKEN_CONTEXT_KEY,
    CALL_ID_STACK_CONTEXT_KEY,
)


MAX_WORKERS_CONFIG_KEY = 'max_workers'
PARENT_CALLS_CONFIG_KEY = 'parent_calls_tracked'

DEFAULT_MAX_WORKERS = 10
DEFAULT_PARENT_CALLS_TRACKED = 10

DEFAULT_RETRY_POLICY = {'max_retries': 3}
