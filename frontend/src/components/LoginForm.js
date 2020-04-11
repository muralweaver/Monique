import React from 'react';
import PropTypes from 'prop-types';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
class LoginForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };
  render() {
    return (
      <form onSubmit={e => this.props.handle_login(e, this.state)}>
        <h4>Log In</h4>
        <TextField id="standard-basic" label="Username"name="username" value={this.state.username} onChange={this.handle_change} />
        <TextField id="standard-basic" type="password" label="Password" name="password" value={this.state.password} onChange={this.handle_change} />
        <Button
            type="submit"
            variant="contained"
            color="primary">
            Log in
          </Button>
      </form>
    );
  }
}

export default LoginForm;

LoginForm.propTypes = {
  handle_login: PropTypes.func.isRequired
};