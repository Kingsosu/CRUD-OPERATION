
setTimeout(function() {
    try {
        var message_timeout = document.getElementById('message-time');
        // Attempt to modify the style and hide the element
        message_timeout.style.display = 'none';
    } catch (error) {
        // If an error occurs, handle it here
        console.error('An error occurred:', error);
        // You can choose to log the error, display a message, or handle it in any way you prefer
    }
}, 3000);
