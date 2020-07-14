import React, { useState } from 'react';


class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      gameName: "",
      gameActive: false
    };
  }

  componentDidMount() {
    fetch("http://localhost:8000/1/get_game/")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            gameName: result.name
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, gameName } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>
            <p key={gameName}>
             Welcome to {gameName}!
            </p>
        </ul>
      );
    }
  }
}

export default Home;
