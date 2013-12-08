$(document).ready( function() {
    $('p.full-list').hide();
    $('a.showLess').hide();
});

$('.showMore').on("click", function(event){
    event.preventDefault();
    var target_id = '#' + $(this).attr('data-target');
    $(this).hide();
    $(target_id).show();
    $(target_id).next().show();
});

$('.showLess').on("click", function(event){
    event.preventDefault();
     $('p.full-list').hide();
    $('a.showLess').hide();
    $('a.showMore').show();
});

$('.form-control').on("focus", function(){
    var topic_id = $(this).prev().attr('for');
    $(this).closest('form').find('#topic_id').val(topic_id);
});
