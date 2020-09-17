# matching
- 좌표 입력하면 그 좌표가 있는 도로 정보 출력

- KTDB 도로망 중 용인시만 대상으로 함 
- 전체 도로를 대상으로 하기위해서는 KTDB데이터 02_링크의 shp파일 이용 

## 개발 환경
- Ubuntu 18.04
- django 3.0.3
- rest_framework 3.11.0
- rest_framework_swagger 2.2.0
- networkx 2.4
- geopandas 0.6.2

## 빌드 및 실행하기    
### 터미널 환경    
   * git, python, Django는 설치되어 있다고 가정
```  
  $ git clone https://github.com/dsalice/matching.git
  $ python manage.py
```  


### allowed_hosts    
matching/settings.py의 ALLOWED_HOSTS에서 추가

### url
- admin: http://localhost:8000/admin/
- coords: http://localhost:8000/api/v1/coords/
- road_info: http://localhost:8000/link_matching/

### road_info
- 좌표값 위치의 도로 정보를 json형태로 보여줌
- 좌표값은 coords의 id: 1인 것을 기준으로 함

### 출력 결과

![도로정보결과](https://user-images.githubusercontent.com/37493709/93419927-fc774f00-f8e8-11ea-8a00-66b160f4df48.png)
