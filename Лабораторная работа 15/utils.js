export function filterTasks(tasks, keyword) {
  return tasks.filter(t =>
    t.toLowerCase().includes(keyword.toLowerCase())
  );
}
