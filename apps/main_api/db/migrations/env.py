from apps.main_api.core.config import settings
from apps.main_api.db.base import Base
from sqlalchemy import engine_from_config, pool

target_metadata = Base.metadata

def run_migrations_offline():
    ...
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        ...
    )

def run_migrations_online():
    ...
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=settings.DATABASE_URL
    )
