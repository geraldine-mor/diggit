$(document).ready(function () {

    // Replaced with popover for consistencey and easier styling
    // $("#comment-btn").click(function(){
    //     $("#comment-form").show();
    // });

    // $("#comment-close").click(function(){
    //     $("#comment-form").hide();
    // });

    // Clear the post form on cancel
    $("#post-form-cancel").click(function () {
        $("#post-form>form")[0].reset();
    });

    const editButtons = document.getElementsByClassName("post-edit-btn");
    if (editButtons.length > 0) {
        postEdit(editButtons);
    };

    const deleteButtons = document.getElementsByClassName("post-delete-btn");
    if (deleteButtons.length > 0) {
        postDelete(deleteButtons);
    };

    const commentEditButtons = document.getElementsByClassName("comment-edit-btn");
    if (commentEditButtons.length > 0) {
        commentEdit(commentEditButtons);
    };

    const commentDeleteButtons = document.getElementsByClassName("comment-delete-btn");
    if (commentDeleteButtons.length > 0) {
        commentDelete(commentDeleteButtons);
    };

    const commentLikeButtons = document.getElementsByClassName("like-btn");
    if (commentLikeButtons.length > 0) {
        commentLike(commentLikeButtons);
    };

});

function postEdit(editButtons) {
    const postTitle = document.getElementById("id_title");
    const postContent = document.getElementById("id_content");
    const postSave = document.getElementById("post-save");
    const postForm = document.getElementById("edit-create-post");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.getAttribute("data-post-slug");
            postTitle.value = e.target.getAttribute("data-title");
            postContent.value = e.target.getAttribute("data-content");
            postSave.innerText = "Update";
            postForm.setAttribute("action", `/${postSlug}/edit_post/`);
        });
    };
}

function postDelete(deleteButtons) {
    const postDelete = document.getElementById("confirm-post-delete");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.getAttribute("data-post-slug");
            postDelete.setAttribute("href", `/${postSlug}/delete_post/`);
        });
    };
}

function commentEdit(commentEditButtons) {
    const commentContent = document.getElementById("id_content");
    const commentSave = document.getElementById("comment-save");
    const commentForm = document.getElementById("edit-create-comment");

    for (let button of commentEditButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.getAttribute("data-post-slug");
            let commentId = e.target.getAttribute("data-comment-id")
            commentContent.value = e.target.getAttribute("data-comment");
            commentSave.innerText = "Update";
            commentForm.setAttribute("action", `/${postSlug}/edit_comment/${commentId}`);
        })
    };
}

function commentDelete(deleteButtons) {
    const commentDelete = document.getElementById("confirm-comment-delete");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.getAttribute("data-post-slug");
            let commentId = e.target.getAttribute("data-comment-id");
            commentDelete.setAttribute("href", `/${postSlug}/delete_comment/${commentId}`);
        });
    };
}

function commentLike(commentLikeButtons) {
    const commentLike = document.getElementById("comment-likes");

    for (let button of commentLikeButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.closest(".like-btn").getAttribute("data-post-slug");
            let commentId = e.target.closest(".like-btn").getAttribute("data-comment-id");
            commentLike.setAttribute("action", `/${postSlug}/like_comment/${commentId}`);
        });
    };
}