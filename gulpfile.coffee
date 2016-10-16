gulp = require 'gulp'
concatCss = require 'gulp-concat-css'
cssmin = require 'gulp-cssmin'
concat = require 'gulp-concat'
uglify = require 'gulp-uglify'
runSequence = require 'run-sequence'

BASE_PATH = 'node_modules'
DEST_PATH = 'kawanado/app/static'

gulp.task 'concatCss', ->
    gulp.src [
        "${BASE_PATH}/bootstrap/dist/css/bootstrap.css",
    ]
    .pipe concatCss 'css/libs.min.css'
    .pipe cssmin()
    .pipe gulp.dest DEST_PATH

gulp.task 'concatJs', ->
    gulp.src [
        "${BASE_PATH}/bootstrap/dist/js/bootstrap.js",
    ]
    .pipe concat 'js/libs.min.js'
    .pipe uglify()
    .pipe gulp.dest DEST_PATH

gulp.task 'concat', ->
    runSequence 'concatCss', 'concatJs'

gulp.task 'default', ->
