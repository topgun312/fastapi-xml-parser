TAG_METADATA = [
    {
        "name": "parser_data",
        "description": "A service for analyzing and uploading data from files to a database, generating an invoice and displaying a short analytical report with sales conclusions",
    },
    {
        "name": "healthz",
        "description": "Standard service health check",
    },
]

TITLE = "FastAPI XML Parser & AI Analyzer Service app"

DESCRIPTION = (
    "An application with the following functionality:"
    "• Analyzing and uploading data from files to a database"
    "• Generating an invoice and displaying a short analytical report with sales conclusions"
)


VERSION = "0.0.1"

ERROR_MAPS = {
    "postgres": "PostgreSQL connection failed",
    "redis": "Redis connection failed",
    "celery": "Celery connection failed",
}
