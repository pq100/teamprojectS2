var express = require('express');
var router = express.Router();

router.get('/notfound', function(req, res, next) {
  res.sendFile(__dirname + '/views/notfound.html')
});


router.get('/', function(req, res, next) {
  res.sendFile(__dirname + '/views/index.html')
});


router.get('/payment', function(req, res, next) {
  res.sendFile(__dirname + '/views/payment.html')
});


module.exports = router;

