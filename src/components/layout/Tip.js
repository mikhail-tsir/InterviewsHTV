import React, { Component } from 'react';
import PropTypes from 'prop-types';

export default class Tip extends Component{

	constructor(props){
		super(props)
		this.state = {
			displayProp: 'Good Job!',
		}
				
	}
	
getData = () => {
    void(fetch('http://localhost:5000/photo'))
    void(fetch('http://localhost:5000/stop'))
    if (this.state.displayProp=='Smile More!'){
    	 this.setState({displayProp: 'Remember Posture'})
    } else {
    	 this.setState({displayProp: 'Smile More!'})
    }
    fetch('http://localhost:5000/pdata')
      .then(response => response.json())
      .then(data => {
        this.setState({displayProp: 'Remember Posture'});
        // call getData() again in 5 seconds
        this.intervalID = setTimeout(this.getData.bind(this), 5000);
      });
  }
	
	
  componentDidMount() {
    this.getData()
  }
  
  doSomething(){
  	
  }


	render(){
		return(
		<div>
			<p style = {myStyle}>{this.state.displayProp}</p>
			<button onClick={this.doSomething()}></button>
		</div>
		);
	}
}



const myStyle ={
	position: 'fixed',
	marginTop: '10%',
	marginLeft: '37%'
}
