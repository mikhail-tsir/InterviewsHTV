import React, { Component } from 'react';

class Stats extends Component {
  intervalID;

  state = {
    data: [],
  }


  componentWillUnmount() {
    /*
      stop getData() from continuing to run even
      after unmounting this component. Notice we are calling
      'clearTimeout()` here rather than `clearInterval()` as
      in the previous example.
    */
    clearTimeout(this.intervalID);
  }

  render() {
    return (
      <div>
        Our Stats
      </div>
    );
  }
}

export default Stats