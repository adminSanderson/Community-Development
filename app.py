from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


conn = sqlite3.connect('projects_db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS projects
                  (name TEXT, concept TEXT, audience TEXT, benefits TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS comments
                  (project_id INTEGER, comment TEXT)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    conn = sqlite3.connect('projects_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    project_list = cursor.fetchall()
    conn.close()
    return render_template('projects.html', projects=project_list)

@app.route('/project/<int:project_id>')
def project(project_id):
    conn = sqlite3.connect('projects_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE rowid=?', (project_id,))
    project = cursor.fetchone()
    cursor.execute('SELECT comment FROM comments WHERE project_id=?', (project_id,))
    comments_list = cursor.fetchall()
    conn.close()
    return render_template('project.html', project=project, comments=comments_list, project_id=project_id)

@app.route('/project/<int:project_id>/add_comment', methods=['POST'])
def add_comment(project_id):
    comment = request.form['comment']
    conn = sqlite3.connect('projects_db.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments VALUES (?, ?)', (project_id, comment))
    conn.commit()
    conn.close()
    return redirect(f'/project/{project_id}')

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form['name']
        concept = request.form['concept']
        audience = request.form['audience']
        benefits = request.form['benefits']
        
        conn = sqlite3.connect('projects_db.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO projects VALUES (?, ?, ?, ?)', (name, concept, audience, benefits))
        conn.commit()
        conn.close()
        
        return redirect('/projects')
    
    return render_template('create_project.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    