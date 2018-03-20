import React from 'react';
import ReactDOM from 'react-dom';

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
              <div key={index}>
                <h1>{item.title }</h1>
                <p>{item.description}</p>
              </div>
            )
          }
        )}
      </ul>
    )
  }
}

ReactDOM.render(
  <ApiTest/>,
  document.getElementById('root')
);
