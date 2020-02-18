import React, { Component } from 'react';
import PropTypes from 'prop-types';

export class TodoItem extends Component{
	getStyle = () => {
		return{
			textDecoration: this.props.todo.completed ? 'line-through' : 'none'
		}
	}
	
	markComplete = (e) => {
		console.log(this.props)
	}

	render(){	
		const { id, title } = this.props.todo;
	
		return(
			<div style={this.getStyle()}>
				<p>
					<input type="checkbox" onChange={this.props.markComplete.bind
					(this, id)}/> {' '}
					{title}
					<button onClick={this.props.delTodo.bind(this, id)} style={btnStyle}>x</button>
				</p>
			</div>
		)
	}
}

TodoItem.propTypes = {
	todo: PropTypes.object.isRequired
}

const btnStyle = {
	background: 'red',
	color: 'white',
	border: 'none',
	padding: '5px 10px',
	borderRadius: '50%',
	cursor: 'pointer',
}


export default TodoItem;