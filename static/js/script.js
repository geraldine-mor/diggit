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

    const editButtons = document.getElementsByClassName("edit-btn");
    const postTitle = document.getElementById("id_title");
    const postContent = document.getElementById("id_content");
    const postSave = document.getElementById("post-save");
    const postForm = document.getElementById("edit-create-post");

    for (let button of editButtons) {
        button.addEventListener("click", (e) =>{
            let postSlug = e.target.getAttribute("data-post-slug");
            postTitle.value = e.target.getAttribute("data-title");
            postContent.value = e.target.getAttribute("data-content");
            postSave.innerText = "Update";
            postForm.setAttribute("action", `/${postSlug}/edit_post/`);
        });
    }
});