from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [  {    "ID":1,    "title":"Data Analyst",    "location": "Mumbai, India",    "salary": "Rs 10,00,000"  },
          {    "ID":2,    "title":"Data Scientist",    "location": "Delhi, India",    "salary": "Rs 15,00,000"  },
          {    "ID":3,    "title":"Front-end Engineer",    "location": "Remote",    "salary": "Rs 15,00,000"  },
          {    "ID":4,    "title":"Backend-end Engineer",    "location": "San Francisco, USA",    "salary": "$ 120,000"  }]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(debug=True)

