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
    global task_id_control # sempre que for usar uma variável que for fazer interação dentro desse método, use o GLOBAL, porque ele consegue fazer referência com aquilo que está fora do método
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

@app.route('/tasks/<int:id>', methods=['GET']) # R do CRUD
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
            
                        
    return jsonify({"mensagem": "Não foi possível encontrar a atividade"}), 404

"""# estudar a documentação https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing
@app.route('/user/<int:user_id>') # consigo receber os indicadores em ( string, int, float, path, uuid.)
def show_user(user_id):
    print(user_id)
    print(type(user_id))
    return "%s" % user_id"""

@app.route('/tasks/<int:id>', methods=["PUT"])    
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    print(task)        
    if task == None:
        return jsonify({"mensagem": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    print(task)        
    if task == None:
        return jsonify({"mensagem": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

# executando a rota
if __name__ == "__main__": # isso é para garantir, que só quando a gente execute ele de forma manual, vamos subir o servidor dessa forma
    app.run(debug=True)


def generate_random_password(length=12):
    """
    Gera uma senha aleatória com o comprimento especificado.
    
    :param length: Comprimento da senha (padrão é 12)
    :return: Senha aleatória gerada
    """
    # Define os caracteres que podem ser utilizados na senha
    characters = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha aleatória
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Exemplo de uso
senha = generate_random_password(16)
print(f"Senha gerada: {senha}")