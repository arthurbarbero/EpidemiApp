function onFocusLoose(element) {
    let hasBorder = element.style.getPropertyValue('border')
    if (element.value && hasBorder) {
        element.style.removeProperty('border');
    }
};
