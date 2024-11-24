from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_texts():
    text1 = request.form.get('text1', '')
    text2 = request.form.get('text2', '')
    merged_text = text1 + text2
    return jsonify({'result': merged_text})

if __name__ == '__main__':
    app.run(debug=True)
