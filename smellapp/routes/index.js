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


var flag = 0;
var numOfMatchedBalls = 0;
var smells = {

    1: {
        smell_name: "banana",
        output_id: 1,
        img: "/public/images/banana.png",
        is_set: -1

    },
    2: {
        smell_name: "strawberry",
        output_id: 2,

        img: "/public/images/strawberry.png",
        is_set: -1
    },
    3: {
        smell_name: "apple",
        output_id: 3,

        img: "/public/images/apple.png",
        is_set: -1
    },

    4: {
        smell_name: "bazookajoe",
        output_id: 4,

        img: "/public/images/bazookajoe.jpg",
        is_set: -1
    },
    5: {
        smell_name: "chocoalte",
        output_id: 5,
        img: "/public/images/chocoalte.jpeg",
        is_set: -1
    },
    6: {
        smell_name: "grapes",
        output_id: 6,
        img: "/public/images/grapes.png",
        is_set: -1
    },
    7: {
        smell_name: "strawberry",
        output_id: 7,
        img: "/public/images/pineapple.jpeg",
        is_set: -1
    },
    8: {
        smell_name: "passionfruit",
        output_id: 8,
        img: "/public/images/passionfruit.jpg",
        is_set: -1
    },
    9: {
        smell_name: "cola",
        output_id: 9,
        img: "/public/images/cola.png",
        is_set: -1
    },
    10: {
        smell_name: "watermelon",
        output_id: 10,
        img: "/public/images/watermelon.jpeg",
        is_set: -1
    }
};

/* GET home page. */
router.get('/admin', function (req, res, next) {

    res.render('admin', {p: smells, ball_map: ballMap});


});

/* GET home page. */
router.get('/', function (req, res, next) {


    console.log(smells);
    console.log(ballMap);

    res.render('index', {p: smells, ball_map: ballMap});


});

router.post('/updateSmell/:id/:smell', function (req, res, next) {


    //console.log(req.params);
    var ballid = req.params['id'];
    var smellid = req.params['smell'];
    console.log(ballid, smellid);

    ballMap[ballid]['smell_id'] = smellid;
    smells[smellid]['is_set'] = 1;
    numOfMatchedBalls++;
    console.log(numOfMatchedBalls);
    res.sendStatus(200);

    //smellMap


});

router.post('/setflag', function (req, res, next) {
    flag = 1;
    res.sendStatus(200);

});

var getRandomInt = function(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
};

router.get('/startcheck', function (req, res, next) {


    if (flag == 1) {
        flag = 0;

        var unasignedBalls = _.filter(ballMap, function (ball) {
            return ball['smell_id'] == -1;
        });
        console.log(unasignedBalls.length);

        var assignedBalls = _.filter(ballMap, function (ball) {
            return ball['smell_id'] != -1;
        });

        var assignedsmells = _.map(assignedBalls, 'smell_id');

        // assignedsmells = _.map(assignedBalls, parseInt);
        assignedsmells = _.sortBy(assignedsmells, function (o) {
            return o;
        });

        for(var j = 0; j < assignedsmells.length; j++) {
            assignedsmells[j] = parseInt( assignedsmells[j]);
        }

        console.log(assignedsmells);

        var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

        var leftNumbers = [];

        for(var i = 0; i < numbers.length; i++) {
            // console.log(assignedsmells.indexOf(1));
            if (assignedsmells.indexOf(numbers[i]) < 0) {
                leftNumbers.push(numbers[i]);
            }
        }

        leftNumbers = _.shuffle(leftNumbers);


        _.forEach(unasignedBalls, function(ball, index){

            ball['smell_id'] = leftNumbers[index];

            smells[leftNumbers[index]]['is_set'] = 1;
        });



        console.log(ballMap);


        res.json({status: 0, start: 1});
    }
    else
        res.json({status: 0, start: 0});

});
router.get('/rf', function (req, res, next) {


    // console.log(req.query.rfid);

    var rfid = req.query.rfid;

    var realRfId = matchIdAprox(rfid);
    //console.log('realRfId = ', realRfId);

    if (realRfId == -1)
        return res.json({status: -1});


    var ballId = matchingMapIdToNum[realRfId]['ball_id'];
    //  console.log('ballId = ', ballId);

    var smellid = ballMap[ballId]['smell_id'];

    console.log('smellid = ', smellid);

    //reset smell match for ball
    // console.log(smells[smellid]);

    if (smells[smellid] == undefined)
        return res.json({status: -2});


    res.json({status: 0, smell_data: smells[smellid]});
    smells[smellid]['is_set'] = -1;
    ballMap[ballId]['smell_id'] = -1;
    numOfMatchedBalls = 0;
    //console.log('done');


});


var matchIdAprox = function (rfid) {

    var key = null;

    _.forIn(matchingMapIdToNum, function (v, k) {

        //console.log("key = ", k);

        var matchCounter = 0;
        for (var i = 0; i < rfid.length; i++) {

            if (rfid.charAt(i) === k.charAt(i))
                matchCounter++;

            //console.log(matchCounter);
            //matched
            if (matchCounter >= 13) {
                //console.log(matchCounter);
                key = k;
                break;
            }

        }
        if (key)
            return false;


    });
    return key ? key : -1;
};


// var resetBalls = function() {
//   numOfMatchedBalls = 0;
//   _.forEach(ballMap, function(b){
//
//       b['smell_id'] = -1;
//
//   });
// };


module.exports = router;
