const container = document.querySelector('.container')
 
const colors = ['#23f6c8', '#81a826', '#d73571', '#ff3300', '#faaf45']
 
for (let i = 0; i < 500; i++) {
    const square = document.createElement('div')
 
    square.classList.add('square')
    container.appendChild(square)
 
    square.addEventListener('mouseover', () => {
 
        const color = colors[Math.floor(Math.random() * colors.length)]
        square.style.backgroundColor = color
        square.style.boxShadow = `0 0 2px ${color}, 0 0 10px ${color}` //template string
    })
 
 
    square.addEventListener('mouseout', () => {
        square.style.backgroundColor = '#1d1d1d'
 
        square.style.boxShadow = '0 0 2px #000, 0 0 10px #000'
    })
 
}