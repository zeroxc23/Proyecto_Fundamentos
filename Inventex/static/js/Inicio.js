const cards = document.querySelectorAll('.card');

cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.classList.add('show');
    });
    card.addEventListener('mouseleave', () => {
        card.classList.remove('show');
    });
});
