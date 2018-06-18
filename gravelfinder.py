from flask import Flask, redirect, url_for, render_template
import config

app = Flask(__name__)

GOOGLE_API_KEY=config.GOOGLE_API_KEY

@app.route('/')
def index():
    return redirect(url_for('label_by_class'))

@app.route('/single_label')
def first_map():
    return render_template('map_class_iv_through_vii.html')

@app.route('/label_by_class')
def label_by_class():
    return render_template('map_by_classifcation.html')

@app.route('/test')
def test():
    return render_template('test.html',message='This is a test page.')

@app.route('/google')
def google_map():    
    return render_template('google_map.html',google_api_key=GOOGLE_API_KEY)

def main():
    pass

if __name__ == '__main__':
    main()
