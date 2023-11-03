import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { Button, Card, CardTitle, Row, Col } from "reactstrap";
import { PropsInterface } from "../interfaces/props";
import { login, signin } from "../utils/auth";

export default function NotLogin(props: PropsInterface): React.JSX.Element {
  const handleLogin = () => {
    props.setIsLogin(true);
  };
  const handleSignIn = () => {
    props.setIsLogin(true);
  };
  return (
    <div>
      <Row>
        <Col sm="6">
          <Card body>
            <CardTitle tag="h5">This is Login</CardTitle>
            <Button color="primary" onClick={() => handleLogin()}>
              Login
            </Button>
          </Card>
        </Col>
        <Col sm="6">
          <Card body>
            <CardTitle tag="h5">This is Signin</CardTitle>
            <Button>Signin</Button>
          </Card>
        </Col>
      </Row>
    </div>
  );
}
