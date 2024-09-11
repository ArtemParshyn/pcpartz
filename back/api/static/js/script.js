document.addEventListener('DOMContentLoaded', function () {
    // Привязываем события к кнопкам добавления в корзину на странице каталога
    if (document.querySelectorAll('.add-to-cart').length > 0) {
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', addToCart);
        });
    }

    // Если мы находимся на странице корзины, обновляем общую сумму
    if (document.querySelector('.cart-total')) {
        updateCartTotal();
    }
});

function addToCart(event) {
    const button = event.target;
    const productName = button.getAttribute('data-product');
    const productPrice = parseFloat(button.getAttribute('data-price'));

    const cart = getCart();
    cart.push({ name: productName, price: productPrice });
    saveCart(cart);

    // Обновляем сумму корзины только если находимся на странице корзины
    if (document.querySelector('.cart-total')) {
        updateCartTotal();
    }
}

function updateCartTotal() {
    const cart = getCart();
    const total = cart.reduce((sum, product) => sum + product.price, 0);

    const cartTotalElement = document.querySelector('.cart-total');

    if (cartTotalElement) {
        cartTotalElement.textContent = `Total: $${total.toFixed(2)}`;
    }
}

function getCart() {
    const cart = localStorage.getItem('cart');
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}
