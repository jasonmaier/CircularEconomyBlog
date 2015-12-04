from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tasks = Table('tasks', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('priority', INTEGER, nullable=False),
    Column('user_id', INTEGER),
    Column('description', VARCHAR(length=140)),
    Column('Cr', FLOAT),
    Column('Cu', FLOAT),
    Column('Ec', FLOAT),
    Column('Ef', FLOAT),
    Column('Fr', FLOAT),
    Column('Fu', FLOAT),
    Column('L', FLOAT),
    Column('Lav', FLOAT),
    Column('Mass', FLOAT),
    Column('U', FLOAT),
    Column('Uav', FLOAT),
    Column('LFI', FLOAT),
    Column('MCI', FLOAT),
    Column('VirginFeed', FLOAT),
    Column('Wc', FLOAT),
    Column('Wf', FLOAT),
    Column('Wtot', FLOAT),
    Column('X', FLOAT),
    Column('industry', VARCHAR(length=140)),
    Column('product', VARCHAR(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].columns['priority'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tasks'].columns['priority'].create()
