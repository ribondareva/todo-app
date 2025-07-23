from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Принудительное создание таблиц при запуске
with app.app_context():
    db.create_all()


# Главная страница (список задач)
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


# Добавление задачи
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        priority = request.form.get('priority', 1, type=int)
        new_task = Task(title=title, done=False, priority=priority)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))


# Изменение статуса задачи
@app.route('/update/<int:task_id>')
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect(url_for('index'))


# Удаление задачи
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
