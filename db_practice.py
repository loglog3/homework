# 데이터 넣기
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.
#
# # MongoDB에 insert 하기
#
# # 'users'라는 collection에 데이터를 생성합니다.
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})

#데이터 확인하기
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.
#
# # MongoDB에서 데이터 모두 보기
# all_users = list(db.users.find({})) # find({중괄호 안에 원하는 것을 씁니다, 딕셔너리 형태입니다})
#
# print(all_users[0])  # 0번째 결과값을 보기
# print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기
#
# for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
#     print(user)




#스크랩핑 + DB 같이하기
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.movie  # 'dbsparta'라는 이름의 db를 만듭니다.
#
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
# movies = soup.select('#old_content > table > tbody > tr')
#
# for movie in movies:
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt']
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#         print(rank, title, star)
#         db.list.insert_one({'rank':rank,'title':title,'star':star})


from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.movie  # 'dbsparta'라는 이름의 db를 만듭니다.

# 1등의 별점 출력하기
rank1st = db.list.find_one({'rank': '01'})
print(rank1st['star'])

# 2등의 타이틀을 내 이름으로
db.list.update_one({'rank': '02'}, {'$set': {'title': '이승민'}})
print(db.list.find_one({'rank': '02'})['title'])

# 9등 데이터 지우기
db.list.delete_one({'rank': '09'})

