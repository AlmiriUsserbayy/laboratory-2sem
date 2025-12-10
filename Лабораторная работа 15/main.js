import { saveTasks, loadTasks } from "./storage.js";
import { renderList } from "./ui.js";

let tasks = loadTasks();

const input = document.getElementById("taskInput");
const timeInput = document.getElementById("taskTime");
const addBtn = document.getElementById("addBtn");
const listElem = document.getElementById("taskList");
const themeToggle = document.getElementById("themeToggle");

// --- Удаление задачи ---
function removeTask(index) {
  tasks.splice(index, 1);
  saveTasks(tasks);
  renderList(listElem, tasks);
}

// --- Добавление задачи ---
addBtn.addEventListener("click", () => {
  const text = input.value.trim();
  const time = timeInput.value;

  if (!text) return;

  tasks.push({ text, time });
  saveTasks(tasks);

  input.value = "";
  timeInput.value = "";

  renderList(listElem, tasks);
});

renderList(listElem, tasks);

// --- Единый обработчик кликов (исправление бага!) ---
listElem.addEventListener("click", (event) => {
  if (event.target.classList.contains("delete-btn")) {
    const index = event.target.dataset.index;
    removeTask(Number(index));
  }
});

// --- Переключение темы ---
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

// --- Часы ---
function updateClock() {
  const now = new Date();
  document.getElementById("clock").textContent =
    now.toLocaleTimeString("ru-RU");
}
setInterval(updateClock, 1000);
updateClock();
