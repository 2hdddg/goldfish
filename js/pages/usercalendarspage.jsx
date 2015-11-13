'use strict';

import React from 'react';
import PageLink from '../components/pagelink';

export default class UserCalendarsPage extends React.Component {
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
            calendars.forEach(calendar => {
                let ref = calendar.ref;
                let html =
                    <li key={ref}>
                        <PageLink text={calendar.property('name')} link={ref} />
                    </li>
                calendarsHtml.push(html);
            });
            content = (<div><h1>List of users calendars</h1><ul>{calendarsHtml}</ul><div>{menuHtml}</div></div>);
        }
        return content;
    }
}
