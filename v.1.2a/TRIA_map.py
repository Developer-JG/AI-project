from random import *

class restaurant:
    def __init__(self, name, address, distance, opening_hours):
        self.name = name
        self.address = address
        self.distance = distance
        self.opening_hours = opening_hours

restaurant_1 = restaurant('이름','주소','거리','영업시간')
restaurant_2 = restaurant('이름','주소','거리','영업시간')
restaurant_3 = restaurant('이름','주소','거리','영업시간')
restaurant_4 = restaurant('이름','주소','거리','영업시간')
restaurant_5 = restaurant('이름','주소','거리','영업시간')

restaurant_list = [restaurant_1, restaurant_2, restaurant_3, restaurant_4, restaurant_5]

#맛집찾기
def hungry(command_result, location_3,location_4):
    if naver + google + mango + cacao + trip + code >= 2:
        if naver == 1:
            print('네이버')
        if google == 1:
            print('구글')
        if mango == 1:
            print('망고플레이트')
        if cacao == 1:
            print('카카오플레이스')
        if trip == 1:
            print('트립어드바이저')
        if code == 1:
            print('다이닝코드')

        app == input('검색엔진을 선택하세요:')

        if app != '네이버' or app != '구글' or app != '망고플레이트' or app != '카카오플레이스' or app != '트립어드바이저' or app != '다이닝코드':
            print('지원되지 않는 검색엔진입니다.\n기본 검색엔진으로 검색합니다.')
            app = ''
    try:
        print("{0}에서 가까운 맛집을 검색합니다.\n\n{1} {2} 근처 맛집".format(app, location_3,location_4))
    except:
        print("가까운 맛집을 검색합니다.\n\n{0} {1} 근처 맛집".format(location_3, location_4))

    for i in range(len(restaurant_list)):
        print("{0}  {1}".format(i + 1, restaurant_list[i].name))
    ans = input("\n더 보고 싶은 음식점 번호를 입력하세요\n:")
    try:
        if 1 <= int(ans) <= range(len(restaurant_list)):
            print("\n{0} 의 점보\n주소 : (1)\n거리 : {2}\n영업시간 : {3}" \
                  .format(restaurant_list[ans].name, restaurant_list[ans].address \
                          ,restaurant_list[ans].distance, restaurant_list[ans].opening_hours))
    except:
        pass

#길찾기
def navigation(command_result_1, command_result, location_2, location_3, location_4):
    pass