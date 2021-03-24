from flask import Flask, render_template
import csv

app = Flask(__name__)
application = app


def convert_to_dict(filename):
    datafile = open(filename, newline='')
    # create DictReader object
    my_reader = csv.DictReader(datafile)
    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

animal_list = convert_to_dict('final.csv')


@app.route('/')
def index():
    return render_template('index.html', list=animal_list)


@app.route('/animals/<num>')
def animals(num):
    animal = animal_list[int(num) - 1]
    return render_template('animals.html', animal=animal)




if __name__ == '__main__':
    app.run(debug=True)
