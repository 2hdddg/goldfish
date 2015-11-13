'use strict';

import React from 'react';
import PageLink from '../components/pagelink';
import { StackedActionForm } from '../components/actionform';
import { open } from '../infrastructure/currentpage';
import ErrorPage from './errorpage';
import UserCalendarsPage from './usercalendarspage'

export let Error = ErrorPage;
export let UserCalendars = UserCalendarsPage;

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

                let user = actionResponse
                    .getEmbeddedFromEvent('created')
                    .filter(x => x.cls === 'User')[0];
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

export class CalendarTemplate extends React.Component {

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
        let template = this.props.resource;
        let createAction = template.getAction('create');
        let data = this._form.getData(createAction, this);

        this.setState({isBusy: true, message: ''});

        createAction.submit(data)
            .then(actionResponse => {
                this.setState({isBusy: false, message: ''});

                let calendar = actionResponse
                    .getEmbeddedFromEvent('created')
                    .filter(x => x.cls === 'Calendar')[0];
                open(calendar);
            })
            .catch(error => {
                this.setState({isBusy: false, message: 'Unknown error'});
            });
        event.preventDefault();
    }
    render(){
        let html;
        let template = this.props.resource;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            let createAction = template.getAction('create');
            html = this._form.htmlFormForAction(
                createAction, 'Whatever.', 'Register', (usage, fieldname) => fieldname, this._submit);
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


export class User extends React.Component {
    render(){
        return <span>User page!</span>;
    }
}

export class Calendar extends React.Component {
    render(){
        return <span>Calendar page...</span>;
    }
}