import sentry_sdk
from app.api import create_app
from app.core.config import settings
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

sentry_sdk.init(dsn=settings.SENTRY_DSN)

app = SentryAsgiMiddleware(create_app())
