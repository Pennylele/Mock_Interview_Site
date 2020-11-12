$(document).ready(function () {
    var pathArray = window.location.pathname.split('/');
    video_id = pathArray[2]
    console.log(video_id)
    const domain = 'meet.jit.si';
    const options = {
        roomName: video_id,
        width: 500,
        height: 500,
        parentNode: document.getElementById("meet")
    };
    const api = new JitsiMeetExternalAPI(domain, options);
});