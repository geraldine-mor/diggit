/* jshint esversion: 11, jquery: true */

/**
 * Handles user interactions for posts, comments and replies
 * Controls popover forms for create/edit/delete flows
 * Uses mode-based state management for form reuse
 */

$(document).ready(function () {

    // Clear the post form on cancel
    $("#post-form-cancel").click(function () {
        $("#post-form>form")[0].reset();
        // Logic suggested by Claude.ai: ensures the URL resets
        // on cancel so error-state popovers don't re-open on reload.
        window.location.href = window.location.pathname;
    });

    // Check for form errors and open the relevant popover
    const formErrors = $('[data-has-errors="true"]');
    if (formErrors.length > 0) {
        formErrors[0].showPopover();
    }

    
    postEdit($(".post-edit-btn"));

    postDelete($(".post-delete-btn"));

    commentEdit($(".comment-edit-btn"));

    commentDelete($(".comment-delete-btn"));

    commentLike($(".like-btn"));

    commentReply($(".comment-reply-btn"));

    replyEdit($(".reply-edit-btn"));

    $("#comment-btn").click(() => {
        setCommentMode("create");
    });

    $("#create-post").click(() => {
        setPostMode("create");
        document.getElementById("post-form").showPopover();
    });

});
// Close any open popovers to ensure only one comment-related popover is visible at a time
const closePopovers = () => {
    ["comment-form", "comment-delete"].forEach(id => {
        const el = document.getElementById(id);
        if (el.matches(":popover-open")) el.hidePopover()
    });
};

const openCommentForm = () => { document.getElementById("comment-form").showPopover(); };

// Close any open popovers to ensure only one post-related popover is visible at a time
const closeOpenForms = () => {
    ["post-form", "post-delete"].forEach(id => {
        const el = document.getElementById(id);
        if (el.matches(":popover-open")) el.hidePopover()
    });
};

/**
 * Applies click handlers to post edit buttons.
 * Reads post data from data attributes and delegates to setPostMode("edit").
 * @param {jQuery} editButtons - DOM collection of post edit buttons
 */
function postEdit(editButtons) {
    editButtons.click(function () {
        let postSlug = $(this).attr("data-post-slug");
        let categories = $(this).attr("data-categories").split(",").map(Number);
        setPostMode("edit", {
            title: $(this).attr("data-title"),
            content: $(this).attr("data-content"),
            slug: `/${postSlug}/edit_post/`,
            categories: categories
        });
    });
}

// Sets the delete URL and opens the confirmation popover
function postDelete(deleteButtons) {
    deleteButtons.click(function () {
        closeOpenForms();
        let postSlug = $(this).attr("data-post-slug");
        $("#confirm-post-delete").attr("href", `/${postSlug}/delete_post/`);
        document.getElementById("post-delete").showPopover();
    });
}

/**
 * Configures the post form settings based on the current mode
 * 
 * Modes: 
 * - "create": Resets the form for creating a new post (default)
 * - "edit": Populates the form with existing post data for editing
 * 
 * @param {"create" | "edit"} mode - determines how the form should behave
 * @param {Object} [data={}] - data used to populate the form in edit mode
 * @param {string} [data.title] - the post title to populate the title field of the form
 * @param {string} [data.content] - the post content to populate the content field of the form
 * @param {string} [data.slug] - the form action URL for submission
 * @param {number[]} [data.categories] - array of category IDs to pre-select the checkboxes 
 */
function setPostMode(mode, data = {}) {
    closeOpenForms();

    // Reset defaults
    $("#id_title").val("");
    $("#id_content").val("");
    $("#post-save").text("Save");
    $("#post-form-title").text("Create post");

    // Edit mode
    if (mode === "edit") {
        $("#post-form-title").text("Edit post");
        $("#id_title").val(data.title);
        $("#id_content").val(data.content);
        // Pre-check categories - code provided by Claude.ai
        $("#id_categories input[type='checkbox']").each(function () {
            $(this).prop("checked", data.categories.includes(parseInt($(this).val())));
        });
        $("#post-save").text("Update");
        $("#edit-create-post").attr("action", data.slug);
        document.getElementById("post-form").showPopover();
    }
}

/**
 * Applies click handlers to comment edit buttons.
 * Reads post data from data attributes and delegates to setCommentMode("edit").
 * @param {jQuery} commentEditButtons - DOM collection of comment edit buttons
 */
function commentEdit(commentEditButtons) {
    commentEditButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");

        setCommentMode("edit", {
            content: $(this).attr("data-comment"),
            slug: `/${postSlug}/edit_comment/${commentId}`
        });
    });
}

// Sets the delete URL and opens the confirmation popover
function commentDelete(deleteButtons) {
    deleteButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");
        const type = $(this).attr("data-type");
        closePopovers();
        document.getElementById("comment-delete").showPopover();
        $("#comment-delete h2").text(`Are you sure you want to delete this ${type}?`);
        $("#confirm-comment-delete").attr("href", `/${postSlug}/delete_comment/${commentId}`);
    });
}

// Reads comment data from data attributes and builds the form URL for comment likes
function commentLike(commentLikeButtons) {
    commentLikeButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");
        closePopovers();
        $(this).parent().attr("action", `/${postSlug}/like_comment/${commentId}`);
    });
}

/**
 * Applies click handlers to comment reply buttons.
 * Reads post data from data attributes and delegates to setCommentMode("reply").
 * @param {jQuery} replyButtons - DOM collection of comment reply buttons
 */
function commentReply(replyButtons) {
    replyButtons.click(function () {
        setCommentMode("reply", {
            parentId: $(this).attr("data-comment-id"),
            author: $(this).attr("data-comment-author")
        });
    });
}

/**
 * Applies click handlers to reply edit buttons.
 * Reads post data from data attributes and delegates to setCommentMode("reply-edit").
 * @param {jQuery} replyEditButtons - DOM collection of reply edit buttons
 */
function replyEdit(replyEditButtons) {
    replyEditButtons.click(function () {
        const postSlug = $(this).attr("data-post-slug");
        const commentId = $(this).attr("data-comment-id");
        setCommentMode("reply-edit", {
            content: $(this).attr("data-comment"),
            slug: `/${postSlug}/edit_comment/${commentId}`,
            author: $(this).attr("data-comment-author")
        });
    });
}

/**
 * Configures the comment form settings based on the current mode
 * 
 * Modes: 
 * - "create": Resets the form for creating a new top-level comment
 * - "reply": Updates the form with reply instructions and applies the parentID to the hidden form field
 * - "edit": Populates the form with existing comment data for editing
 * - "reply-edit": Populates the form with existing reply data for editing, updates the form instructions to indicate reply rather than comment 
 * 
 * @param {"create" | "reply" | "edit" | "reply-edit" } mode - determines how the form should behave
 * @param {Object} [data={}] - data used to populate the form in edit mode
 * @param {number} [data.parentId] - the comment's parent ID used to populate the hidden parent_id field
 * @param {string} [data.content] - the comment content to populate the content field of the form
 * @param {string} [data.slug] - the form action URL for submission
 * @param {string} [data.author] - the author of the parent comment used to update the reply form text 
 */
function setCommentMode(mode, data = {}) {

    closePopovers();

    // Default settings (create form)
    $("#parent-id").val("");
    $("#id_content").val("");
    $("#comment-title").show();
    $("#reply-title").hide();
    $("#author-name-comment").show();
    $("#author-name-reply").hide();
    $("#comment-save").text("Comment");

    $("#edit-create-comment").attr("data-mode", mode);

    // For replies
    if (mode === "reply") {
        $("#parent-id").val(data.parentId);
        $("#comment-save").text("Reply");
        $("#comment-title").hide();
        $("#reply-title").text("You are replying to " + data.author).show();
        $("#author-name-comment").hide();
        $("#author-name-reply").show();
    }

    // For edits
    if (mode === "edit") {
        $("#id_content").val(data.content);
        updateCounter();
        $("#comment-save").text("Update");
        $("#edit-create-comment").attr("action", data.slug);
    }

    // For reply edits
    if (mode == "reply-edit") {
        $("#id_content").val(data.content);
        updateCounter();
        $("#comment-title").hide();
        $("#reply-title").text("You are replying to " + data.author).show();
        $("#author-name-comment").hide();
        $("#author-name-reply").show();
        $("#comment-save").text("Update");
        $("#edit-create-comment").attr("action", data.slug);
    }

    openCommentForm();
}

// Show character limit countdown on comments
// Code derived from: https://stackoverflow.com/a/1250788/32259671
// Separated to allow accurate character count on edit forms
function updateCounter() {
    let left = 1000 - $('#edit-create-comment #id_content').val().length;
        if (left < 0) {
            left = 0;
        }
        $('#counter').text(`${left}/1000`);
}

$('#edit-create-comment #id_content').keyup(function () {
    updateCounter();
});