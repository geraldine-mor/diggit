# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. There were errors initially with several of the files, detailed below with their fixes.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| blog | [digging_deeper.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/digging_deeper.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Fdigging_deeper%2F) | ![screenshot of validation no errors](documentation/validation/digging-deeper-html.png) | Trailing slash on void elements info is caused by the cloudinary field, I have no way to remove. |
| blog | [diggit_forum.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/diggit_forum.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Fdiggit_forum%2F) | ![screenshot of validation no errors](documentation/validation/diggit-forum-html.png) | Trailing slash on void elements info is caused by the cloudinary field, I have no way to remove.  |
| blog | [read_post.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/read_post.html) | [Sample validation link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Fapril-showers-and-garden-power-managing-spring-rai%2F) | ![screenshot of validation no errors](documentation/validation/read-post-html.png) | Trailing slash on void elements info is caused by the cloudinary field, I have no way to remove. |
| contact | [contact.html](https://github.com/geraldine-mor/diggit/blob/main/contact/templates/contact/contact.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Fcontact%2F) | ![screenshot of validation no errors](documentation/validation/contact-html.png) |  |
| templates | [home.html](https://github.com/geraldine-mor/diggit/blob/main/templates/home.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2F#textarea) | ![screenshot of validation no errors](documentation/validation/home-html.png) |  |
| templates | [login.html](https://github.com/geraldine-mor/diggit/blob/main/templates/account/login.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fdiggit_forum%2F) | ![screenshot of validation no errors](documentation/validation/login-html.png) |  |
| templates | [logout.html](https://github.com/geraldine-mor/diggit/blob/main/templates/account/logout.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Faccounts%2Flogout%2F%3Fnext%3D%2F) | ![screenshot of validation no errors](documentation/validation/logout-html.png) |  |
| templates | [signup.html](https://github.com/geraldine-mor/diggit/blob/main/templates/account/signup.html) | [Link to validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdiggit-938ea2f476b2.herokuapp.com%2Faccounts%2Fsignup%2F%3Fnext%3D%2F) | ![screenshot of validation no errors](documentation/validation/signup-html.png) |  |

**Initial Errors**
| Page | Errors | Actions Taken |
| --- | --- | --- |
| [home.html](https://github.com/geraldine-mor/diggit/blob/main/templates/home.html) | ![screenshot of homepage validation errors](documentation/validation-errors/home-validation-fail.png) | Removed trailing `</i>` |
| [signup.html](https://github.com/geraldine-mor/diggit/blob/main/templates/account/signup.html) | ![screenshot of signup validation errors](documentation/validation-errors/signup-validation-fail.png) | Assigned the id "id_password1_helptext"to the password instructions `<div>` |
| [diggit_forum.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/diggit_forum.html) | ![screenshot of diggit forum validation errors](documentation/validation-errors/diggit-forum-validation-errors.png) | Most of the errors were caused by `{{ post.excerpt \| linebreaks}}` being in a `<p>` element and creating another nested `<p>` element ![screenshot of nested paragraph elements](documentation/validation-errors/nested-p-elements.png) I changed this to a `<div>`. <br>Closed the `<div class="forum-backdrop">` to resolve the remaining errors |
| [digging_deeper.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/digging_deeper.html) | ![screenshot of digging deeper validation issues](documentation/validation-errors/digging-deeper-validation-errors.png) | A repeat of the issue from diggit_forum.html regarding the double `<p>` elements dealt with the same way.<br> The duplicate id of card-footer was changed to a class.<br> Links were rearranged to remove nesting rule violation |
| [read_post.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/read_post.html) | ![screenshot of read post validation errors](documentation/validation-errors/read-post-validation-errors.png) | Several `<p>` tags were changed to `<div>`<br>`<span>` containing a `<form>` was changed to `<div>`<br>Extra `</form>` elements removed<br>`{% endfor %}` relocated to outside the `</div>` because it was causing erroneous unclosed `<div>` errors. |
| [read_post.html](https://github.com/geraldine-mor/diggit/blob/main/blog/templates/blog/read_post.html) | ![screenshot of read post validation errors](documentation/validation-errors/read-post-errors-2.png) | Default placeholder text added to empty headings, replaced all `<h3>` elements with either `<h2` or `<p>` to avoid heading discrepancies between blog posts and forum posts |
| [login.html](https://github.com/geraldine-mor/diggit/blob/main/templates/account/login.html) | ![screenshot of login validation errors](documentation/validation-errors/login-html-error.png) | Created a hidden span to apply the id to since the password helptext is not appropriate in this instance |

### CSS

I used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https://diggit-938ea2f476b2.herokuapp.com) to validate all of my CSS files.

When testing via URL, I received 122 errors relating to Bootstrap and 947 warnings so I decided to validate by direct input instead:
![screenshot of inital errors](documentation/validation-errors/css-validation-errors.png)

| Directory | File |  Screenshot | Notes |
| --- | --- | --- | --- |
| static | [styles.css](https://github.com/geraldine-mor/diggit/blob/main/static/css/styles.css) |  ![screenshot of validated css](documentation/validation/validated-styles-css.png) | The warnings relate to the imported fonts and css variables not being checked |
| static | [buttons.css](https://github.com/geraldine-mor/diggit/blob/main/static/css/buttons.css) | ![screenshot of validated css](documentation/validation/validates-buttons-css.png) | The warnings all relate to css variables not being checked due to their dynamic nature |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate my JS file.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [script.js](https://github.com/geraldine-mor/diggit/blob/main/static/js/script.js) |  | ![screenshot of javascript no errors](documentation/validation/js-hint-no-errors.png) | Initial issues included an unnecessarily named function not being called and several missing or unnecessary semi-colons. All of these were easily rectified ![screenshot of js hint errors](documentation/validation-errors/initial-jshint.png) |


### Python

⚠️ Work in Progress ⚠️



You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

I used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. There were errors initially with several of the files, detailed below with their fixes.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| blog | [admin.py](https://github.com/geraldine-mor/diggit/blob/main/blog/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/admin.py) | ![screenshot of validation no errors](documentation/validation/blog-admin.png) | Code corrections [commit](https://github.com/geraldine-mor/diggit/commit/91a3ea3cf62574bc6c5fba1b1521d9c92c8555f8) |
| blog | [choices.py](https://github.com/geraldine-mor/diggit/blob/main/blog/choices.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/choices.py) | ![screenshot](documentation/validation/py-blog-choices.png) | ⚠️ Notes (if applicable) |
| blog | [forms.py](https://github.com/geraldine-mor/diggit/blob/main/blog/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/forms.py) | ![screenshot](documentation/validation/py-blog-forms.png) | ⚠️ Notes (if applicable) |
| blog | [models.py](https://github.com/geraldine-mor/diggit/blob/main/blog/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/models.py) | ![screenshot](documentation/validation/py-blog-models.png) | ⚠️ Notes (if applicable) |
| blog | [tests.py](https://github.com/geraldine-mor/diggit/blob/main/blog/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/tests.py) | ![screenshot](documentation/validation/py-blog-tests.png) | ⚠️ Notes (if applicable) |
| blog | [urls.py](https://github.com/geraldine-mor/diggit/blob/main/blog/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/urls.py) | ![screenshot](documentation/validation/py-blog-urls.png) | ⚠️ Notes (if applicable) |
| blog | [utils.py](https://github.com/geraldine-mor/diggit/blob/main/blog/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/utils.py) | ![screenshot](documentation/validation/py-blog-utils.png) | ⚠️ Notes (if applicable) |
| blog | [views.py](https://github.com/geraldine-mor/diggit/blob/main/blog/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/blog/views.py) | ![screenshot of validation no errors](documentation/validation/blog-views.png) | Code corrections [commit](https://github.com/geraldine-mor/diggit/commit/53964b9c1e8613668d3d21269ba00d8bf28b8fff) |
| contact | [admin.py](https://github.com/geraldine-mor/diggit/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png) | ⚠️ Notes (if applicable) |
| contact | [forms.py](https://github.com/geraldine-mor/diggit/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) | ⚠️ Notes (if applicable) |
| contact | [models.py](https://github.com/geraldine-mor/diggit/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) | ⚠️ Notes (if applicable) |
| contact | [tests.py](https://github.com/geraldine-mor/diggit/blob/main/contact/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/tests.py) | ![screenshot](documentation/validation/py-contact-tests.png) | ⚠️ Notes (if applicable) |
| contact | [urls.py](https://github.com/geraldine-mor/diggit/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.png) | ⚠️ Notes (if applicable) |
| contact | [views.py](https://github.com/geraldine-mor/diggit/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.png) | ⚠️ Notes (if applicable) |
| diggit | [settings.py](https://github.com/geraldine-mor/diggit/blob/main/diggit/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/diggit/settings.py) | ![screenshot](documentation/validation/py-diggit-settings.png) | ⚠️ Notes (if applicable) |
| diggit | [urls.py](https://github.com/geraldine-mor/diggit/blob/main/diggit/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/geraldine-mor/diggit/main/diggit/urls.py) | ![screenshot](documentation/validation/py-diggit-urls.png) | ⚠️ Notes (if applicable) |

**Initial Errors**
| File | Errors | Actions Taken |
| --- | --- | --- |
| blog/admin.py | ![screenshot of validation errors](documentation/validation-errors/blog-admin-errors.png) | Simple whitespace and blank line errors, easily corrected |
| blog/views.py | ![screenshot of validation errors](documentation/validation-errors/blog-views-errors.png) | For all line too long errors, I was able to break the line at a parentheses opening. For the whitespace, blank line and continuation indenting, I simply added or removed the issue as required. |
| blog/views.py | ![screenshot of validation errors](documentation/validation-errors/blog-views-errors-2.png) | Folowing code review and commenting, I had these errors and performed the same actions as before to rectify them. | 

## Responsiveness

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is to test the following 3 sizes:

- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of your results, to "prove" that you've actually tested them.

Using the [amiresponsive](http://ami.responsivedesign.is) mockup images (*or similar*) does not meet the requirements. Consider using some of the built-in device sizes from the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well. It showcases a higher level of manual tests, and can be seen as a positive inclusion!

⚠️ --- END --- ⚠️

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Add Blog | ![screenshot](documentation/responsiveness/mobile-add-blog.png) | ![screenshot](documentation/responsiveness/tablet-add-blog.png) | ![screenshot](documentation/responsiveness/desktop-add-blog.png) | Works as expected |
| Edit Blog | ![screenshot](documentation/responsiveness/mobile-edit-blog.png) | ![screenshot](documentation/responsiveness/tablet-edit-blog.png) | ![screenshot](documentation/responsiveness/desktop-edit-blog.png) | Works as expected |
| Blog Post | ![screenshot](documentation/responsiveness/mobile-blog-post.png) | ![screenshot](documentation/responsiveness/tablet-blog-post.png) | ![screenshot](documentation/responsiveness/desktop-blog-post.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various browsers. Consider testing at least 3 different browsers, if available on your system. You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the browsers you've tested, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time. Some of these are paid services, but some are free. If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

⚠️ --- END --- ⚠️

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Add Blog | ![screenshot](documentation/browsers/chrome-add-blog.png) | ![screenshot](documentation/browsers/firefox-add-blog.png) | ![screenshot](documentation/browsers/safari-add-blog.png) | Works as expected |
| Edit Blog | ![screenshot](documentation/browsers/chrome-edit-blog.png) | ![screenshot](documentation/browsers/firefox-edit-blog.png) | ![screenshot](documentation/browsers/safari-edit-blog.png) | Works as expected |
| Blog Post | ![screenshot](documentation/browsers/chrome-blog-post.png) | ![screenshot](documentation/browsers/firefox-blog-post.png) | ![screenshot](documentation/browsers/safari-blog-post.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Add Blog | ![screenshot](documentation/lighthouse/mobile-add-blog.png) | ![screenshot](documentation/lighthouse/desktop-add-blog.png) |
| Edit Blog | ![screenshot](documentation/lighthouse/mobile-edit-blog.png) | ![screenshot](documentation/lighthouse/desktop-edit-blog.png) |
| Blog Post | ![screenshot](documentation/lighthouse/mobile-blog-post.png) | ![screenshot](documentation/lighthouse/desktop-blog-post.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Blog Management | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data. | Post was created successfully and displayed correctly in the blog. | ![screenshot](documentation/defensive/create-post.png) |
| | Feature is expected to allow the blog owner to update existing posts. | Edited the content of an existing blog post. | Post was updated successfully with the new content. | ![screenshot](documentation/defensive/update-post.png) |
| | Feature is expected to allow the blog owner to delete blog posts. | Attempted to delete a blog post, confirming the action before proceeding. | Blog post was deleted successfully. | ![screenshot](documentation/defensive/delete-post.png) |
| | Feature is expected to retrieve a list of all published posts. | Accessed the blog owner dashboard to view all published posts. | All published posts were displayed in a list view. | ![screenshot](documentation/defensive/published-posts.png) |
| | Feature is expected to preview posts as drafts before publishing. | Created a draft post and previewed it. | Draft was displayed correctly in preview mode. | ![screenshot](documentation/defensive/preview-draft.png) |
| Comments Management | Feature is expected to allow the blog owner to approve or reject comments. | Approved and rejected comments from the dashboard. | Approved comments were published; rejected comments were removed. | ![screenshot](documentation/defensive/review-comments.png) |
| | Feature is expected to allow the blog owner to edit or delete comments. | Edited and deleted existing comments. | Comments were updated or removed successfully. | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) |
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png) |
| User Comments | Feature is expected to allow registered users to leave comments on blog posts. | Logged in and added comments to a blog post. | Comments were successfully added and marked as pending approval. | ![screenshot](documentation/defensive/add-comment.png) |
| | Feature is expected to display a notification that comments are pending approval. | Added a comment and checked the notification message. | Notification was displayed as expected. | ![screenshot](documentation/defensive/pending-approval.png) |
| | Feature is expected to allow users to edit their own comments. | Edited personal comments. | Comments were updated as expected. | ![screenshot](documentation/defensive/edit-user-comments.png) |
| | Feature is expected to allow users to delete their own comments. | Deleted personal comments. | Comments were removed as expected. | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features | Feature is expected to allow guest users to read blog posts without registering. | Opened blog posts as a guest user. | Blog posts were fully accessible without logging in. | ![screenshot](documentation/defensive/view-posts-guest.png) |
| | Feature is expected to display the names of other commenters on posts. | Checked the names of commenters on posts as a guest user. | Commenter names were displayed as expected. | ![screenshot](documentation/defensive/commenter-names.png) |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | ![screenshot](documentation/defensive/brute-force.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my experiences with my audience. | ![screenshot](documentation/features/feature01.png) |
| As a blog owner | I would like to update existing blog posts | so that I can correct or add new information to my previous stories. | ![screenshot](documentation/features/feature02.png) |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. | ![screenshot](documentation/features/feature03.png) |
| As a blog owner | I would like to retrieve a list of all my published blog posts | so that I can manage them from a central dashboard. | ![screenshot](documentation/features/feature04.png) |
| As a blog owner | I would like to preview a post as draft before publishing it | so that I can ensure formatting and content appear correctly. | ![screenshot](documentation/features/feature05.png) |
| As a blog owner | I would like to review comments before they are published | so that I can filter out spam or inappropriate content. | ![screenshot](documentation/features/feature06.png) |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. | ![screenshot](documentation/features/feature07.png) |
| As a blog owner | I would like to view a list of all comments (both approved and pending) | so that I can manage user engagement effectively. | ![screenshot](documentation/features/feature08.png) |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. | ![screenshot](documentation/features/feature09.png) |
| As a registered user | I would like to log in to the site | so that I can leave comments on blog posts. | ![screenshot](documentation/features/feature10.png) |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the blog. | ![screenshot](documentation/features/feature11.png) |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the owner's experiences. | ![screenshot](documentation/features/feature12.png) |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the comment. | ![screenshot](documentation/features/feature13.png) |
| As a registered user | I would like to receive a notification or message saying my comment is pending approval | so that I understand it hasn't been posted immediately. | ![screenshot](documentation/features/feature14.png) |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. | ![screenshot](documentation/features/feature15.png) |
| As a guest user | I would like to read blog posts without registering | so that I can enjoy the content without needing to log in. | ![screenshot](documentation/features/feature16.png) |
| As a guest user | I would like to browse past posts | so that I can explore the blog's full content history. | ![screenshot](documentation/features/feature17.png) |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments on posts. | ![screenshot](documentation/features/feature18.png) |
| As a guest user | I would like to see the names of other commenters on posts | so that I can get a sense of community interaction before registering. | ![screenshot](documentation/features/feature19.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature20.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Jest procedures, and remove/adjust where applicable.

- Installing Node.js (**Windows**)
  - https://codeinstitute.s3.eu-west-1.amazonaws.com/nodejs-installation-guides/Installing+and+maintaining+NodeJS+(Windows).pdf
- Installing Node.js (**MacOS**)
  - https://codeinstitute.s3.eu-west-1.amazonaws.com/nodejs-installation-guides/Installing+and+maintaining+NodeJS+(MacOS).pdf

⚠️ SAMPLE ⚠️

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality. In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `<enter>` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work. Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

/* jshint esversion: 11, jquery: true */
/* global jest, require, describe, beforeEach, afterEach, test, expect, global */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test. The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the very bottom of the file. Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
/* jshint esversion: 11, jquery: true */
/* global module */
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially. Write JS code that can get the tests to pass as part of the Red-Green refactor process. Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/automation/jest-coverage.png) |

#### Jest Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Jest tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with Jest.

⚠️ --- END --- ⚠️

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/geraldine-mor/diggit/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/geraldine-mor/diggit/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issue custom search](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

