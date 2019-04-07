from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json



onyang_to_kyunghee = []
onyang_to_schoolback = []
onyang_to_hyang2 = []
onyang_to_schoolfront = []
sinchang_to_kyunghee = []
sinchang_to_schoolback = []
sinchang_to_hyang2 = []
sinchang_to_schoolfront = []

#해시를 사용하여 수정하기 편하게 한다
dictionary = {'onyang_to_kyunghee' : onyang_to_kyunghee,
'onyang_to_schoolback' : onyang_to_schoolback,
'onyang_to_hyang2' : onyang_to_hyang2,
'onyang_to_schoolfront' : onyang_to_schoolfront,
'sinchang_to_kyunghee' : sinchang_to_kyunghee,
'sinchang_to_schoolback' : sinchang_to_schoolback,
'sinchang_to_hyang2' : sinchang_to_hyang2,
'sinchang_to_schoolfront' : sinchang_to_schoolfront}

class ChatConsumer(WebsocketConsumer):


    def connect(self):
        self.room_nametemp = self.scope['url_route']['kwargs']['room_name'] #채팅방 이름 자체를 전화번호를 포함된 채로 가져오게 한다.
        self.room_name = self.room_nametemp.split("+")[0] #+ 로 전화번호를 구분한다.
        try:
            self.phone_num = self.room_nametemp.split("+")[1] #전화번호가 무조건 있게 한다
        except:
            self.phone_num = "1234" #전화번호가 없으면 1234로 출력되게 한다.

        self.room_group_name = 'chat_%s' % self.room_name

        try:
            if (self.phone_num != "1234"): #전화번호가 초기값이 아니면
                dictionary[self.room_name].append(self) #딕셔너리에 객체를 저장
        except:
            pass

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        for key in dictionary.keys():
            if len(dictionary[key]) == 2: #딕셔너리의 크기가 2면
                for j in range(2): #0부터 2까지 반복하고
                    temp = dictionary[key][j-1] #temp 의 객체를 만들고
                    messages = str(dictionary[key][j].phone_num) #그 객체가 가진 전화번호를 메세지로 한다
                    temp.send(text_data=json.dumps({
                        'message': messages #메세지를 클라이언트에 전송한다
                    }))
                    temp.disconnect() #그 후 연결을 끊어버린다.

                dictionary[key] = [] #그러고 그 리스트를 초기화 시킨다.



    #연결 끊김  지워주는거 만들기
    def disconnect(self, close_code=1001):
        print("연결 해제되었음")
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

# 여기서 부턴 필요없는 메소드들

    # 웹서버로부터 정보를 받는다
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print(event)
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
