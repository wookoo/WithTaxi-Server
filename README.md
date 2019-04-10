# WithTaxi-Server

개발환경 : 윈도우 10, python 3.x.x , django 2.x 

실행환경 : 윈도우 or Linux , Python 3 이상, django 2 이상

사용 에디터 : Atom

사전 설치 프로그램 : redias, Channels_radis (파이썬 패키지 , 리눅스일경우)

필요 패키지 : django, django-channels

[참고사이트](https://victorydntmd.tistory.com/262)

실행방법

- 윈도우 : cmd 실행 > manage.py 폴더로 이동 > cmd 에서 python manage.py runserver 0.0.0.0:포트번호
- 리눅스 : 명령 프롬트 실행 > manage..py 폴더 이동 > 명령프롬트에서 python3 manage.py runserver 0.0.0.0:포트번호



알고리즘 소개 

1. 서버에서 접속이 되면 url 에 해당하는 배열에 객체를 넣습니다. url 이 서버에 존재하지 않으면 객체는 저장하지 않습니다.
2. 연결이 되었으면 for 문을 사용하여 배열의 크기를 확인합니다. 배열의 크기가 2면 객체가 2개 존재한다는 뜻 입니다.
3. 객체가 A B 로 2개 존재한다면 A 객체엔 B 의 전화번호 필드를 반환하고, B 객체엔 A 의 전화번호 필드를 반환해줍니다.
4. 반환을 해줬으면 배열을 클리어 합니다.