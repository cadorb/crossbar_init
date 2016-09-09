

// the URL of the WAMP Router (Crossbar.io)
//
var wsuri = "ws://192.168.245.133:9090/ws";

// the WAMP connection to the Router
//
var connection = new autobahn.Connection({
	url: wsuri,
	realm: "realm1"
});



function clickButton (){
	// PUBLISH an event on every clickButton()
	//
	connection.session.publish("com.example.clickButton", ['Button clicked']);
	console.log('PUBLISHED to topic "com.example.clickButton"');

	// CALL a remote procedure
	//
    connection.session.call('com.example.click_counter').then(
        function (res) {
    		console.log("Result:", res);
    	}
    );
}


 


// fired when connection is established and session attached
//
connection.onopen = function (session, details) {
	console.log('Connected');

	// PUBLISH an event on connection
	//
	session.publish("com.example.hello", ['Event Launcher Online']);
	console.log("PUBLISHED : Event Launcher Online");

};

// fired when connection was lost (or could not be established)
//
connection.onclose = function (reason, details) {
	console.log("Connection lost: " + reason);
}

// now actually open the connection
// 
connection.open();