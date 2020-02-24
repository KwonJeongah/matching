# matching
좌표 입력하면 그 좌표가 있는 도로 정보 출력

KTDB 도로망 중 용인시만 대상으로 함 
전체 도로를 대상으로 하기위해서는 KTDB데이터 02_링크의 shp파일 이용
(용량이 커 git에 올라가지 않음)

## 개발 환경
Ubuntu 18.04
django
djangorestframework
django-rest-swagger
networkx 
geopandas

## allowed_hosts
matching/settings.py의 ALLOWED_HOSTS에서 추가

## admin 계정
id: mtov
email: abcd@mtov.net
password: 1234

## url접근
admin: http://192.168.0.143:8000/admin/
coords: http://192.168.0.143:8000/api/v1/coords/
road_info: http://192.168.0.143:8000/link_mathing/

## road_info
- 좌표값 위치의 도로 정보를 json형태로 보여줌
- 좌표값은 coords의 id: 1인 것을 기준으로 함

