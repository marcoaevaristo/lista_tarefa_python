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
        
        # Cor para o card baseada na prioridade
        if priority == "Baixa":
            color = "green"
        elif priority == "Média":
            color = "yellow"
        else:
            color = "red"
        
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'color': color
        }
        tasks.append(task)
        return redirect(url_for('index'))

    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)
