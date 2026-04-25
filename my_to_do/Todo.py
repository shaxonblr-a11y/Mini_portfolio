todo='tasks.txt'

def load_task(todo):
    try:
        with (open(todo, 'r', encoding='utf-8') as f):
            lines=f.readlines()
            tasks=[]
            for i in lines:
                i=i.strip()
                parts=i.split('|')
                if parts[0] == "1":
                    done = True
                else:
                    done=False
                description=parts[1]
                dict_tasks={'description':description,'done':done}
                tasks.append(dict_tasks)
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, todo):
    with open(todo, 'w',encoding='utf-8')as f:
        for task in tasks:
            if task['done']:
                status_str='1'
            else:
                status_str='0'
            l=status_str+'|'+ task['description'] +'\n'
            f.write(l)

def show_tasks(tasks):
    if len(tasks)==0:
        print('Список дел пуст')
        return
    else:
        for number,task in enumerate(tasks, start=1):
            if task['done']:
                icon='[X]'
            else:
                icon='[]'
            print(f"{number}. {icon} {task['description']}")


def add_task(tasks,todo):
    text=input('Введите новую задачу:').strip()
    if len(text)==0:
        print('Задача не может быть пустой')
        return
    new_task = {"description": text, "done": False}
    tasks.append(new_task)
    save_tasks(tasks,todo)
    print('Задача добавлена!')


def mark_done(tasks, todo):
    show_tasks(tasks)
    try:
        choice = int(input('Введите номер задачи которую хотите отметить выполненной:'))
        task_number = choice
    except ValueError:
        print('Ошибка')
        return
    if task_number < 1 or task_number > len(tasks):
        print('Ошибка')
        return
    ind_number=task_number -1
    tasks[ind_number]['done']=True
    save_tasks(tasks,todo)
    print('Задача отмечена как выполненная')


def delete_task(tasks, todo):
    show_tasks(tasks)
    try:
        choice_delete=int(input('Введите номер задачи которую хотите удалить:'))
        number_delete = choice_delete
    except ValueError:
        print('Ошибка')
        return
    if number_delete < 1 or number_delete>len(tasks):
        print('Ошибка')
        return
    ind_number = number_delete - 1
    del tasks[ind_number]
    save_tasks(tasks,todo)
    print('Задача удалена.')


if __name__=="__main__":
        tasks=load_task(todo)
        while True:
            print('1. Показать задачи')
            print('2. Добавить задачу')
            print('3. Отметить задачу выполненной')
            print('4. Удалить задачу')
            print('5. Выйти')
            choice=input('Выберите действие: ')
            if choice=='1':
                show_tasks(tasks)
            elif choice=='2':
                add_task(tasks,todo)
            elif choice=='3':
                mark_done(tasks,todo)
            elif choice=='4':
                delete_task(tasks,todo)
            elif choice=='5':
                break
            else:
                print('Неверная команда попробуй снова.')





