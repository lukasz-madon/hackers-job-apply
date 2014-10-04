import os
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
	if request.json and request.json.get("answer") == os.getenv("ANSWER"):
		return os.getenv("JOB_EMAIL") + "\n"
	return "%s %s" % (os.getenv("QUESTION"),"POST the json to server with answer -> { 'answer': 'xxx'}")


if __name__ == "__main__":
	app.run(debug=True)