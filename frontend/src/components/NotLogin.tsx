import "bootstrap/dist/css/bootstrap.min.css";
import React, { useContext } from "react";
import { Button, Card, CardTitle, Row, Col } from "reactstrap";
import { getJwtAccessToken, login } from "../api/auth";
import { LoginContext } from "../App";

export default function NotLogin(): React.JSX.Element {
  const { setIsLogin } = useContext(LoginContext);
  const handleSignIn = async (e: any) => {
    e.preventDefault();
    const loginStatus: boolean = Boolean(login());
    setIsLogin(loginStatus);
  };
  const handleTest = async (e: any) => {
    e.preventDefault();
    getJwtAccessToken();
  };

  return (
    <div>
      <Row>
        <Col sm="6">
          <Card body>
            <CardTitle tag="h5">This is Login</CardTitle>
            <Button color="primary" onClick={(e: any) => handleSignIn(e)}>
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
        <Col sm="6">
          <Card body>
            <CardTitle tag="h5">This is Test</CardTitle>
            <Button onClick={(e: any) => handleTest(e)}>Test</Button>
          </Card>
        </Col>
      </Row>
    </div>
  );
}
