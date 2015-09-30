from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller with my name."""
 
    from_number = request.values.get('From', None)
     message ="Hello from CS6432015 jyotsna buddha"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)