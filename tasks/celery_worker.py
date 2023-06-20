from app import create_app

# Create app context for Celery to run in
app = create_app()
app.app_context().push()

from tasks import celery