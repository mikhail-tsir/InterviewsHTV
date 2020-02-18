import React, { Component, useEffect } from 'react';
import Todos from './components/Todos';
import Header from './components/layout/Header';
import AddTodo from './components/AddTodo';
import uuid from 'uuid';
import textBubble from './textBubble.png';
import Tip from './components/layout/Tip';
import Stats from './Stats';
import ReactDOM from 'react-dom'; 
import axios from 'axios'
import logo from './ace.png';

import talk from './talk.png';
import notalk from './notalk.png';

import './App.css';

class App extends Component{
  state = {
    text: 'Smile More'
  }

  onClickButton1 = () => {
    this.setState({
      text: 'clicked 1'
    });
  }
    
    markComplete = (id) => {
        this.setState({todos: this.state.todos.map(todo => {
                if(todo.id === id){
                    todo.completed = !todo.completed
                }
                return todo;
            })});
    }
    
    delTodo = (id) => {
        this.setState({
                todos: [...this.state.todos.filter(todo => todo.id !== id)]
            });
    }
    
    //function for adding reminders?
    //Change AddTodos to an interface for interview tips
    //Find a way to update real time
    //<AddTodo addTodo = {this.addTodo}/>
    
    addTodo = (title) => {
        const newTodo = {
            id: uuid.v4(),
            title,
            completed: false   
        }
        this.setState({todos: [...this.state.todos, newTodo]});
    }
    
    //go to stats page
    goToStats(){
        axios.get('http://localhost:5000/audio')
        .then(response => console.log(response))       
        axios.get('http://localhost:5000/question')
        .then(response => console.log(response))                
    }
    
    getQuestion = () => {
        return 'Ace';
    }
    
    getTip = () => {
        return 'lol'   
    }

    render(){
        
        var bob = new XMLHttpRequest()
        
        bob.addEventListener('load', () =>{
            console.log(bob.responseText)  
        })
        

                
        return (
        <div className="App">
            <div className="Container">
                <Header name={this.getQuestion()}/>
                <Tip name={this.getTip()}/>
                 <Stats/>
                <img style={{width:'100%', marginTop:'-18%', marginLeft: '-22%'}}src={notalk} alt = "Person"/>
                <img style={{width:'40%', position: 'fixed', marginLeft: '-50%', marginTop:'1%'}}src={textBubble} alt = "textBubble"/>
                <button style={{ position: 'fixed', backgroundColor: '#1F75FE', fontSize: '16px', marginTop:'1%'}} onClick={this.goToStats}>Go to stats</button>
                <img style={{width:'20%', position: 'fixed', marginLeft: '0%', marginTop:'24%'}}src={logo} alt = "logo"/>
            </div>
        </div>
      );
    }
}





export default App;
