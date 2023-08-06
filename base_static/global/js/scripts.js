(function () {
    select_variation = document.getElementById('select-variations');
    variation_marketing_price = document.getElementById('variation-marketing-price');
    variation_marketing_off_price = document.getElementById('variation-marketing-off-price');

    if (!select_variation) {
        return;
    }

    if (!variation_marketing_price) {
        return;
    }

    select_variation.addEventListener('change', function () {
        price = this.options[this.selectedIndex].getAttribute('data-price');
        off_price = this.options[this.selectedIndex].getAttribute('data-off-price');

        variation_marketing_price.innerHTML = price;

        if (variation_marketing_off_price) {
            variation_marketing_off_price.innerHTML = off_price;
        }
    })
})();

