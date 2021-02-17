
//selectors
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");

//EventListener
todoButton.addEventListener("click", addTodo);
todoList.addEventListener("click", deleteCheck);

//Functions

function addTodo(event){
    event.preventDefault();
    if (todoInput.value === '') {
      alert("You must write something!");
    }else{
      const todoDiv = document.createElement('div');
      todoDiv.classList.add("todo");
      const newTodo = document.createElement('li');
      newTodo.innerText = todoInput.value;
      newTodo.classList.add('todo-item');
      todoDiv.appendChild(newTodo);
      
      const checkedButton = document.createElement('button');
      checkedButton.innerText = 'Checked';
      checkedButton.classList.add("complete-btn");
      todoDiv.appendChild(checkedButton);

      const trashButton = document.createElement('button');
      trashButton.innerText = "Delete";
      trashButton.classList.add("trash-btn");
      todoDiv.appendChild(trashButton);
      //Append
      todoList.appendChild(todoDiv);
      todoInput.value = "";
    }
}

function deleteCheck(e){
  const item = e.target;

  if(item.classList[0] === "trash-btn"){
    const todo = item.parentElement;
    todo.remove();
  }

  if(item.classList[0] === "complete-btn"){
    const todo = item.parentElement;
    todo.classList.toggle("completed");
  }
}

