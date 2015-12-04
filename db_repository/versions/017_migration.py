from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tasks = Table('tasks', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String(length=140)),
    Column('product', String(length=140)),
    Column('industry', String(length=140)),
    Column('priority', Integer),
    Column('user_id', Integer),
    Column('Mass', Float),
    Column('Fr', Float),
    Column('Fu', Float),
    Column('Cr', Float),
    Column('Cu', Float),
    Column('Ec', Float),
    Column('Ef', Float),
    Column('L', Float),
    Column('Lav', Float),
    Column('U', Float),
    Column('Uav', Float),
    Column('VirginFeed', Float),
    Column('Wtot', Float),
    Column('Wc', Float),
    Column('Wf', Float),
    Column('LFI', Float),
    Column('X', Float),
    Column('MCI', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tasks'].columns['industry'].create()
    post_meta.tables['tasks'].columns['product'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tasks'].columns['industry'].drop()
    post_meta.tables['tasks'].columns['product'].drop()
