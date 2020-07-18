import React, { useState } from 'react';
import { Cookies } from 'react-cookie';
import Welcome from './Welcome.js';

const cookies = new Cookies();
const DOMAIN = "http://localhost:8000";


// Game Status
const INACTIVE = 'INACTIVE'
const SHOW_WELCOME = 'SHOW_WELCOME'
const SHOW_QUESTION = 'SHOW_QUESTION'
const SHOW_LEADERBOARD = 'SHOW_LEADERBOARD'

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      gameName: "",
      gameStatus: INACTIVE,
      participantName: null,
      nameInput: "",
      showQuestion: false,
      showLeaderBoard: false,
      isHost: true,
    };
    this.setParticipantName = this.setParticipantName.bind(this);
    this.setNameInput = this.setNameInput.bind(this);
  }

  setParticipantName(e) {
    e.preventDefault();
    cookies.set('participantName', this.state.nameInput, { path: '/' });
    this.setState({
      participantName: this.state.nameInput
    });
    // this also needs to POST to create participant and return a participant id
  }

  setNameInput(e) {
    this.setState({
        nameInput: e.target.value
      });
  }

  componentDidMount() {
    if (cookies.get('participantName')) {
      this.setState({
        participantName: cookies.get('participantName')
      });
    }
    const gameId = window.location.pathname.split("/")[1];
    const getGameUrl = `${DOMAIN}/${gameId}/get_game/`;
    fetch(getGameUrl)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            gameName: result.name,
            gameStatus: result.status,
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
    const { error, isHost, isLoaded, gameStatus, gameName, participantName } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else if (!participantName && gameStatus == INACTIVE) {
      return (
          <div>
              <p>Please enter a name for yourself</p>
              <form onSubmit={this.setParticipantName}>
                <input
                  id="name-input"
                  onChange={this.setNameInput}
                  value={this.state.name}
                />
                <button>Submit</button>
              </form>
          </div>
      );
    } else {
      return <Welcome 
        gameName={gameName}
        participantName={participantName}
        isHost={isHost}
      />;
    }
  }
}

export default Home;
