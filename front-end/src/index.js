import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/dist/jquery.min.js'
import 'popper.js/dist/popper.min.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import {
  Row, Col, Card, CardBody, CardTitle, CardText
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
class ContentItem extends React.Component{
  render(){
    return(
      <Row className="content">
        <Col xs="6">
          <Card>
            <CardBody>
              <CardTitle>
                {this.props.item.title}
              </CardTitle>
              <CardText>
                {this.props.item.description}
              </CardText>
            </CardBody>
          </Card>
        </Col>
      </Row>
    )
  }
}


ReactDOM.render(
  <ApiTest/>,
  document.getElementById('root')
);
