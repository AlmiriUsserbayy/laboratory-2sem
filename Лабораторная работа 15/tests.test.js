import { saveTasks, loadTasks } from "./storage.js";

test("Сохранение и загрузка списка работает", () => {
  const sample = ["task1", "task2"];
  saveTasks(sample);
  expect(loadTasks()).toEqual(sample);
});
