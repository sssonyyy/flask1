import pickle

import numpy as np
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Лаба 1", "url": "p_knn"},
        {"name": "Лаба 2", "url": "lab2"},
        {"name": "Лаба 3", "url": "lab3"},
        {"name": "Лаба 4", "url": "lab4"}]

loaded_model_knn = pickle.load(open('model/Iris_pickle_file', 'rb'))
loaded_model_line = pickle.load(open('model/pickle2', 'rb'))
loaded_model_log = pickle.load(open('model/logistic_model', 'rb'))

@app.route("/")
def index():
    return render_template('index.html', title="Лабораторные работы, выполненные ФИО", menu=menu)


@app.route("/p_knn", methods=['POST', 'GET'])
def f_lab1():
    if request.method == 'GET':
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),
                           float(request.form['list4'])]])
        pred = loaded_model_knn.predict(X_new)
        return render_template('lab1.html', title="Метод k -ближайших соседей (KNN)", menu=menu,
                               class_model="Это: " + pred)

@app.route("/lab2", methods=['POST', 'GET'])
def f_linear():
    if request.method == 'GET':
        return render_template('lab2.html',
                               title="Линейная регрессия",
                               menu=menu,
                               )
    if request.method == 'POST':
        x_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),]])
        pred = loaded_model_line.predict(x_new)
        return render_template('lab2.html',
                               title="Линейная регрессия",
                               menu=menu,
                               class_model=f"Ваш размер обуви: {pred[0]}",
                               )
@app.route("/lab3",  methods=['POST', 'GET'])
def f_lab3():
    if request.method == 'GET':
        return render_template('lab3.html', title="Логистическая регрессия", menu=menu, class_model='')
    if request.method == 'POST':
        X_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),
                           float(request.form['list4']),
                           float(request.form['list5']),
                           float(request.form['list6']),
                           float(request.form['list7'])
                           ]])
        pred = loaded_model_log.predict(X_new)
        return render_template('lab3.html', title="Логистическая регрессия", menu=menu,
                               class_model=f"Это: {pred[0]}")
@app.route("/lab4", methods=['POST', 'GET'])
def f_tree():
    if request.method == 'GET':
        return render_template('lab4.html',
                               title="Бинарное дерево",
                               menu=menu,
                               )
    if request.method == 'POST':
        x_new = np.array([[float(request.form['list1']),
                           float(request.form['list2']),
                           float(request.form['list3']),]])
        pred = loaded_model_line.predict(x_new)
        return render_template('lab4.html',
                               title="Бинарное дерево",
                               menu=menu,
                               class_model=f"Сложность предмета: {pred[0]}",)


if __name__ == "__main__":
    app.run(debug=True)
