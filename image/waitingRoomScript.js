document.addEventListener('DOMContentLoaded', function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const roomCode = urlParams.get('roomCode');

    // Display the room code
    const roomCodeSpan = document.getElementById('room-code');
    roomCodeSpan.textContent = roomCode;

    // Here you can add logic to check if the room is ready or if enough players have joined
    // For example, you might use WebSocket to communicate with a server to check for room status

    // If the room is ready, you can redirect the player to the game page
    // Example:
    // if (roomCode) {
    //     setTimeout(function() {
    //         window.location.href = `GamePage.html?roomCode=${roomCode}`;
    //     }, 5000); // Redirect after 5 seconds (adjust this value as needed)
    // }
});
