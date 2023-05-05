import React from "react";
import Nav from 'react-bootstrap/Nav';

const NavBarComponent = () => {
    // console.log
    return (
        <Nav className="mb-1"
            activeKey="/home"
            onSelect={(selectedKey) => alert(`selected ${selectedKey}`)}
        >
            <Nav.Item>
                <Nav.Link href="/home"><h2 className="text-info">Steam Rec</h2></Nav.Link>
            </Nav.Item>
        </Nav>
    )
};

export default NavBarComponent;