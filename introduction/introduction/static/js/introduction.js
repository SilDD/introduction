const container = document.getElementById('scrollContainer');

container.addEventListener('scroll', function() {
  if (container.scrollLeft + container.clientWidth >= container.scrollWidth) {
   
    loadMoreItems();
  }
});

function loadMoreItems() {
  for (let i = 0; i < 5; i++) {
    const newItem = document.createElement('div');
    newItem.className = 'scroll-item';
    newItem.textContent = `Item ${document.querySelectorAll('.scroll-item').length + 1}`;
    container.appendChild(newItem);
  }
}
