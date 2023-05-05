import React from "react";
import Card from 'react-bootstrap/Card';
import Table from 'react-bootstrap/Table';

const userTopTen = require('./new_user_result.json');



const NewuserComponent = () => {
    const indexes = [];
    for (let i = 0; i < 10; i++) {
        indexes.push(i);
    }
    return (
        <div className="mb-5">
            <Table striped bordered hover>
                <thead><h3 className="text-white">&nbsp;&nbsp;Welcome! Guess You like</h3></thead>
                <tbody>
                    <tr>
                        {indexes.map(idx => {
                            return (<td>
                                <Card className="bg-dark" style={{ height: '30rem', width: '24rem' }}>
                                    <Card.Img variant="top" src={userTopTen[idx][1]} style={{ height: '20rem', width: '24rem' }} alt="https://as2.ftcdn.net/v2/jpg/04/42/21/53/1000_F_442215355_AjiR6ogucq3vPzjFAAEfwbPXYGqYVAap.jpg"/>
                                    <Card.Body>
                                        <Card.Title className="text-white text-center">{userTopTen[idx][0]}</Card.Title>
                                    </Card.Body>
                                </Card>
                            </td>)
                        })}
                    </tr>
                </tbody>
            </Table>
        </div>
    )
};

export default NewuserComponent;