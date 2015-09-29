'use strict';

import React from 'react';

var LoginForm = React.createClass({
    getInitialState: function(){
        return {
            isBusy: false,
            message: ''
        };
    },
    _submit: function(){
        let username = React.findDOMNode(this.refs.username).value.trim();
        let password = React.findDOMNode(this.refs.password).value.trim();

        this.setState({isBusy: true});
        let application = this.props.application;

        application.login(username, password)
            .then(() => {
                this.setState({isBusy: false, message: ''});
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
    },
    render: function(){
        let html;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            html = (<form>
                        <h1>Login</h1>
                        <input type="text" placeholder="Your email" ref="username" /><br />
                        <input type="password" placeholder="Password" ref="password" /><br />
                        <input type="button" value="Login" onClick={this._submit} />
                        <span>{this.state.message}</span>
                    </form>);
        }
        return html;
    }
});

export default LoginForm;