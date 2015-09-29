'use strict';

var gulp = require('gulp');
var browserify = require('browserify');
var babelify = require('babelify');
var shim = require('browserify-shim')
var source = require('vinyl-source-stream');

gulp.task('build', function () {
  browserify({
    entries: 'js/export.js',
    extensions: ['.jsx'],
    debug: true
  })
  .transform([babelify, shim])
  .bundle()
  .pipe(source('goldfish.js'))
  .pipe(gulp.dest('static/'));
});

gulp.task('default', ['build']);