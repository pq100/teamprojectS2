let createError = require('http-errors');
let express = require('express');
let path = require('path');

var session = require('express-session')
let port = 3000

let indexRouter = require('./public/index');

let app = express();


app.use(session({
  secret: 'secret',
  resave: false,
  saveUninitialized: false
}));

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

app.use(function(req, res, next) {
  next(createError(404));
});


app.listen(port, () => {
  console.log(`frontend server on port ${port}`)
})

module.exports = app;

