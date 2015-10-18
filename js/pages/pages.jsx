'use strict';

import React from 'react';
import { StackedActionForm } from '../components/actionform'
import { open } from '../infrastructure/currentpage'

export class UserTemplate extends React.Component {

    constructor(){
        super();
        this.state = {
            isBusy: false,
            validationMessage: ''
        };
        this._form = new StackedActionForm();
        this._submit = this._submit.bind(this);
    }
    _submit(event){
        let userTemplate = this.props.resource;
        let createAction = userTemplate.getAction('create');
        let data = this._form.getData(createAction, this);

        this.setState({isBusy: true, message: ''});

        createAction.submit(data)
            .then(actionResponse => {
                this.setState({isBusy: false, message: ''});
                let affected = actionResponse.getAffectedFromEvent('logged_in');
                let userRef = affected.filter(x => x.refcls === 'User')[0];
                let user = actionResponse.getEmbeddedFromRef(userRef.ref);
                let calendars_link = user.getLink('calendars');
                open(calendars_link);
            })
            .catch(error => {
                this.setState({isBusy: false, message: 'Unknown error'});
            });
        event.preventDefault();
    }
    render(){
        let html;
        let userTemplate = this.props.resource;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            let createAction = userTemplate.getAction('create');
            html = this._form.htmlFormForAction(
                createAction, 'Please register.', 'Register', (usage, fieldname) => fieldname, this._submit);
        }

        return (
            <div>{html}<span>{this.state.message}</span></div>);
    }
}

export class GlobalCalendars extends React.Component {
    render(){
        return (
            <div>List of global calendars</div>);
    }
}

export class UserCalendars extends React.Component {
    render(){
        return (
            <div>List of users calendars</div>);
    }
}