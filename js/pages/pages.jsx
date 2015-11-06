'use strict';

import React from 'react';
import PageLink from '../components/pagelink';
import { StackedActionForm } from '../components/actionform';
import { open } from '../infrastructure/currentpage';
import { ErrorPage } from './error';

export let Error = ErrorPage;

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

export class UserCalendars extends React.Component {
    render(){
        let resource = this.props.resource;
        let calendars = resource.property('list', []);

        let menuitemClasses = "pure-menu-link";
        let menuitems = [];
        if (resource.hasLink('calendarTemplate')){
            let link = resource.getLink('calendarTemplate');
            menuitems.push(
                <li key="createcalendar" className="pure-menu-item">
                    <PageLink classes={menuitemClasses} key="createcalendar" text="New calendar" link={link} />
                </li>);
        }
        let menuHtml =
            <ul className="pure-menu-list" style={{float: 'right'}}>
                {menuitems}
            </ul>;

        let content = null;
        if (calendars.length === 0){
            content = (<div><span>No calendars, yet!</span><div>{menuHtml}</div></div>);
        }
        else{
            let calendarsHtml = [];
            calendars.forEach(c => {
                let html = (<span>A calendar</span>);
                calendarsHtml.push(html);
            });
            content = (<div><h1>List of users calendars</h1><div>{calendarsHtml}</div><div>{menuHtml}</div></div>);
        }
        return content;
    }
}