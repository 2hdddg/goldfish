'use strict';

import React from 'react';

export default class ModalLink extends React.Component {
    constructor(){
        super();
        this.state = {isOpen:false, content: null};
        this._open = this._open.bind(this);
        this._close = this._close.bind(this);
    }

    _open(event){
        event.preventDefault();
        let content = this.props.getContent(
            () => this.setState({isOpen:false, content: null}));
        this.setState({isOpen:true, content});
    }

    _close(event){
        event.preventDefault();
        this.setState({isOpen:false, content: null});
    }

    render(){
        let link = <a href="#" className={this.props.classes} onClick={this._open}>{this.props.text}</a>;
        let modal;
        if (this.state.isOpen){
            let closeStyle = {
                'float': 'right',
                'fontSize': '28px'
            };
            modal =
                <div className="modalDialog">
                    <div>
                    <a style={closeStyle} href="#" onClick={this._close}>
                        <span className="typcn typcn-delete-outline"></span>
                    </a>
                    {this.state.content}
                    </div>
                </div>;
        }
        return (<div>{link}{modal}</div>);
    }
}