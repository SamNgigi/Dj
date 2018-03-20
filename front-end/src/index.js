import React from 'react';
import ReactDOM from 'react-dom';

class ApiTest extends React.Component{
  componentDidMount(){
    this.getItems();
  }
  getItems(){
    fetch('http://127.0.0.1:8000/Apis/item/')
     .then(results => results.json())
     .then(results=> console.log(results));
  }
  render(){
    return null;
  }
}

ReactDOM.render(
  <ApiTest/>,
  document.getElementById('root')
);
