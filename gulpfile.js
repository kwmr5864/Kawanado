var gulp = require('gulp');
var concatCss = require('gulp-concat-css');
var cssmin = require('gulp-cssmin');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var runSequence = require('run-sequence');

gulp.task('concatCss', function () {
    gulp.src([
        'node_modules/bootstrap/dist/css/bootstrap.css',
    ])
    .pipe(concatCss('libs.min.css'))
    .pipe(cssmin())
    .pipe(gulp.dest('kawanado/app/static/css'));
});

gulp.task('concatJs', function () {
    gulp.src([
        'node_modules/bootstrap/dist/js/bootstrap.js',
    ])
    .pipe(concat('libs.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('kawanado/app/static/js'));
});

gulp.task('concat', function () {
    runSequence('concatCss', 'concatJs')
});

gulp.task('default', function () {
});