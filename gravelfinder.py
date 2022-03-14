from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY','XXX')
HOST=os.environ.get('HOST','0.0.0.0')
PORT=os.environ.get('PORT','5000')

@app.route('/')
def index():
    return redirect(url_for('label_by_class_using_js'))

@app.route('/label_by_class')
def label_by_class():
    return render_template('map_by_classifcation.html')

@app.route('/test')
def test():
    return render_template('test.html',message='This is a test page.')

@app.route('/google')
def google_map():    
    return render_template('google_map.html',google_api_key=GOOGLE_API_KEY)

@app.route('/centerline')
def label_by_class_using_js():
    webmap='2e41bf75bf604569a6b7f6583ce71e60'
    return render_template('arcgic_js_view.html',webmap=webmap)

def main():
    app.run(host=HOST,port=PORT)

if __name__ == '__main__':
    main()
