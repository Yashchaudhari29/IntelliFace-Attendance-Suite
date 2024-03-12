const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
const video = document.getElementById('video-element');
const captureBtn = document.getElementById('capture-btn');

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
            const { height, width } = stream.getTracks()[0].getSettings();

            captureBtn.addEventListener('click', function () {
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');

                // Set the canvas dimensions to match the video dimensions
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;

                // Draw the current video frame onto the canvas
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                // Get the base64-encoded data URL of the canvas content
                const imageData = canvas.toDataURL('image/png');
                console.log(imageData)
                // Send the captured image data to the Django backend
                fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrftoken 
                    },
                    body: new URLSearchParams({ 'image_data': imageData })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error capturing image:', error);
                });
            });
        })
        .catch(error => {
            console.error('Error accessing webcam:', error);
        });
}
