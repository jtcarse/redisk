from flask import Flask, jsonify
from flask_cors import cross_origin
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/', methods=['GET'])
@cross_origin()
def root():
	redis.incr('hits')
	return jsonify({ 'message': u'This page has been viewed {} times.'.format(redis.get('hits')) })

if __name__ == '__main__':
	# only used locally
	app.run(host='0.0.0.0', port=8080, debug=True)
