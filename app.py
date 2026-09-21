from flask import Flask,render_template,request
from analyser import analyse
from database import init_db, save_entry, get_entries

app = Flask(__name__)

# Initialisiing the databse when the app is started
init_db()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse_text():
    text = request.form.get('text')
    result = analyse(text)
    # saving entry into a database:
    save_entry(text,result["sentiment"],result["emotions"],result["score"])
    return render_template('result.html',result=result,text=text)

@app.route('/journal')
def journal():
    # Get the entries from the database
    entries = get_entries()
    return render_template('journal.html',entries=entries)

if __name__ == '__main__':
    app.run(debug=True)