// Display a div then disapear
function notify(){
    var div = $("div");
    div.animate({height: '50px', opacity: '0.4'}, "slow");
    div.animate({width: '50px', opacity: '0.8'}, "slow");
    div.animate({height: '25px', opacity: '0.4'}, "slow");
    div.animate({width: '25px', opacity: '0.8'}, "slow");
}

// the URL of the WAMP Router (Crossbar.io)
//
var wsuri = "ws://192.168.245.133:9090/ws";

// the WAMP connection to the Router
//
var connection = new autobahn.Connection({
	url: wsuri,
	realm: "realm1"
});


// fired when connection is established and session attached
//
connection.onopen = function (session, details) {
	console.log('Connected');


// 1) subscribe to a topic
   function onevent(args) {
      console.log("Event:", args[0]);
      notify();
   }
   session.subscribe('com.example.clickButton', onevent);

	

	

};

// fired when connection was lost (or could not be established)
//
connection.onclose = function (reason, details) {
	console.log("Connection lost: " + reason);
}

// now actually open the connection
// 
connection.open();





  