from django.shortcuts import render
import networkx as nx
import geopandas as gpd
import pandas as pd
import requests, json
from shapely.geometry import Point
from django.http import JsonResponse
from .models import Coords
def link_matching(requests):
    '''
    #특정 지역의 shp파일 생성
    link = gpdread_file('AD0022.shp')
    link.to_crs({'init': 'epsg:4326'})
    yongin_link = link[link['FIRST_GU'].isin(['31191','31192','31193'])]
    yongin_link.to_file("yongin_link_KTDB.shp")
    '''

   # point_url = 'http://192.168.0.143:8000/api/v1/point/'
   # result_url = 'http://192.168.0.143:8000/api/v1/resultlink/'

    #point = requests.get(point_url).json()
    #point = pd.DataFrame(point)
    #point = (point.lat, point.lon)
    #point = (37.278127, 127.115921)

    point = Coords.objects.get(id=1)
    point = (point.lat, point.lon)

    print(point)
    link = gpd.read_file('yongin_link_KTDB.shp')

    graph_edges = link[['geometry','UP_FROM_NO','UP_TO_NODE']].values.tolist()

    edges_with_distances = [
        (
        graph_edge,
        Point(tuple(reversed(point))).distance(graph_edge[0])
        )
        for graph_edge in graph_edges
    ]

    edges_with_dstances = sorted(edges_with_distances, key=lambda x: x[1])
    closest_edge_to_point = edges_with_distances[0][0]
    geometry, u, v = closest_edge_to_point

    result = link[(link['UP_FROM_NO'] == u) & (link['UP_TO_NODE'] == v)]
    result = result.to_json()

    #res = requests.post(result_url, data=result)
    '''
    result_link.link_id = 
    result_link.up_from_no = 
    result_link.up_to_no = 
    result_link.down_from_no =
    result_link.down_to_no =
    result_link.navi_lv = 
    result_link.koti_lv =
    result_link.length =
    result_link.st_dir =
    result_link.ed_dir =
    result_link.road_rank = 
    result_link.link_cate = 
    result_link.oneway = 
    result_link.width = 
    result_link.lane =
    result_link.up_lanes = 
    result_link.down_lanes = 
    result_link.pavement =
    result_link.road_name = 
    result_link.first_do =
    result_link.first_gu =
    result_link.tg_name = 
    result_link.road_fac_na = 
    result_link.road_no = 
    result_link.hov_lane = 
    result_link.shov_lane = 
    result_link.auto_exclue =
    result_link.num_cross = 
    result_link.barrier = 
    result_link.max_spd =
    result_link.facil_kind = 
    result_link.tl_density = 
    result_link.up_its_id =
    reult_link.down_its_id = 
    '''

    print(result)
    return JsonResponse(result, safe=False)