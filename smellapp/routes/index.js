var express = require('express');
var router = express.Router();

var matchingMapNumToId = {
   1: {
       rfid: ""
   }
};

var matchingMapIdToNum = {
    "1d3j3d1": {
        id: 1
    }
};


var smellMap = {

  1: {

      smell_name: "banana",
      img: "/public/images/banana.png"
  },
    2: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    3: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },

    4: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    5: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    6: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    7: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    8: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    9: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    },
    10: {
        smell_name: "banana",
        img: "/public/images/banana.png"
    }
};



/* GET home page. */
router.get('/', function(req, res, next) {


  res.render('index', {p: smellMap});


});

router.post('/updateSmell/:id/:smell', function(req, res, next) {


    //smellMap


});



router.post('/rf/:rfid', function(req, res, next){

    var rfid = req.params.rfid;

    var ballId = matchingMapIdToNum[rfid];

    var smellJson = smellMap[ballId];

    res.json(smellJson);

});


module.exports = router;
