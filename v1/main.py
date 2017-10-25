from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	file_handler = open('codes/init.cc', 'r')
	initial_code = file_handler.read()
	file_handler.close()

	file_hanlder = open('codes/init.in', 'r')
	initial_input = file_hanlder.read()
	file_handler.close()

	return render_template('index.html', init_code=initial_code, init_input=initial_input)

if __name__ == '__main__':
	app.run()
