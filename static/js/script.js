$(document).ready(function(){
    
    $("#comment-btn").click(function(){
        $("#comment-form").show();
    });

    $("#comment-close").click(function(){
        $("#comment-form").hide();
    });

    $("#post-form-cancel").click(function(){
        $("#post-form>form")[0].reset();
    });
});