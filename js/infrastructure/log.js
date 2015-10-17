'use strict';

function log(f){
    window.console.log("GOLDFISH:" + f());
}

export default {
    info: log,
    debug: log,
    error: log,
    warn: log
};