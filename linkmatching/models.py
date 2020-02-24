from django.db import models

# Create your models here.
class Coords(models.Model):
    lat = models.FloatField(default = -1)
    lon = models.FloatField(default = -1)

class ResultLink(models.Model):
    link_id = models.CharField(max_length=13)
    up_from_no = models.CharField(max_length=6)
    up_to_node = models.CharField(max_length=6)
    down_from_no = models.CharField(max_length=6)
    down_to_no = models.CharField(max_length=6)
   
    navi_lv = models.CharField(max_length=1)
    koti_lv = models.CharField(max_length=1)
   
    length = models.FloatField(default = -1)
    st_dir = models.CharField(max_length=3)
    ed_dir = models.CharField(max_length=3)

    road_rank = models.CharField(max_length=3)
    link_cate = models.IntegerField(default=-1)

    oneway = models.CharField(max_length = 1)
    
    width = models.IntegerField(default = -1)
    lane = models.IntegerField(default = -1)
    up_lanes = models.IntegerField(default = -1)
    down_lanes = models.IntegerField(default = -1)

    pavement = models.CharField(max_length = 1)
    road_name = models.CharField(max_length=30)
    first_do = models.CharField(max_length = 2)
    first_gu = models.CharField(max_length = 5)
    tg_name = models.CharField(max_length = 30)
    road_fac_na = models.CharField(max_length = 30)
    road_no = models.CharField(max_length =5)
    
    hov_lane = models.CharField(max_length = 1)
    shov_lane = models.CharField(max_length = 1)
    auto_exclu = models.CharField(max_length = 1)

    num_cross = models.IntegerField(default = -1)
    barrier = models.CharField(max_length = 2)

    max_spd = models.IntegerField(default = -1)
    facil_kind = models.IntegerField(default = -1)
    tl_density = models.FloatField(default = -1)
    up_its_id = models.CharField(max_length = 10)
    down_its_id = models.CharField(max_length = 10)
