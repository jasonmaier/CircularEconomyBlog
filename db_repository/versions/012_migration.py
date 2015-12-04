from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tasks = Table('tasks', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('description', TEXT, nullable=False),
    Column('priority', INTEGER, nullable=False),
    Column('user_id', INTEGER),
)

tasks = Table('tasks', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('task', String(length=140)),
    Column('priority', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].columns['description'].drop()
    post_meta.tables['tasks'].columns['task'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].columns['description'].create()
    post_meta.tables['tasks'].columns['task'].drop()
