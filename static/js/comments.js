const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}/` endpoint.
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    if (commentText) commentText.value = commentContent;
    if (submitButton) submitButton.innerText = "Update";
    if (commentForm) commentForm.setAttribute("action", `edit_comment/${commentId}/`);
  });
}

// Wire up delete buttons to open modal and set delete URL
for (let dbtn of deleteButtons) {
  dbtn.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let base = window.location.pathname;
    if (!base.endsWith("/")) base += "/";
    // set href on confirm anchor to the delete endpoint
    if (deleteConfirm) deleteConfirm.setAttribute("href", base + `delete_comment/${commentId}/`);
    deleteModal.show();
  });
}
