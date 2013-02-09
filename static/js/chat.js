window.onload = function(){
    
    var socket = new io.Socket();
    socket.connect();
    socket.on('connect', function() {
        socket.subscribe('my channel');
    });
    
}

