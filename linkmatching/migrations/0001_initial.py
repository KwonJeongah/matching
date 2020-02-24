# Generated by Django 3.0.3 on 2020-02-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=-1)),
                ('lon', models.FloatField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='ResultLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.CharField(max_length=13)),
                ('up_from_node', models.CharField(max_length=6)),
                ('up_to_node', models.CharField(max_length=6)),
                ('down_from_node', models.CharField(max_length=6)),
                ('down_to_node', models.CharField(max_length=6)),
                ('navi_lv', models.CharField(max_length=1)),
                ('koti_lv', models.CharField(max_length=1)),
                ('length', models.FloatField(default=-1)),
                ('st_dir', models.CharField(max_length=3)),
                ('ed_dir', models.CharField(max_length=3)),
                ('road_rank', models.CharField(max_length=3)),
                ('link_category', models.IntegerField(default=-1)),
                ('oneway', models.CharField(max_length=1)),
                ('width', models.IntegerField(default=-1)),
                ('lanes', models.IntegerField(default=-1)),
                ('up_lanes', models.IntegerField(default=-1)),
                ('down_lanes', models.IntegerField(default=-1)),
                ('pavement', models.CharField(max_length=1)),
                ('road_name', models.CharField(max_length=30)),
                ('first_do', models.CharField(max_length=2)),
                ('first_gu', models.CharField(max_length=5)),
                ('toll_name', models.CharField(max_length=30)),
                ('road_facility_name', models.CharField(max_length=30)),
                ('road_no', models.CharField(max_length=5)),
                ('hov_buslane', models.CharField(max_length=1)),
                ('shov_buslane', models.CharField(max_length=1)),
                ('autoexcusive', models.CharField(max_length=1)),
                ('numcross', models.IntegerField(default=-1)),
                ('barrier', models.CharField(max_length=2)),
                ('maxspeed', models.IntegerField(default=-1)),
                ('facility_kind', models.IntegerField(default=-1)),
                ('tl_density', models.FloatField(default=-1)),
                ('traf_id_p', models.CharField(max_length=10)),
                ('traf_id_n', models.CharField(max_length=10)),
            ],
        ),
    ]
