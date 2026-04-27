$(document).ready(function () {

    // Clear the post form on cancel
    $("#post-form-cancel").click(function () {
        $("#post-form>form")[0].reset();
        // Provided by Claude.ai to ensure form clears on cancel where there are errors.
        window.location.href = window.location.pathname;
    });

    // Check for form errors and open the relevant popover
    const formErrors = $('[data-has-errors="true"]');
    if (formErrors.length > 0) {
        formErrors[0].showPopover();
    };

    postEdit($(".post-edit-btn"));

    postDelete($(".post-delete-btn"));

    commentEdit($(".comment-edit-btn"));

    commentDelete($(".comment-delete-btn"));

    commentLike($(".like-btn"));

    commentReply($(".comment-reply-btn"));

    $("#comment-btn").click(() => {
        setCommentMode("create");
    });

    $("#create-post").click(() => {
        setPostMode("create");
        document.getElementById("post-form").showPopover();
    });

});

// Close any open comment popovers
const closePopovers = () => {
    document.getElementById("comment-form").hidePopover();
    document.getElementById("comment-delete").hidePopover();
}

// Open the comment popover
const openCommentForm = () => { document.getElementById("comment-form").showPopover(); }

//Close any open popovers on the read_post template
const closeOpenForms = () => {
    console.log("closeOpenForms called")
    document.getElementById("post-form").hidePopover();
    document.getElementById("post-delete").hidePopover();
}

// Update the new post fprm for edits
function postEdit(editButtons) {
    editButtons.click(function () {
        let postSlug = $(this).attr("data-post-slug");
        setPostMode("edit", {
            title: $(this).attr("data-title"),
            content: $(this).attr("data-content"),
            slug: `/${postSlug}/edit_post/`
        });
    });
}

function postDelete(deleteButtons) {
    deleteButtons.click(function () {
        closeOpenForms();
        let postSlug = $(this).attr("data-post-slug");
        $("#confirm-post-delete").attr("href", `/${postSlug}/delete_post/`);
        document.getElementById("post-delete").showPopover();
    });
}

function setPostMode(mode, data = {}) {
    console.log("setPostMode called", mode)
    closeOpenForms();

    // Reset defaults
    $("#id_title").val("");
    $("#id_content").val("");
    $("#post-save").text("Save");
    $("#edit-create-post").attr("action", "/create_post/");

    // Edit mode
    if (mode === "edit") {
        $("#id_title").val(data.title);
        $("#id_content").val(data.content);
        $("#post-save").text("Update");
        $("#edit-create-post").attr("action", data.slug);
        document.getElementById("post-form").showPopover();
        console.log("got here")
    };
}

function commentEdit(commentEditButtons) {
    commentEditButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");

        setCommentMode("edit", {
            content: $(this).attr("data-comment"),
            slug: `/${postSlug}/edit_comment/${commentId}`
        });
    });
};

function commentDelete(deleteButtons) {
    deleteButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");
        closePopovers();
        document.getElementById("comment-delete").showPopover();
        $("#confirm-comment-delete").attr("href", `/${postSlug}/delete_comment/${commentId}`);
    });
};

// Apply event listeners to the like buttons, close any open popovers and set the like url
function commentLike(commentLikeButtons) {
    commentLikeButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");
        closePopovers();
        $(this).parent().attr("action", `/${postSlug}/like_comment/${commentId}`);
    });
};

// Apply event listeners to the reply buttons and set reply mode
function commentReply(replyButtons) {
    replyButtons.click(function () {
        setCommentMode("reply", {
            parentId: $(this).attr("data-comment-id")
        });
    });
};

function setCommentMode(mode, data = {}) {

    closePopovers();

    // Default settings (create form)
    $("#parent-id").val("");
    $("#id_content").val("");
    $("#author-name-comment").show();
    $("#author-name-reply").hide();
    $("#comment-save").text("Comment");

    $("#edit-create-comment").attr("data-mode", mode)

    // For replies
    if (mode === "reply") {
        $("#parent-id").val(data.parentId);
        $("#comment-save").text("Reply");
        $("#author-name-comment").hide();
        $("#author-name-reply").show();
    }

    // For edits
    if (mode === "edit") {
        $("#id_content").val(data.content);
        $("#comment-save").text("Update");
        $("#edit-create-comment").attr("action", data.slug)
    }

    openCommentForm();
}