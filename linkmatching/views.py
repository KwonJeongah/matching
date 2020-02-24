from django.shortcuts import render
import networkx as nx
import geopandas as gpd
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

    point = Coords.objects.get(id=1)
    point = (point.lat, point.lon)

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

    return JsonResponse(result, safe=False)