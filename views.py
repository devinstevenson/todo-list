from app import app
from flask import render_template, request, redirect, url_for, flash
from models import Category, Task, Priority, db


@app.route('/')
def list_all():
    return render_template('list.html',
                           categories=Category.query.all(),
                           tasks=Task.query.all())
    # join(Priority).order_by(Priority.value.desc())

@app.route('/<name>')
def list_tasks(name):
    category = Category.query.filter_by(name=name).first()
    tasks = Task.query.filter_by(category=category).all(),
    # .join(Priority).order_by(Priority.value.desc()),
    return render_template('list.html', tasks=tasks, categories=Category.query.all())

@app.route('/new-task', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        category = Category.query.filter_by(id=request.form['category']).first()
        # priority = Priority.query.filter_by(id=request.form['priority']).first()
        # task = Task(category=category, priority=priority, description=request.form['description'])
        task = Task(category=category, description=request.form['description'])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list_all'))
    else:
        return render_template('new-task.html',
                               page='new-task',
                               categories=Category.query.all(),
                               # priorities=Priority.query.all()
        )

@app.route('/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if request.method == 'GET':
        return render_template('new-task.html', task=task,
                               categories=Category.query.all())
        # priorities=Priority.query.all()

    else:
        category = Category.query.filter_by(id=request.form['category']).first()
        # priority = Priority.query.filter_by(id=request.form['priority']).first()
        description = request.form['description']
        task.category = category
        # task.priority = priority
        task.description = description
        db.session.commit()
        return redirect('/')

@app.route('/new-category', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        category = Category(name=request.form['category'])
        db.session.add(category)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new-category.html', page='new-category.html')

@app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get(category_id)
    if request.method == 'GET':
        return render_template('new-category.html', category=category)
    else:
        category_name = request.form['category']
        category.name = category_name
        db.session.commit()
        return redirect('/')

@app.route('/delete-category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if request.method == 'POST':
        category = Category.query.get(category_id)
        task = Task.query.filter_by(category_id=category_id)
        if not task.first():
            db.session.delete(category)
            db.session.commit()
        else:
            flash('You have Tasks in that category. Remove them first.')
        return redirect('/')

@app.route('/delete-task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if request.method == 'POST':
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect('/')

@app.route('/mark-done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    if request.method == 'POST':
        task = Task.query.get(task_id)
        task.is_done = True
        db.session.commit()
        return redirect('/')
