$(document).ready( function() {
    $('p.full-list').hide();
    $('a.showLess').hide();
    $('.glyphicon-ok-circle').css({'color': 'green', 'font-size': '1.66em'});
    if ( $.cookie("intro") === "yes"){
        // Load page as normal
    }
    else {
        introJs().setOptions({
        'showButtons': true,
        'showBullets': false,
        'keyboardNavigation': true,
        'exitOnEsc': true,
        'exitOnOverlayClick': true,
        'showStepNumbers': false
        }).oncomplete(function() {
            alert("This is the end of the introduction. Good luck!");
        }).onexit(function(){
            $.cookie("intro", "yes", { expires : 31 });
        }).start();
    }
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

$('.btn-danger').on("click", function(event){
    event.preventDefault();
    var rowId = $(this).attr('data-target');
    var split = rowId.split('t');
    var topic_id = split[1];
    var postToken = $.cookie("token");
    var sweepPromise = $.ajax({
        type: "POST",
        data: {token: postToken},
        url: "/remove/topic/"+topic_id
    });
    sweepPromise.done(function(){
        var target = "#"+rowId;
        $(target).next('hr').remove();
        $(target).remove();
    });
});
