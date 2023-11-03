import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState } from "react";
import { Container } from "reactstrap";
import Navigation from "./components/Navigation";
import Login from "./components/Login";
import NotLogin from "./components/NotLogin";

export default function App(): React.JSX.Element {
  const [isLogin, setIsLogin] = useState<boolean>(false);
  return (
    <div className="App">
      <Container>
        <Navigation isLogin={isLogin} setIsLogin={setIsLogin} />
        {isLogin ? (
          <Login setIsLogin={setIsLogin} />
        ) : (
          <NotLogin setIsLogin={setIsLogin} />
        )}
      </Container>
    </div>
  );
}
