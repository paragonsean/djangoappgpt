function toggleTranscript(id) {
    const element = document.getElementById(id);
    element.classList.toggle('hidden');
}

function manipulateDiv(id) {
    const element = document.getElementById(id);
    element.style.color = 'green'
    console.log('touched u')

}