// Toggle popup menu visibility
function togglePopupMenu() {
    const popupMenu = document.getElementById('popup-menu');
    popupMenu.style.display = popupMenu.style.display === 'block' ? 'none' : 'block';
}

// Close the popup if clicked outside
window.addEventListener('click', function (event) {
    const popupMenu = document.getElementById('popup-menu');
    const button = document.getElementById('floating-button');
    if (!popupMenu.contains(event.target) && !button.contains(event.target)) {
        popupMenu.style.display = 'none';
    }
});