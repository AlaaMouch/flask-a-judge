from flask import Flask, redirect, render_template, request
from subprocess import Popen, PIPE

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

@app.route('/compile', methods=['POST'])
def compile():
    file_handler = open('codes/tmp.cc', 'w')
    file_handler.write(request.form['sourcecode'])
    file_handler.close()

    compiler = Popen(["g++", "-std=c++11", "-Wall", "codes/tmp.cc", "-o", "codes/tmp.out"], stderr=PIPE)
    err = compiler.communicate()[1]

    if compiler.returncode == 0:
        file_handler = open('codes/tmp.in', 'w')
        file_handler.write(request.form['custominput'])
        file_handler.close()
        return redirect("/execute")
    else:
        file_handler = open('codes/tmp.err', 'w')
        file_handler.write(err)
        file_handler.close()
        return redirect("/errors")

@app.route('/execute')
def execute():
    file_handler = open('codes/tmp.in', 'r')
    custominput = file_handler.read()
    file_handler.close()

    executable = Popen(["./codes/tmp.out"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output = executable.communicate(custominput)[0]
    print(output)

    file_rm = Popen(["rm", "codes/tmp.cc", "codes/tmp.in", "codes/tmp.out"])

    return render_template('execute.html', output=output)

@app.route('/errors')
def errors():
    file_handler = open('codes/tmp.err', 'r')
    err = file_handler.read()
    file_handler.close()

    file_rm = Popen(["rm", "codes/tmp.cc", "codes/tmp.err"])

    return render_template('errors.html', errors=err.decode('utf-8'))

if __name__ == '__main__':
    app.run()
