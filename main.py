from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api=Api(app)

class HelloWord(Resource):
  def get(self):
    return {"data":"Hello World"}

  def post(self,name,age):
    return {"name":name,"age":age}

# routes
api.add_resource(HelloWord,"/helloworld/<string:name>/<int:age>")

if __name__ =="__main__":
  app.run(debug=True)
