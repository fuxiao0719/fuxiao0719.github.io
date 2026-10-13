$(document).ready(function() {
    $('a.abstract, button.abstract').each(function(index) {
        const panel = $(this).parent().parent().find('.abstract.hidden');
        if (!panel.attr('id')) panel.attr('id', 'abstract-' + index);
        $(this).attr('aria-controls', panel.attr('id'));
    }).click(function() {
        const panel = $(this).parent().parent().find('.abstract.hidden');
        panel.toggleClass('open');
        $(this).attr('aria-expanded', panel.hasClass('open'));
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
    });
    $('.navbar-nav').find('a').removeClass('waves-effect waves-light');
});
