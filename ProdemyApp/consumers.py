from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import ChatComment, Group , User
from channels.db import database_sync_to_async
import json

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        print('websocket Connetcted...')
        
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        # self.close()   #to reject the connections
        
        
    async def receive_json(self, content, **kwargs):
        print('Message received from client...a.', content)
        # this content is dict formmat because of used jsonWebsocketconsumer..
        # otherwise we get string type
        print('message========')
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        user = self.scope['user']
       
        
        print('message====================user', user)
        
        print("Type of conten===============", type(content))
        
        if self.scope['user'].is_authenticated:
            user = user.name
            chat = ChatComment(
                content = content['msg'],
                user=user,
                group = group
            )
            print('chat========', chat)
            
            await database_sync_to_async(chat.save)()
            content['user']=user

            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'chat.message',
                    'message': json.dumps(content)
                }
            )
        else:
            print('========ok ok ===========')
            await self.send_json(
                json.dumps({'msg':'LogIn Required','user':'anonymous'})
            )
        
    async def chat_message(self, event):
            await self.send_json({
                'msg':event['message']
            })
        
       
        
    async def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code)
    
        