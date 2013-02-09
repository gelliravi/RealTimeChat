var http = require('http'),
    rest = require('./restler');
var server = http.createServer().listen(4000);

var io = require('socket.io').listen(server);
var cookie_reader = require('cookie');
var querystring = require('querystring');
 
var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient();
 
sub.subscribe('chat');
 
io.configure(function(){
    io.set('authorization', function(data, accept){
        if(data.headers.cookie){
            
            data.cookie = cookie_reader.parse(data.headers.cookie);
            return accept(null, true);
        }
        console.log(data)
        return accept('error', false);
    });
    io.set('log level', 1);
});
 
io.sockets.on('connection', function (socket) {
    
    sub.on('message', function(channel, message){
        socket.send(message);
    });
    
    sub.on('is_type', function(channel, message){
        socket.send(message);
    });
    
    socket.on('is_type', function(message){
        var type = querystring.stringify({
            username: message,
            action: 'is_type',
            sessionid: socket.handshake.cookie['sessionid'],
        });
        rest.post('http://localhost:8000/node_api', {data: type}).on('complete', function(data, response) {
           console.log(response)
        });
    });
    
    socket.on('send_message', function (message) {
        values = querystring.stringify({
            comment: message,
            sessionid: socket.handshake.cookie['sessionid'],
        });
        
        rest.post('http://localhost:8000/node_api', {data: values}).on('complete', function(data, response) {
            if (response.statusCode == 200) {
             
            }
        });
       
    });
});