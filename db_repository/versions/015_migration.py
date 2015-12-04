from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tasks = Table('tasks', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String(length=140)),
    Column('priority', Integer),
    Column('user_id', Integer),
    Column('Mass', Float),
    Column('Fr', Float, default=ColumnDefault(0.0)),
    Column('Fu', Float, default=ColumnDefault(0.0)),
    Column('Cr', Float, default=ColumnDefault(0.0)),
    Column('Cu', Float, default=ColumnDefault(0.0)),
    Column('Ec', Float, default=ColumnDefault(0.0)),
    Column('Ef', Float, default=ColumnDefault(0.0)),
    Column('L', Float, default=ColumnDefault(1.0)),
    Column('Lav', Float, default=ColumnDefault(1.0)),
    Column('U', Float, default=ColumnDefault(1.0)),
    Column('Uav', Float, default=ColumnDefault(1.0)),
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
    post_meta.tables['tasks'].columns['LFI'].create()
    post_meta.tables['tasks'].columns['MCI'].create()
    post_meta.tables['tasks'].columns['VirginFeed'].create()
    post_meta.tables['tasks'].columns['Wc'].create()
    post_meta.tables['tasks'].columns['Wf'].create()
    post_meta.tables['tasks'].columns['Wtot'].create()
    post_meta.tables['tasks'].columns['X'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tasks'].columns['LFI'].drop()
    post_meta.tables['tasks'].columns['MCI'].drop()
    post_meta.tables['tasks'].columns['VirginFeed'].drop()
    post_meta.tables['tasks'].columns['Wc'].drop()
    post_meta.tables['tasks'].columns['Wf'].drop()
    post_meta.tables['tasks'].columns['Wtot'].drop()
    post_meta.tables['tasks'].columns['X'].drop()
