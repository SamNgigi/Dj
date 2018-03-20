import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/dist/jquery.min.js'
import 'popper.js/dist/popper.min.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import {
  Row, Col, Card, CardBody, CardTitle, CardText, CardImg
} from 'reactstrap'
import './index.css'
class ApiTest extends React.Component{
  constructor() {
    // Seems we need super() for our this.state to work.
    super();
    this.state = {
      'items': []
    }
  }
  componentDidMount(){
    this.getItems();
  }
  getItems() {
    fetch('http://127.0.0.1:8000/Apis/item/')
     .then(results => results.json())
     .then(results=> this.setState({'items':results}));
  }
  render(){
    return (

      <ul>
      <h1>Hii ndio shida</h1>
          {this.state.items.map(function (item, index) {
            return (
              <ContentItem item={item} key={index}/>
            )
          }
        )}
      </ul>
    );
  }
}

const ContentItem = ({item})=>(
  <Row className="content">
    <Col xs="3"></Col>
    <Col xs="12" sm="6">
      <Card>
        <CardImg top width="100%" src={item.image}></CardImg>
        <CardBody className="text-center">
          <CardTitle>
            {item.title}
          </CardTitle>
          <CardText>
            {item.description}
          </CardText>
        </CardBody>
      </Card>
    </Col>
    <Col xs="3"></Col>
  </Row>
)



ReactDOM.render(
  <ApiTest/>,
  document.getElementById('root')
);
