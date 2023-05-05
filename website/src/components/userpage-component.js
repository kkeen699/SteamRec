import React from "react";
import Card from 'react-bootstrap/Card';
import Table from 'react-bootstrap/Table';

const userTopTen = require('./user_0_result.json');
const userGenre = require('./user_0_genre.json')



const UserpageComponent = () => {
    console.log(userTopTen)
    const indexes = [];
    for (let i = 0; i < 6; i++) {
        indexes.push(i);
    }
    console.log(indexes)
    return (
        <div>
            {indexes.map(idx => {

                return (
                    <div>
                        <Genre games={userTopTen[idx]} genre={userGenre[idx]} />
                    </div>)
            })}
        </div>
    )
};

const Genre = (props) => {
    const indexes = [];
    for (let i = 0; i < 10; i++) {
        indexes.push(i);
    }
    return (
        <div className="mb-5">
            <Table striped bordered hover>
                <thead><h4 className="text-white">&nbsp;&nbsp;&nbsp;{props.genre}</h4></thead>
                <tbody>
                    <tr>
                        {indexes.map(idx => {
                            return (<td>
                                <Card className="bg-dark" style={{ height: '20rem', width: '18rem' }}>
                                    <Card.Img variant="top" src={props.games[idx][1]} style={{ height: '13rem', width: '18rem' }} title={props.games[idx][0]} alt={props.games[idx][0]} />
                                    <Card.Body>
                                        <Card.Title className="text-white text-center">{props.games[idx][0]}</Card.Title>
                                    </Card.Body>
                                </Card>
                            </td>)
                        })}
                    </tr>
                </tbody>
            </Table>
        </div>
    )
}
export default UserpageComponent;