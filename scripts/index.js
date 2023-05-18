const board = document.querySelector('chess-board');

board.pieceTheme = (piece) => {
    const pieces = {
        wK: '../assets/themes/classic/wK.svg',
        wQ: '../assets/themes/classic/wQ.svg',
        wR: '../assets/themes/classic/wR.svg',
        wB: '../assets/themes/classic/wB.svg',
        wN: '../assets/themes/classic/wN.svg',
        wP: '../assets/themes/classic/wP.svg',
        bK: '../assets/themes/classic/bK.svg',
        bQ: '../assets/themes/classic/bQ.svg',
        bR: '../assets/themes/classic/bR.svg',
        bB: '../assets/themes/classic/bB.svg',
        bN: '../assets/themes/classic/bN.svg',
        bP: '../assets/themes/classic/bP.svg',
    }

    return pieces[piece]
}

board.addEventListener('drop', (e) => {
    const {source, target, piece, newPosition, oldPosition, orientation} = e.detail;
    console.log('Source: ' + source)
    console.log('Target: ' + target)
    console.log('Piece: ' + piece)
    console.log('Orientation: ' + orientation)
    console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
});

const play_button = document.getElementById('play_button')

play_button.addEventListener('click', async () => {
    const response = await fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const data = await response.json()

    const fen = data['fen']
    board.setAttribute('position', fen)
    console.log(fen)
})
