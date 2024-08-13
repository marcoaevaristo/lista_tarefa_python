from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        
        if priority == "Baixa":
            color = "green"
        elif priority == "Média":
            color = "yellow"
        else:
            color = "red"
        
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'color': color,
            'completed': False
        }
        tasks.append(task)
        return redirect(url_for('index'))

    return render_template('add_task.html')

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['due_date'] = request.form['due_date']
        task['priority'] = request.form['priority']

        if task['priority'] == "Baixa":
            task['color'] = "green"
        elif task['priority'] == "Média":
            task['color'] = "yellow"
        else:
            task['color'] = "red"

        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['completed'] = True
    return redirect(url_for('completed_tasks'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/completed_tasks')
def completed_tasks():
    completed_tasks = [task for task in tasks if task['completed']]
    return render_template('completed_tasks.html', tasks=completed_tasks)

if __name__ == '__main__':
    app.run(debug=True)

