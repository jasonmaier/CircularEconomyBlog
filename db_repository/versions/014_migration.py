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
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tasks'].columns['Cr'].create()
    post_meta.tables['tasks'].columns['Cu'].create()
    post_meta.tables['tasks'].columns['Ec'].create()
    post_meta.tables['tasks'].columns['Ef'].create()
    post_meta.tables['tasks'].columns['Fr'].create()
    post_meta.tables['tasks'].columns['Fu'].create()
    post_meta.tables['tasks'].columns['L'].create()
    post_meta.tables['tasks'].columns['Lav'].create()
    post_meta.tables['tasks'].columns['Mass'].create()
    post_meta.tables['tasks'].columns['U'].create()
    post_meta.tables['tasks'].columns['Uav'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tasks'].columns['Cr'].drop()
    post_meta.tables['tasks'].columns['Cu'].drop()
    post_meta.tables['tasks'].columns['Ec'].drop()
    post_meta.tables['tasks'].columns['Ef'].drop()
    post_meta.tables['tasks'].columns['Fr'].drop()
    post_meta.tables['tasks'].columns['Fu'].drop()
    post_meta.tables['tasks'].columns['L'].drop()
    post_meta.tables['tasks'].columns['Lav'].drop()
    post_meta.tables['tasks'].columns['Mass'].drop()
    post_meta.tables['tasks'].columns['U'].drop()
    post_meta.tables['tasks'].columns['Uav'].drop()
