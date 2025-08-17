import os

# Local daki PostgreSQL bağlantı bilgileri
POSTGRES_USER_LOCAL = "fast_api_user"
POSTGRES_PASSWORD_LOCAL = "fast_api_password"
POSTGRES_DB_LOCAL = "fast_api_db"
POSTGRES_HOST_LOCAL = "localhost"
POSTGRES_PORT_LOCAL = "5433"
POSTGRES_CONN_INFO_LOCAL = (
    f"dbname='{POSTGRES_DB_LOCAL}' "
    f"user='{POSTGRES_USER_LOCAL}' "
    f"password='{POSTGRES_PASSWORD_LOCAL}' "
    f"host='{POSTGRES_HOST_LOCAL}' "
    f"port='{POSTGRES_PORT_LOCAL}'"
)



# Docker Environment için PostgreSQL bağlantı bilgileri
POSTGRES_USER_DOCKER = os.getenv("POSTGRES_USER", "fast_api_user")
POSTGRES_PASSWORD_DOCKER = os.getenv("POSTGRES_PASSWORD", "fast_api_password")
POSTGRES_DB_DOCKER = os.getenv("POSTGRES_DB", "fast_api_db")
POSTGRES_HOST_DOCKER = os.getenv("POSTGRES_HOST", "db")  # docker-compose'da host ismi db
POSTGRES_PORT_DOCKER = os.getenv("POSTGRES_PORT", "5432")

POSTGRES_CONN_INFO = (
    f"dbname='{POSTGRES_DB_DOCKER}' "
    f"user='{POSTGRES_USER_DOCKER}' "
    f"password='{POSTGRES_PASSWORD_DOCKER}' "
    f"host='{POSTGRES_HOST_DOCKER}' "
    f"port='{POSTGRES_PORT_DOCKER}'"
)