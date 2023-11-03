import axios from "axios";
import { todoInterface } from "../interfaces/todo";

export const getTodos = async (
  setTodoItems: React.Dispatch<React.SetStateAction<todoInterface[]>>,
  setCompletedItems: React.Dispatch<React.SetStateAction<todoInterface[]>>
): Promise<void> => {
  try {
    await axios.get("http://localhost:8000/api/").then((res) => {
      const todos = res.data.filter((item: todoInterface) => {
        return item.completed === false;
      });
      const completedTodos = res.data.filter((item: todoInterface) => {
        return item.completed === true;
      });
      setTodoItems(todos);
      setCompletedItems(completedTodos);
    });
  } catch (error) {
    console.error("エラー:", error);
  }
};

export const postTodo = async (inputText: string): Promise<void> => {
  try {
    await axios.post("http://localhost:8000/api/", {
      title: inputText,
      description: "description",
      completed: false,
    });
  } catch (error) {
    console.error("エラー:", error);
  }
};

export const handleCheckboxChange = (todoItem: todoInterface): void => {
  // update
  const _update = async (): Promise<void> => {
    await axios.put(`http://localhost:8000/api/${todoItem.id}/`, {
      title: todoItem.title,
      description: todoItem.description,
      completed: !todoItem.completed,
    });
  };

  _update();
};
