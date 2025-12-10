export function renderList(listElem, tasks) {
  listElem.innerHTML = "";

  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.className = "task-item";

    li.innerHTML = `
      <span>${task.text} <small>${task.time || ""}</small></span>
      <button class="delete-btn" data-index="${index}">Удалить</button>
    `;

    listElem.appendChild(li);
  });
}
