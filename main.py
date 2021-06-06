
from flask import Flask, render_template
from flask_sse import sse
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import threading
import time

import .disco-client

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

'''
def publoop():
	print("new publoop")
	with app.app_context():
		while True:
			sse.publish({"message": datetime.datetime.now()}, type='publish')
			time.sleep(5)
'''

@app.before_first_request
def initialize():
   # create Discord thread
   
   # create IRC thread
   
   # start threads
   pass

'''
   thread = threading.Thread(target=publoop)
   thread.daemon = True
   thread.start()
'''

@app.route('/sse')
def sse_page():
   return render_template('sse-test.html')

if __name__ == '__main__':
   app.run(debug=True,host="0.0.0.0")
