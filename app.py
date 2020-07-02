from flask import Flask, render_template
MyApp = Flask(__name__)

@MyApp.route("/")
def hello():
	return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)
