'use strict';

var gulp = require('gulp');
var browserify = require('browserify');
var babelify = require('babelify');
var shim = require('browserify-shim')
var source = require('vinyl-source-stream');
var glob = require('glob');

gulp.task('build', function () {
    // All pages are entries to simplify
    // creation of new page..
    var entries = glob.sync('./js/pages/**/*.jsx');
    entries.push('js/export.js');

    browserify({
        entries: entries,
        extensions: ['.jsx'],
        debug: true
    })
    .transform([babelify, shim])
    .bundle()
    .pipe(source('goldfish.js'))
    .pipe(gulp.dest('static/'));
});

gulp.task('default', ['build']);