document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/sandwiches')
        .then(response => response.json())
        .then(data => {
            const sandwichList = document.getElementById('sandwich-list');
            data.forEach(sandwich => {
                const div = document.createElement('div');
                div.className = 'sandwich';
                div.innerHTML = `<h2>${sandwich.name}</h2>`;
                sandwichList.appendChild(div);
            });
        })
        .catch(error => console.error('Error:', error));
});
