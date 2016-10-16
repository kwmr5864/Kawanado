gulp = require 'gulp'
concatCss = require 'gulp-concat-css'
cssmin = require 'gulp-cssmin'
concat = require 'gulp-concat'
uglify = require 'gulp-uglify'
coffee = require 'gulp-coffee'
runSequence = require 'run-sequence'

BASE_PATH = 'node_modules'
STATIC_PATH = 'kawanado/app/static'
CSS_PATH = "#{STATIC_PATH}/css"
JS_PATH = "#{STATIC_PATH}/js"
RESOURCE_PATH = 'resources'

gulp.task 'concatCss', ->
    gulp.src [
        "#{BASE_PATH}/bootstrap/dist/css/bootstrap.css",
    ]
    .pipe concatCss 'libs.min.css'
    .pipe cssmin()
    .pipe gulp.dest CSS_PATH

gulp.task 'concatJs', ->
    gulp.src [
        "#{BASE_PATH}/bootstrap/dist/js/bootstrap.js",
        "#{BASE_PATH}/vue/dist/vue.min.js",
    ]
    .pipe concat 'libs.min.js'
    .pipe uglify()
    .pipe gulp.dest JS_PATH

gulp.task 'concat', ->
    runSequence 'concatCss', 'concatJs'

gulp.task 'coffee', ->
    gulp.src "#{RESOURCE_PATH}/coffee/**/*.coffee"
    .pipe coffee({bare: true})
    .pipe concat 'script.min.js'
    .pipe uglify()
    .pipe gulp.dest JS_PATH

gulp.task 'default', ->
    runSequence 'coffee'
