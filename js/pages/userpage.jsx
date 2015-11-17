'use strict';

import React from 'react';
import { register } from './registry';

export class UserPage extends React.Component {
    render(){
        return <span>User page!</span>;
    }
}

register('User', UserPage);