'use strict';

import React from 'react';
import { register } from './registry';

export default class ErrorPage extends React.Component {
    render(){
        return <span>Error</span>;
    }
}

register('Error', ErrorPage);