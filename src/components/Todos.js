import React, { Component } from 'react';
import TodoItem from './TodoItem';
import PropTypes from 'prop-types';

class Todos extends Component{
	render(){
			return this.props.todos.map((todo) => (
				<div style={{width: '50%', float: 'left'}}>
					<TodoItem key = {todo.id} todo={todo} markComplete={this.props.markComplete}
					delTodo={this.props.delTodo}/>
				</div>
			)
		);
	}
}

Todos.propTypes = {
	todos: PropTypes.array.isRequired
}

export default Todos;