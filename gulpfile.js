var gulp = require('gulp'),
    jsonlint = require("gulp-jsonlint"),
    yamllint = require('gulp-yaml-validate');

gulp.task('lint', function() {
    // JSON
    gulp.src("data/*.json")
        .pipe(jsonlint())
        .pipe(jsonlint.failOnError());

    // YAML
    gulp.src("data/*.yaml")
        .pipe(yamllint());
});
