from flask import Flask, render_template, request, redirect, send_file
import boto3

app = Flask(__name__)


@app.route("/")
def home():
    session = boto3.Session(region_name='us-east-1')
    ssm = session.client('ssm')
    # bucket_name = ssm.get_parameter(Name='bucket-name')
    return render_template('index.html', bucket_name=ssm.get_parameter(Name='bucket-name')['Parameter']['Value'])

if __name__ == '__main__':
    app.run(debug=True)