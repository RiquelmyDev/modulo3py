from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control #sempre que for usar uma variavel que for fazer intereção dentro desse metodo, use o GLOBAl, pq ele consegue fazer referencia com aquilo que está fora do medotodo
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
  task_id_control += 1
  tasks.append(new_task) 
  print(tasks)
  return jsonify({"mensagem": "Nova tarefa criada com sucesso!"})
  
@app.route('/tasks', methods=['GET'])
def get_tasks():
  tasks_list = [task.to_dict() for task in tasks]
  

  output = {
                "tasks": tasks_list,
                "total_tasks": len(tasks_list)
            }

  return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
    
  return jsonify({"mensagem": "Não foi possível encontrar a atividade"}), 404


# executando a rota
if __name__ == "__main__": #isso é para garantir, que só quando a gente execute ele de forma manual, vamos subir o servidor dessa forma
  app.run(debug=True)

