'use strict';

import React from 'react';
import { register } from './registry';

export class GlobalCalendarsPage extends React.Component {
    render(){
        return (
            <div>List of global calendars</div>);
    }
}

register('GlobalCalendars', GlobalCalendarsPage);