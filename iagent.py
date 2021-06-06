

class ChatMessage:
	def __init__(self,timestamp,user,text,src,user_color="default",badges=[],msg_id=""):
		self.timestamp=timestamp
		self.msg_id=msg_id
		self.user=user
		self.user_color=user_color
		self.badges=badges
		self.text=text
		self.src=src

def publish_message(msg):
	pass
