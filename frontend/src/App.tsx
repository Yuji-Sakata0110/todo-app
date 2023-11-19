import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect, Context, createContext } from "react";
import { Container } from "reactstrap";
import Navigation from "./components/Navigation";
import Login from "./components/Login";
import NotLogin from "./components/NotLogin";
import { LoginContextInterface } from "./interfaces/app";

const LoginContextInitValue: LoginContextInterface = {
  isLogin: false,
  setIsLogin: () => {},
};

export const LoginContext: Context<LoginContextInterface> =
  createContext<LoginContextInterface>(LoginContextInitValue);

export default function App(): React.JSX.Element {
  const [isLogin, setIsLogin] = useState<boolean>(false);

  return (
    <LoginContext.Provider value={{ isLogin, setIsLogin }}>
      <div className="App">
        <Container>
          <Navigation isLogin={isLogin} setIsLogin={setIsLogin} />
          {isLogin ? <Login /> : <NotLogin />}
        </Container>
      </div>
    </LoginContext.Provider>
  );
}
