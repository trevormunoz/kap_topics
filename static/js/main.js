$(document).ready( function() {
    $('p.full-list').hide();
    $('a.showLess').hide();
});

$('.showMore').on("click", function(){
    var target_id = '#' + $(this).attr('data-target');
    $(this).hide();
    $(target_id).show();
    $(target_id).next().show();
});

$('.showLess').on("click", function(){
     $('p.full-list').hide();
    $('a.showLess').hide();
    $('a.showMore').show();
});