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

    const commentReplyButtons = document.getElementsByClassName("comment-reply-btn");
    if (commentReplyButtons.length > 0) {
        commentReply(commentReplyButtons);
    }

    const commentButton = document.getElementById("comment-btn");
    if (commentButton) {
        comment(commentButton);
    }

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

function comment(button) {
    const commentPopover = document.getElementById("comment-form");
    const deletePopover = document.getElementById("comment-delete");

    button.addEventListener("click", () => {
        deletePopover.hidePopover();
        commentPopover.hidePopover();
        setCommentMode("create");
        commentPopover.showPopover();
    });
}

function commentEdit(commentEditButtons) {

    for (let button of commentEditButtons) {
        button.addEventListener("click", (e) => {
            const postSlug = e.currentTarget.getAttribute("data-post-slug");
            const commentId = e.currentTarget.getAttribute("data-comment-id");
            const content = e.currentTarget.getAttribute("data-comment");
            const commentPopover = document.getElementById("comment-form");
            const deletePopover = document.getElementById("comment-delete");

            deletePopover.hidePopover();
            commentPopover.hidePopover();

            setCommentMode("edit", {
                commentId: commentId,
                content: content,
                slug: `/${postSlug}/edit_comment/${commentId}`
            });
            commentPopover.showPopover();
        })
    };
}

function commentDelete(deleteButtons) {
    const commentDelete = document.getElementById("confirm-comment-delete");
    const commentPopover = document.getElementById("comment-form");
    const deletePopover = document.getElementById("comment-delete");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.getAttribute("data-post-slug");
            let commentId = e.target.getAttribute("data-comment-id");
            commentPopover.hidePopover();
            deletePopover.showPopover();
            commentDelete.setAttribute("href", `/${postSlug}/delete_comment/${commentId}`);
        });
    };
}

function commentLike(commentLikeButtons) {
    const commentPopover = document.getElementById("comment-form");
    const deletePopover = document.getElementById("comment-delete");

    for (let button of commentLikeButtons) {
        button.addEventListener("click", (e) => {
            let postSlug = e.target.closest(".like-btn").getAttribute("data-post-slug");
            let commentId = e.target.closest(".like-btn").getAttribute("data-comment-id");
            commentPopover.hidePopover();
            deletePopover.hidePopover();
            e.target.closest(".comment-likes").setAttribute("action", `/${postSlug}/like_comment/${commentId}`);
        });
    };
}

function commentReply(replyButtons) {
    const commentPopover = document.getElementById("comment-form");
    const deletePopover = document.getElementById("comment-delete");

    for (let button of replyButtons) {
        button.addEventListener("click", (e) => {
            const parentId = e.currentTarget.getAttribute("data-comment-id");

            deletePopover.hidePopover();
            commentPopover.hidePopover();

            setCommentMode("reply", {
                parentId: parentId
            });
            commentPopover.showPopover();
        });
    };
}

function setCommentMode(mode, data = {}) {
    const commentForm = document.getElementById("edit-create-comment");
    const parentField = document.getElementById("parent-id");
    const content = document.getElementById("id_content");
    const saveBtn = document.getElementById("comment-save");
    const commentText = document.getElementById("author-name-comment");
    const replyText = document.getElementById("author-name-reply");

    // Default settings (create form)
    parentField.value = "";
    content.value = "";
    commentText.classList.remove("hidden");
    replyText.classList.add("hidden");
    saveBtn.innerText = "Comment";

    commentForm.dataset.mode = mode;

    // For replies
    if (mode === "reply") {
        parentField.value = data.parentId;
        saveBtn.innerText = "Reply";
        commentText.classList.add("hidden");
        replyText.classList.remove("hidden");
    }

    // For edits
    if (mode === "edit") {
        content.value = data.content;
        saveBtn.innerText = "Update";
        commentForm.setAttribute("action", data.slug)
    }
}