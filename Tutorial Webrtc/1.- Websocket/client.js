//open a websocket from js
var ws = new WebSocket("ws://localhost:8895")

ws.onopen = function () {
    //WebSocket is connected, send datas to server
    ws.send("Message fro user");
    console.log("Message send to server")
}

ws.onmessage = function (evt) {
    //handle messages from server
    var received_msg = evt.data;
    alert("Message from server = " + received_msg);
};

ws.onclose = function () {
    //websocket is closed
    console.log("Websocket Connection is closed...");
}