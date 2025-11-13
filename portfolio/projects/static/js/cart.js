document.addEventListener('DOMContentLoaded', function () {
    console.log('cart.js loaded');
    document.querySelectorAll('.like-btn').forEach(btn => {
        btn.addEventListener('click', function (e) {
        e.preventDefault();
        console.log('like clicked', this.dataset.projectId);
        const projectId = this.dataset.projectId;
        fetch(`/projects/add-to-cart/${projectId}/`)
            .then(r => r.json())
            .then(data => {
            console.log('add-to-cart response', data);
            if (data.status === 'success') this.classList.add('liked');
            })
            .catch(err => console.error('fetch error', err));
        });
    });

    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const projectId = this.dataset.projectId;
            fetch(`/projects/remove-from-cart/${projectId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        // Remove the item from the DOM
                        this.closest('.cart-item').remove();
                    }
                })
                .catch(err => console.error('Error removing from cart:', err));
        });
    });
});