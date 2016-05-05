/**
 * Created by AndreyMig on 09/01/2016.
 */

var mysql     =    require('mysql');


var pool      =    mysql.createPool({
    connectionLimit : 100, //important
    host     : 'localhost',
    //user     : 'telegram',
    //password : 'T3l3gr4m',
    user: 'smell_user',
    password: 'sm3ll',
    database : 'smell',
    debug    :  false
});

exports.queryDB = function(query, cb){


    pool.getConnection(function(err,connection){
        if (err) {
            console.log('error: ' + err);
            connection.release();
            //res.json({"code" : 100, "status" : "Error in connection database"});
            return;
        }

        console.log('mysql connected as id ' + connection.threadId);

        connection.query(query,function(err,rows){
            connection.release();
            if(!err) {
                console.log(rows);
                cb(rows);

            }
            else
                console.log("Error: "+err);

        });

        connection.on('error', function(err) {
            console.log('Connection error = ' + err);
            return;
        });
    });
};


function handle_database() {


}