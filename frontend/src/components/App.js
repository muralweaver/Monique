import React, { Component } from "react";
import { render } from "react-dom";
import Nav from "./Nav";
import LoginForm from "./LoginForm";
import Footer from "./Footer";
class App extends Component {
  // Component’s state is initialized and the logged_in property is determined based on whether or not a token can be found in local storage
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
      displayed_form: "",
      logged_in: localStorage.getItem("token") ? true : false,
      username: "",
    };
  }

  componentDidMount() {
    fetch("api/contact")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
    if (this.state.logged_in) {
      fetch("http://localhost:8000/api/current_user/", {
        headers: {
          // Each request to the API which requires the user to be authenticated will need to include this header, in this format, in order for the request to be processed.
          Authorization: `JWT ${localStorage.getItem("token")}`,
        },
      })
        .then((res) => res.json())
        .then((json) => {
          this.setState({ username: json.username });
        });
    }
  }
  handle_login = (e, data) => {
    e.preventDefault();
    fetch("http://localhost:8000/api/auth/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((res) => res.json())
      .then((json) => {
        localStorage.setItem("token", json.token);
        this.setState({
          logged_in: true,
          displayed_form: "",
          username: json.user.username,
        });
      });
  };
  // handle_signup = (e, data) => {
  //   e.preventDefault();
  //   fetch("http://localhost:8000/api/auth/", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json"
  //     },
  //     body: JSON.stringify(data)
  //   })
  //     .then(res => res.json())
  //     .then(json => {
  //       localStorage.setItem("token", json.token);
  //       this.setState({
  //         logged_in: true,
  //         displayed_form: "",
  //         username: json.username
  //       });
  //     });
  // };

  handle_logout = () => {
    localStorage.removeItem("token");
    this.setState({ logged_in: false, username: "" });
  };

  display_form = (form) => {
    this.setState({
      displayed_form: form,
    });
  };

  render() {
    let form;
    switch (this.state.displayed_form) {
      case "login":
        form = <LoginForm handle_login={this.handle_login} />;
        break;
      case "signup":
        form = <SignupForm handle_signup={this.handle_signup} />;
        break;
      default:
        form = null;
    }
    return (
      <div className="App">
        {this.state.data.map((contact) => {
          return (
            <li key={contact.id}>
              {contact.name} - {contact.email}
            </li>
          );
        })}
        <Nav
          logged_in={this.state.logged_in}
          display_form={this.display_form}
          handle_logout={this.handle_logout}
        />
        <h3>
          {this.state.logged_in
            ? `Hello, ${this.state.username}`
            : "Please Log In"}
        </h3>
        {form}
        <Footer/>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
