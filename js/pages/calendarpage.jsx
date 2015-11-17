'use strict';

import React from 'react';
import { register } from './registry';

export default class CalendarPage extends React.Component {
    render(){
        let calendar = this.props.resource;
        let name = calendar.property('name');
        let header = <h1>{name}</h1>;

        return <div>{header}</div>;
    }
}
register('Calendar', CalendarPage);