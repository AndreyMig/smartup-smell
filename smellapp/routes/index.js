var express = require('express');
var router = express.Router();
var _ = require('lodash');

var matchingMapNumToId = {
    1: {
        rfid: "218534ad5b8df885fc9be1"
    }
};

var matchingMapIdToNum = {

    "218534ad5b8df885fc9be1": {
        ball_id: 1
    },
    "218534ad7c858a85d626e1": {
        ball_id: 2
    },
    "318134b135855a8935e3fc": {
        ball_id: 3
    },
    "218534a77985248dfc9ae1": {
        ball_id: 4
    },
    "318734adb55d24b5f936f1": {
        ball_id: 5
    },
    "31b134adf94566a5fc9af8": {
        ball_id: 6
    },
    "318734adb64d25894985f8": {
        ball_id: 7
    },
    "318334b1f5ad7589fa9af1": {
        ball_id: 8
    },
    "218534af79851cb1f936e1": {
        ball_id: 9
    },
    "e18534b1a9b57adb4985f8": {
        ball_id: 10
    }
};

var ballMap = {
    1: {
        rf_id: "",
        smell_id: -1

    },
    2: {
        rf_id: "",
        smell_id: -1

    },
    3: {
        rf_id: "",
        smell_id: -1

    },

    4: {
        rf_id: "",
        smell_id: -1

    },
    5: {
        rf_id: "",
        smell_id: -1

    },
    6: {
        rf_id: "",
        smell_id: -1

    },
    7: {
        rf_id: "",
        smell_id: -1
    },

    8: {
        rf_id: "",
        smell_id: -1

    },
    9: {
        rf_id: "",
        smell_id: -1

    },
    10: {
        rf_id: "",
        smell_id: -1
    }
};


var smells = {

    1: {

        smell_name: "banana1",
        img: "/public/images/banana.png"
    },
    2: {
        smell_name: "banana2",
        img: "/public/images/banana.png"
    },
    3: {
        smell_name: "banana3",
        img: "/public/images/banana.png"
    },

    4: {
        smell_name: "banana4",
        img: "/public/images/banana.png"
    },
    5: {
        smell_name: "banana5",
        img: "/public/images/banana.png"
    },
    6: {
        smell_name: "banana6",
        img: "/public/images/banana.png"
    },
    7: {
        smell_name: "banana7",
        img: "/public/images/banana.png"
    },
    8: {
        smell_name: "banana8",
        img: "/public/images/banana.png"
    },
    9: {
        smell_name: "banana9",
        img: "/public/images/banana.png"
    },
    10: {
        smell_name: "banana10",
        img: "/public/images/banana.png"
    }
};


/* GET home page. */
router.get('/', function (req, res, next) {


    res.render('index', {p: smells});


});

router.post('/updateSmell/:id/:smell', function (req, res, next) {


    //console.log(req.params);
    var ballid = req.params['id'];
    var smellid = req.params['smell'];
    console.log(ballid, smellid);

    ballMap[ballid]['smell_id'] = smellid;


    res.sendStatus(200);

    //smellMap


});


router.get('/rf', function (req, res, next) {


    console.log(req.query.rfid);

    var rfid = req.query.rfid;

    var realRfId = matchIdAprox(rfid);
    //console.log('realRfId = ', realRfId);

    if (realRfId == -1)
        return res.sendStatus(200);


    var ballId = matchingMapIdToNum[realRfId]['ball_id'];
    console.log('ballId = ', ballId);

    var smellid = ballMap[ballId]['smell_id'];

    console.log('smellid = ', smellid);

    //reset smell match for ball
    console.log(smells[smellid]);

    res.json(smells[smellid]);
//    ballMap[ballId]['smell_id'] = -1;


    console.log('done');


});


var matchIdAprox = function (rfid) {

    var key = null;

    _.forIn(matchingMapIdToNum, function (v, k) {

        console.log("key = ", k);

        var matchCounter = 0;
        for (var i = 0; i < rfid.length; i++) {

            if (rfid.charAt(i) === k.charAt(i))
                matchCounter++;

            //console.log(matchCounter);
            //matched
            if (matchCounter >= 16) {
                console.log(matchCounter);
                key = k;
                break;
            }

        }
        if (key)
            return false;


    });
    return key ? key : -1;
};

module.exports = router;
