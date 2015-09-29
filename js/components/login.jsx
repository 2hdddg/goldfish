'use strict';

import React from 'react';
import LoginForm from './loginform';

var Login = React.createClass({
    getInitialState: function(){
        return {
            showForm: false,
        };
    },
    hideForm: function(){
        this.setState({showForm: false});
    },
    showForm: function(){
        this.setState({showForm: true});
    },
    render: function(){
        if (this.state.showForm){
            return (<div>
                <LoginForm application={this.props.application}>
                </LoginForm>
                <input type="button" value="Cancel" onClick={this.hideForm}></input>
            </div>);
        }
        else{
            return (<input type="button" value="Log in" onClick={this.showForm}/>);
        }
    }
});

export default Login;