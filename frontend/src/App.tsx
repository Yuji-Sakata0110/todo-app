import "bootstrap/dist/css/bootstrap.min.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Button, Input, Label, FormGroup, Form } from "reactstrap";

export default function App(): React.JSX.Element {
  // todos
  const [todoItems, setTodoItems] = useState<todoInterface[]>([]);
  // completed
  const [completedItems, setCompletedItems] = useState<todoInterface[]>([]);
  // changeEvent
  const [inputText, setInputText] = useState<string>("");

  // todoItemsの状態が変更された時に実行する
  useEffect(() => {
    getTodos(setTodoItems, setCompletedItems);
  }, [todoItems]);

  // inputTextの値を変更
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
    setInputText(e.target.value);
  };

  // todoを追加する
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
    e.preventDefault();

    //バリデーションを通過した場合、todoに追加
    !validation(inputText) && postTodo(inputText);

    setInputText("");
  };

  return (
    <div className="App">
      <div className="row">
        <div className="col-md-6 col-sm-10 mx-auto p-0">
          <div className="card m-5 p-3">
            <h2>Add Todos</h2>
            <Form
              onSubmit={(e: React.FormEvent<HTMLFormElement>) => {
                handleSubmit(e);
              }}
            >
              <FormGroup>
                <Input
                  type="text"
                  className="mb-3"
                  value={inputText}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    handleChange(e)
                  }
                />
                <Button color="danger">Add</Button>
              </FormGroup>
            </Form>
          </div>
          <div className="card m-5 p-3">
            <h2>Todos</h2>
            <Form>
              <ul className="list-group list-group-flush">
                {todoItems.map((todoItem: todoInterface) => (
                  <div key={todoItem.id} className="todos">
                    <FormGroup check inline>
                      <Input
                        type="checkbox"
                        onChange={() => handleCheckboxChange(todoItem)}
                      />
                      <Label check>{todoItem.title}</Label>
                    </FormGroup>
                  </div>
                ))}
              </ul>
            </Form>
          </div>
          <div className="card m-5 p-3">
            <h2>Completed</h2>
            <ul className="list-group list-group-flush ms-3">
              {completedItems.slice(-10).map((completedItem: todoInterface) => (
                <li key={completedItem.id} className="completed m-2">
                  {completedItem.title}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

// react component 内部と切り離しても良い関数は下記に記述
interface todoInterface {
  id: number;
  title: string;
  description: string;
  completed: boolean;
}

const getTodos = async (
  setTodoItems: React.Dispatch<React.SetStateAction<todoInterface[]>>,
  setCompletedItems: React.Dispatch<React.SetStateAction<todoInterface[]>>
): Promise<void> => {
  try {
    await axios.get("http://localhost:8000/api/todos/").then((res) => {
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

const postTodo = async (inputText: string): Promise<void> => {
  try {
    await axios.post("http://localhost:8000/api/todos/", {
      title: inputText,
      description: "description",
      completed: false,
    });
  } catch (error) {
    console.error("エラー:", error);
  }
};

const handleCheckboxChange = (todoItem: todoInterface): void => {
  // update
  const _update = async (): Promise<void> => {
    await axios.put(`http://localhost:8000/api/todos/${todoItem.id}/`, {
      title: todoItem.title,
      description: todoItem.description,
      completed: !todoItem.completed,
    });
  };

  _update();
};

interface validationRuleInterface {
  isEmpty: RegExp;
}
const validationRules: validationRuleInterface = { isEmpty: /^\s*$/ };
const validation = (inputText: string): boolean => {
  if (validationRules.isEmpty.test(inputText)) {
    console.error("ValidationError: 空白でtodoを追加することができません。");
    return true;
  }
  return false;
};
