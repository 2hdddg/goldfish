'use strict';

import React from 'react';

var LoginForm = React.createClass({
    getInitialState: function(){
        return {
            isBusy: false,
            message: ''
        };
    },
    _submit: function(event){
        let username = React.findDOMNode(this.refs.username).value.trim();
        let password = React.findDOMNode(this.refs.password).value.trim();

        this.setState({isBusy: true});
        let application = this.props.application;

        application.login(username, password)
            .then(() => {
                this.setState({isBusy: false, message: ''});
                let requestClose = this.props.requestClose;
                if (requestClose){
                    requestClose();
                }
            })
            .catch(error => {
                if (error.response && error.response.status === 401){
                    this.setState({isBusy: false, message: 'Wrong username or password'});
                }
                else{
                    this.setState({isBusy: false, message: 'Unknown error'});
                    throw error;
                }
            });
        event.preventDefault();
    },
    render: function(){
        let html;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            html = (<form className="pure-form">
                        <fieldset>
                            <legend>Log in</legend>
                            <label for="email">Email</label>
                            <input id="email" type="email" placeholder="Your email" ref="username" />
                            <label for="password">Password</label>
                            <input id="password" type="password" placeholder="Password" ref="password" />
                            <button className="pure-button pure-button-primary" onClick={this._submit}>Log in</button>
                        </fieldset>
                        <span>{this.state.message}</span>
                    </form>);
        }
        return html;
    }
});

export default LoginForm;