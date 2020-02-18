import React from 'react';

function Header(props){
	return (
		<header style={headerStyle}>
			<h1>{props.name}</h1>
		</header>
	)
}

const headerStyle = {
	background: '#333',
	color: 'white',
	textAlign: 'center',
	padding: '10px'
}

export default Header