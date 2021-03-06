"""empty message

Revision ID: 23724b77eada
Revises: 
Create Date: 2018-04-18 13:34:49.841857

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '23724b77eada'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurement')
    op.drop_table('status')
    op.drop_table('sensor_manufacturer')
    op.drop_table('crop')
    op.drop_table('pid')
    op.drop_table('functions')
    op.drop_table('owner')
    op.drop_table('farm_sensor')
    op.drop_table('mushroom_farm')
    op.drop_table('sensor_interface')
    op.drop_table('controller_device')
    op.drop_table('mushroom')
    op.drop_table('sensor')
    op.drop_table('country')
    op.drop_table('phase')
    op.drop_table('material')
    op.drop_table('mushroom_condition')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mushroom_condition',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('min_value', mysql.FLOAT(), nullable=False),
    sa.Column('max_value', mysql.FLOAT(), nullable=False),
    sa.Column('measurement_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('phase_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['measurement_id'], [u'measurement.id'], name=u'mushroom_condition_ibfk_1'),
    sa.ForeignKeyConstraint(['phase_id'], [u'phase.id'], name=u'mushroom_condition_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('material',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('phase',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('n_days', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('nth_phase', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mushroom_color', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('avg_weight_per_seed', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('n_alive', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('n_dead', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mushroom_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('crop_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('material_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['crop_id'], [u'crop.id'], name=u'phase_ibfk_2'),
    sa.ForeignKeyConstraint(['material_id'], [u'material.id'], name=u'phase_ibfk_1'),
    sa.ForeignKeyConstraint(['mushroom_id'], [u'mushroom.id'], name=u'phase_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('country',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('sensor',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('manufacturer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('function_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('power_supply', mysql.FLOAT(), nullable=True),
    sa.Column('interface_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['interface_id'], [u'sensor_interface.id'], name=u'sensor_ibfk_2'),
    sa.ForeignKeyConstraint(['manufacturer_id'], [u'sensor_manufacturer.id'], name=u'sensor_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('mushroom',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('kingdom', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('division', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('_class', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('family', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('genus', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('spieces', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('common_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('number_of_phase', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('controller_device',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('controller_type', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('farm_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('pid_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('measurement_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['farm_id'], [u'mushroom_farm.id'], name=u'controller_device_ibfk_2'),
    sa.ForeignKeyConstraint(['measurement_id'], [u'measurement.id'], name=u'controller_device_ibfk_3'),
    sa.ForeignKeyConstraint(['pid_id'], [u'pid.id'], name=u'controller_device_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('sensor_interface',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('mushroom_farm',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('owner_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status_code', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('address', mysql.VARCHAR(length=128), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], [u'owner.id'], name=u'mushroom_farm_ibfk_2'),
    sa.ForeignKeyConstraint(['status_code'], [u'status.status_code'], name=u'mushroom_farm_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('farm_sensor',
    sa.Column('n_sensors', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('sensor_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('farm_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['farm_id'], [u'mushroom_farm.id'], name=u'farm_sensor_ibfk_2'),
    sa.ForeignKeyConstraint(['sensor_id'], [u'sensor.id'], name=u'farm_sensor_ibfk_1'),
    sa.PrimaryKeyConstraint('sensor_id', 'farm_id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('owner',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('display_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('functions',
    sa.Column('sensor_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('measurement_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['measurement_id'], [u'measurement.id'], name=u'functions_ibfk_2'),
    sa.ForeignKeyConstraint(['sensor_id'], [u'sensor.id'], name=u'functions_ibfk_1'),
    sa.PrimaryKeyConstraint('sensor_id', 'measurement_id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('pid',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('direction', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('band', mysql.FLOAT(), nullable=True),
    sa.Column('max_measure_age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_activated', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('period', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('setpoint', mysql.FLOAT(), nullable=True),
    sa.Column('p', mysql.FLOAT(), nullable=True),
    sa.Column('i', mysql.FLOAT(), nullable=True),
    sa.Column('d', mysql.FLOAT(), nullable=True),
    sa.Column('integrator_min', mysql.FLOAT(), nullable=True),
    sa.Column('integrator_max', mysql.FLOAT(), nullable=True),
    sa.Column('raise_min_duration', mysql.FLOAT(), nullable=True),
    sa.Column('raise_max_duration', mysql.FLOAT(), nullable=True),
    sa.Column('raise_min_off_duration', mysql.FLOAT(), nullable=True),
    sa.Column('lower_min_duration', mysql.FLOAT(), nullable=True),
    sa.Column('lower_max_duration', mysql.FLOAT(), nullable=True),
    sa.Column('lower_min_off_duration', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('crop',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('start_time', mysql.DATETIME(), nullable=False),
    sa.Column('end_time', mysql.DATETIME(), nullable=True),
    sa.Column('note', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('is_expr', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_current', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('be_number', mysql.FLOAT(), nullable=True),
    sa.Column('n_bags', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('seed_ratio', mysql.FLOAT(), nullable=True),
    sa.Column('mushroom_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('current_phase_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['current_phase_id'], [u'phase.id'], name=u'crop_ibfk_2'),
    sa.ForeignKeyConstraint(['mushroom_id'], [u'mushroom.id'], name=u'crop_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('sensor_manufacturer',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('country_code', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['country_code'], [u'country.id'], name=u'sensor_manufacturer_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('status',
    sa.Column('status_code', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('status_code'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('measurement',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('unit', mysql.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###
