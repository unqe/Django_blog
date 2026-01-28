(function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".btn-edit");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        const commentId = this.getAttribute("comment_id");
        const commentDiv = document.getElementById("comment" + commentId);
        if (!commentDiv) return;

        const originalHtml = commentDiv.innerHTML;
        const originalText = commentDiv.innerText.trim();

        // build form
        const form = document.createElement("form");
        form.method = "post";

        let base = window.location.pathname;
        if (!base.endsWith("/")) base += "/";
        form.action = base + "edit_comment/" + commentId + "/";

        // csrf token
        const csrf = document.createElement("input");
        csrf.type = "hidden";
        csrf.name = "csrfmiddlewaretoken";
        csrf.value = getCookie("csrftoken");
        form.appendChild(csrf);

        const textarea = document.createElement("textarea");
        textarea.name = "body";
        textarea.className = "form-control mb-2";
        textarea.rows = 4;
        textarea.value = originalText;
        form.appendChild(textarea);

        const updateBtn = document.createElement("button");
        updateBtn.type = "submit";
        updateBtn.className = "btn btn-primary btn-sm me-2";
        updateBtn.textContent = "Update";
        form.appendChild(updateBtn);

        const cancelBtn = document.createElement("button");
        cancelBtn.type = "button";
        cancelBtn.className = "btn btn-secondary btn-sm";
        cancelBtn.textContent = "Cancel";
        cancelBtn.addEventListener("click", function () {
          commentDiv.innerHTML = originalHtml;
        });
        form.appendChild(cancelBtn);

        commentDiv.innerHTML = "";
        commentDiv.appendChild(form);
      });
    });
  });
})();
