import React, { useState, useEffect, Dispatch, SetStateAction } from "react";
import { Button, Input, Label, FormGroup, Form } from "reactstrap";
import { todoInterface } from "../interfaces/todo";
import { PropsInterface } from "../interfaces/props";
import { validation } from "../utils/validation";
import { getTodos, postTodo, handleCheckboxChange } from "../api/todo";

export default function Login(props: PropsInterface): React.JSX.Element {
  const [todoItems, setTodoItems] = useState<todoInterface[]>([]);
  const [completedItems, setCompletedItems] = useState<todoInterface[]>([]);
  const [inputText, setInputText] = useState<string>("");

  useEffect(() => {
    getTodos(setTodoItems, setCompletedItems);
  }, [todoItems]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
    setInputText(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>): void => {
    e.preventDefault();

    !validation(inputText) && postTodo(inputText);

    setInputText("");
  };
  return (
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
  );
}
