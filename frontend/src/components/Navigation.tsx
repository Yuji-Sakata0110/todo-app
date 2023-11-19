import React, { useState } from "react";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from "reactstrap";
import { PropsNavigationInterface } from "../interfaces/props";

export default function Navigation(
  props: PropsNavigationInterface
): React.JSX.Element {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const toggle = (): void => setIsOpen(!isOpen);
  const handleSignout = (): void => {
    props.setIsLogin(false);
  };

  return (
    <Navbar>
      <NavbarBrand href="/">reactstrap</NavbarBrand>
      <NavbarToggler onClick={toggle} />
      <Collapse isOpen={isOpen} navbar>
        <Nav className="me-auto" navbar>
          <NavItem>
            <NavLink href="/">Home</NavLink>
          </NavItem>
          <NavItem>
            {props.isLogin && (
              <NavLink href="/" onClick={() => handleSignout()}>
                Signout
              </NavLink>
            )}
            {!props.isLogin && (
              <NavLink href="/" onClick={() => handleSignout()}>
                login
              </NavLink>
            )}
          </NavItem>
        </Nav>
      </Collapse>
    </Navbar>
  );
}
