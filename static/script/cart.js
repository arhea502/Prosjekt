// Example: Update cart quantities without page reload
document.querySelectorAll('.cart-qty').forEach(input => {
    input.addEventListener('change', function() {
        const productId = this.dataset.id;
        const qty = this.value;
        fetch(`/update_cart/${productId}?qty=${qty}`)
            .then(res => res.json())
            .then(data => {
                document.querySelector('#cart-total').innerText = data.total;
            });
    });
});
