from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title':'Хлеб',
  'sale':'100-300 тг',
},
  
{
  'id':2,
  'title':'Сэндвич',
  'sale':'700-1000 тг',
}, 
{
  'id':3,
  'title':'Выпечка',
  'sale':'1000-1500 тг'
}
]

@app.route("/")
def  hello_world():
  return render_template('bakery.html',
                        jobs=JOBS,
                        company_name='Lana_bakery')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)