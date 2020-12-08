// Jit.si
$(document).ready(function () {
    var pathArray = window.location.pathname.split('/');
    video_id = pathArray[2]
    const domain = 'meet.jit.si';
    const options = {
        roomName: video_id,
        width: 500,
        height: 500,
        parentNode: document.getElementById("meet")
    };
    const api = new JitsiMeetExternalAPI(domain, options);
});

// Socket.io
const uuid = window.location.pathname.split('/')[1];

const chatSocket = new WebSocket(
	'ws://'
	+ window.location.host
	+ ":8001/"
	+ '/ws/mock_site/'
	+ uuid
	+ '/'
);


chatSocket.onmessage = function(e) {
	const data = JSON.parse(e.data);
	document.querySelector('#script_text_area').value = (data.message);
};

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
};


document.querySelector('#script_text_area').onkeyup = function(e) {

		const messageInputDom = document.querySelector('#script_text_area');
		const message = messageInputDom.value;
		chatSocket.send(JSON.stringify({
			'message': message
		}));
};