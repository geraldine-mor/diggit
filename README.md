# [diggit](https://diggit-938ea2f476b2.herokuapp.com)

| ![diggit logo](documentation/diggit-logo-small.png) | *Ask what you need or sow a few seeds* |
| --- | --- |

Developer: Geraldine Morey ([geraldine-mor](https://www.github.com/geraldine-mor))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://diggit-938ea2f476b2.herokuapp.com/)

⚠️ PROJECT INTRODUCTION AND RATIONALE⚠️

It is human nature to grow things and the majority of people have a garden of some description even if it is only a pot plant at home. Most community led garden advice forums tend to be Facebook groups, Reddit threads or visually unappealing and often difficult to use. diggit is different. It doesn't try to do too much, it has a single purpose: provide an online community for gardeners.  

diggit is a gardening forum aimed at gardeners of all levels, from first-time growers to seasoned horticulturalists. It is an online allotment or potting shed, a place for sharing ideas and asking questions or simply reading the expert's advice in the 'Digging Deeper' section. It allows users to upload images and ask "what's this?" or "what should I do?" with the community suggesting answers and voting for the best answers via likes. User posts are not confined to questions, they can share useful tips or brag about their own horticultural successes. Digging Deeper allows the site owner to share specially curated, seasonally appropriate, professional content to ensure that there is always a trusted knowledge source for the users.

During project idea discussions with my course facilitator, Tindy, we segued into general garden chat which gave me the idea to create a garden tips/questions sharing platform. This idea grew in my mind over the following days and became diggit: Ask what you need or sow a few seeds.

**Site Mockups**

⚠️![screenshot](documentation/mockup.png)

source: [diggit amiresponsive](https://ui.dev/amiresponsive?url=https://diggit-938ea2f476b2.herokuapp.com/)
## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

diggit exists to give gardeners of all levels a dedicated, visually engaging space 
to share knowledge, ask questions and access expert advice — free from the noise 
of general social media platforms.

**Primary User Needs**
- Site owners need a simple and intuitive way of maintaining high quality gardening content and moderating user generated content to ensure a welcoming, secure and trusted experience for their target users.
- Registered users need an intuitive way to share gardening knowledge, ask questions of a like-minded community and engage with the responses and expertise of fellow gardeners.
- Guests need an attractive and user friendly site to explore gardening questions and tips without the need to register but delivered in a manner designed to induce a desire to join in the discussion.

**Business Goals**
- Establish diggit as the primary resource for gardeners looking for peer advice and expert guidance in one place.
- Grow an active community where user generated content reduces the burden on the site owner to produce all the content.
- Convert guest browsers into registered members through a compelling and welcoming user experience.
- Maintain editorial standards through Digging Deeper expert advice to differentiate diggit from generic social media gardening groups.
<br><br>

**Needs-objectives mapping**
| User Need | Business Goal | Alignment | Resolution | 
| --- | --- | --- | --- |
| Guests want to browse the site content without the need to register | Convert guest users into registered users | Conflict | High quality user experiences encourages registration as a desire not a necessity | 
| Registered users need a quick and easy way to ask questions or share advice | Maintain high content standards to ensure trust | Conflict | Introduce community guidelines at registration to allow instant posting. Admin action is on violation rather than approving each post | 
| Users want trusted expert advice | Stand out from generic social media groups | Full | Digging Deeper provides both expert advice for the user and a USP for the site |
| Users want safe and appropriate content | User generated content reduces burden on site admins | Partial Conflict | Enable user reporting of unsafe or inappropriate content |
| Users want to feel heard and receive responses | Build a self-sustaining community | Full | Likes and comments build a strong community environment while providing timely feedback to users | 
| Users want intuitive site navigation | Reduce bounce rate | Full | Intuitive navigation design directly reduces bounce rate |
| Admin users need a simple and intuitive way of managing content | Maintain high content standards | Full | Django's built in admin panel provides an accessible management interface | 

_As an owner-operated platform, the business goals and admin user's needs are largely the same_

#### 2. Scope

**[Features](#features)** (see below)

**Functional Requirements**
- Authentication and access control: registration, login, logout, login state, guest restrictions
- CRUD for posts: create, read, update, delete 
- CRUD for comments: create, read, update, delete
- Role-based permissions: guest, registered user, admin
- Admin functionality: admin panel, content deletion, image management, Digging Deeper blog
- User feedback: confirmation prior to and after deletion, confirmation or error messages for post and comment saves, visual distinction for clickable items
- Data validation: user-facing forms include input validation and clear error messaging

**Content Requirements**

Static content — hardcoded, requires development to update:
- Brand identity, navigation, footer
- Community guidelines and code of conduct
- About section and contact information
- User interaction forms

Admin managed — maintained via Django admin panel:
- Digging Deeper blog posts
- Categories (names, colours, images)

User generated — created dynamically by registered users:
- Posts (text, optional image, categories)
- Comments and replies
- Likes and reactions

System generated:
- User feedback messages
- Like counts and post ordering
- Form validation errors

**Content Constraints**
 - Title length: Post titles restricted to 200 characters
 - Images: Images only accepted in ⚠️ .png or .jpg ⚠️ format ⚠️ and are limited to 1MB in size ⚠️
 - Categories: Limited to 20 in order to provide colour options that are guaranteed to meet accessibility contrast requirements
 - Language: Currently only english language supported.
 - Content moderation: Reactive content moderation allows for fast posting but opens the site to damaging content. Report button and a list of excluded words and phrases will try to control this.
 - Media types: Audio and video files are not currently supported.
 - ⚠️ External links: Users are encouraged to share brand and supplier names rather than links in the community guidelines. ⚠️  

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Digging Deeper, Community Posts, Register and login/logout (⚠️Contact⚠️).
- **Hierarchy**:
  - Homepage offers a brief welcoming introduction with options to continue as guest or login.
  - Community posts are displayed clearly in reverse chronological and popularity order, filterable by category tag. Each posts shows title, image (if used), author, category labels and created date 
  - Digging Deeper posts are displayed clearly with prominent filtering or search options.
  - Clear call-to-action buttons for account creation and engagement (e.g., commenting).

**User Flow**<br>
Guest users:
1. Guest users land on homepage, continue to browse posts → browse community posts and comments.
2. Navigate to Digging Deeper posts for more expert advice.
3. Report offensive content by registering for and account or through admin contact.
4. Create account to leave a comment or post → accept community guidelines and login.

Registeres users:
1. Registerered users land on homepage, login to account → browse community posts and comments.
2. React to posts and comments. 
3. Navigate to Digging Deeper posts for more expert advice.
4. Report offensive content through report button.
5. Create, update or delete posts, comments and replies → receive confirmation messages throughout.
6. Log out to protect account.

Admin users:
1. Login as admin → browse community posts to ensure guidelines are met.
2. Navigate to the admin panel → create, update or delete Digging Deeper articles.
3. Manage users → delete any in breach of community rules
4. Manage user content → review reported content, delete any inappropriate content.
5. Manage post categories → create, update and delete categories as needed.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

**[Modals](#modals)** (see below)

**Navigation Design** 

The navigation bar contains links to all pages as well as information about the user's login state. All users can see  options to login or register. When a user is logged in, a message reading "Logged in as: 'Username'" displays immediately below the navbar and the login link is replaced with a logout link. 

Admin users also have access to an additional link to the admin panel alongside the logout option. The navigation menu collapses on mobile and tablet for better usability but the login/logout links and status remain visible when the menu is collapsed.

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

For this project I wanted an earthy overall feeling to emulate the soil and growth nature of gardening with an electric green bright highlight for visual interest.

I used [coolors.co](https://coolors.co/dce0d9-261617-002500-52e620) to generate my color palette.

- ![#261617](https://img.shields.io/badge/%23261617-261617) primary colour.
- ![#DCE0D9](https://img.shields.io/badge/%23DCE0D9-dce0d9) secondary colour.
- ![#002500](https://img.shields.io/badge/%23002500-002500) alternative dark shade.
- ![#52E620](https://img.shields.io/badge/%2352E620-52e620) bright highlights.

![screenshot of colour palette](documentation/diggit-palette.png)

I had [claude.ai](https://claude.ai/new) run a contrast check on all colours and provide me with a table. As expected the only issues are the light/bright and dark/dark combinations.

![screenshot of colour contrast table](documentation/contrast-table.png)

A fixed palette of 20 colours was created for the category labels, to ensure high contrast is maintained throughout. A dark charcoal grey was chosen for the text ![#13171C](https://img.shields.io/badge/%2313171C-13171C) and the 20 shades were tested to ensure they meet WCAG AAA contrast standards.

| Colour | Hex Code | Contrast | Sample|
| --- | --- | --- | --- | 
| Beige | D9BAAF | 9.94 | ![Swatch of beige](documentation/colours/beige.png) |
| Grey | C3C2C2 | 10.13 | ![Swatch of grey](documentation/colours/grey.png) |
| Blue | A7CFFF | 11.16 | ![Swatch of blue](documentation/colours/blue.png) |
| Mint | B6E2CF | 12.67 | ![Swatch of mint](documentation/colours/mint.png) |
| Duckegg | 77CCBB | 9.55 | ![Swatch of duckegg](documentation/colours/duckegg.png) |
| Turquoise | 26C6DA | 8.72 | ![Swatch of turquoise](documentation/colours/turquoise.png) |
| Teal | 0CCABA | 8.72 | ![Swatch of teal](documentation/colours/teal.png) |
| Jade | 2ECC70 | 8.57 | ![Swatch of jade](documentation/colours/jade.png) |
| Green | 33FF55 | 13.36 | ![Swatch of green](documentation/colours/green.png) |
| Lime | A3D977 | 10.93 | ![Swatch of lime](documentation/colours/lime.png) |
| Lemon | FFF0A7 | 15.67 | ![Swatch of lemon](documentation/colours/lemon.png) |
| Yellow | FFD54F | 12.76 | ![Swatch of yellow](documentation/colours/yellow.png) |
| Amber | FFC107 | 11.05 | ![Swatch of amber](documentation/colours/amber.png) |
| Orange | FF9800 | 8.36 | ![Swatch of orange](documentation/colours/orange.png) |
| Salmon | FEAA8C | 9.73 | ![Swatch of salmon](documentation/colours/salmon.png) |
| Rose | FF8AB3 | 8.18 | ![Swatch of rose](documentation/colours/rose.png) |
| Bubblegum | FF7DAF | 7.55 | ![Swatch of bubblegum](documentation/colours/bubblegum.png) |
| Pink | FF78FF | 8.05 | ![Swatch of pink](documentation/colours/pink.png) |
| Lilac | FFA8FF | 10.55 | ![Swatch of lilac](documentation/colours/lilac.png) |
| Mauve | C7B6E2 | 9.62 | ![Swatch of mauve](documentation/colours/mauve.png) |

### Typography

I used [Google Fonts](https://fonts.google.com/)to select a monospace font for the diggit branding and used [Fontjoy](https://fontjoy.com/) to find pairings that I liked. The same dark charcoal grey was chosen for the body text ![#13171C](https://img.shields.io/badge/%2313171C-13171C)

- [PT Mono](https://fonts.google.com/specimen/PT+Mono) was used for the branding and main headings.
- [Dosis](https://fonts.google.com/specimen/Dosis?preview.script=Latn) was used for the main content.
- [Slabo 27px](https://fonts.google.com/specimen/Slabo+27px?preview.script=Latn) was used for headings and emphasis.
- ⚠️ --- May need another font for comments etc --- ⚠️
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the burger menu icon in the navbar.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I used [Whimsical](https://whimsical.com/ger-s-workspace48/diggit-Kj1maBK5a39CKjbMMnXobr) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot of homepage on mobile](documentation/wireframes/home-mobile.png) | ![screenshot of homepage on tablet](documentation/wireframes/home-tablet.png) | ![screenshot of homepage on desktop](documentation/wireframes/home-desktop.png) |
| Digging Deeper Blog | ![screenshot of blog page on mobile](documentation/wireframes/blog-mobile.png) | ![screenshot of blog page on tablet](documentation/wireframes/blog-tablet.png) | ![screenshot of blog page on desktop](documentation/wireframes/blog-desktop.png) |
| Diggit Forum | ![screenshot of Forum on mobile](documentation/wireframes/forum-mobile.png) | ![screenshot of Forum on tablet](documentation/wireframes/forum-tablet.png) | ![screenshot of Forum on desktop](documentation/wireframes/forum-desktop.png) |
| Expanded View | ![screenshot of expanded view on mobile](documentation/wireframes/expanded-mobile.png) | ![screenshot of expanded view on tablet](documentation/wireframes/expanded-tablet.png) | ![screenshot of expanded view on desktop](documentation/wireframes/expanded-desktop.png) |
| Create Post | ![screenshot of create post on mobile](documentation/wireframes/create-post-mobile.png) | ![screenshot of create post on tablet](documentation/wireframes/create-post-tablet.png) | ![screenshot of create post on desktop](documentation/wireframes/create-post-desktop.png) |
| Contact | ![screenshot of contact form on mobile](documentation/wireframes/contact-mobile.png) | ![screenshot of contact form on tablet](documentation/wireframes/contact-tablet.png) | ![screenshot of contact form on desktop](documentation/wireframes/contact-desktop.png) |
| 404 | ![screenshot of 404 page on mobile](documentation/wireframes/404-mobile.png) | ![screenshot of 404 page on tablet](documentation/wireframes/404-tablet.png) | ![screenshot of 404 page on desktop](documentation/wireframes/404-desktop.png) |

### Modals
This project uses a number of modals for various authentication and CRUD functions.

| Modal | Mockup |
| --- | --- |
| Register | ![screenshot of registration modal](documentation/modals/register.png) |
| Login | ![screenshot of login modal](documentation/modals/login.png) |
| Log out | ![screenshot of log out modal](documentation/modals/log-out.png) |
| Edit post | ![screenshot of edit post modal](documentation/modals/update-post.png) |
| Delete post | ![screenshot of delete post modal](documentation/modals/delete-post.png) |
| Comment | ![screenshot of comment modal](documentation/modals/comment.png) |
| Edit comment | ![screenshot of edit comment modal](documentation/modals/update-comment.png) |
| Delete comment | ![screenshot of delete comment modal](documentation/modals/delete-comment.png) |
| Report post | ![screenshot of report post modal](documentation/modals/report-post.png) |
| Report comment | ![screenshot of report comment modal](documentation/modals/report-comment.png) |

## User Stories

| Target | Expectation | Outcome | Prority |
| --- | --- | --- | --- |
| As a guest | I can view Digging Deeper posts | so that I can access professional gardening advice | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a site admin | I can create Digging Deeper posts | so that I can share professional advice with the community | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a site admin | I can edit and delete the Digging Deeper posts | so that I can keep the content accurate and up to date | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) | 
| As a registered user | I can comment on Digging Deeper posts | so that I can join the conversation | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) | 
| As a guest | I can register for an account | so that I can participate in the community | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a registering user | I can read and acknowledge the community guidelines | so that I understand the rules before posting | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a registered user | I can log in to my account | so that I can access my personalised content and actions | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a logged in user | I can log out of my account | so that my account stays secure | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a user | I can see my current login state | so that I always know whether I am logged in or out | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a guest | I can browse user's posts | so that I can read community tips and decide whether to join | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a user | I can view an individual post and its comments | so that I can read the full content and discussion | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000)|
| As a logged in user | I can create a post | so that I can ask questions or share tips with the gardening community | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a logged in user | I can edit or delete my posts | so that I have full control of the content I created | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a site admin | I can access an admin panel | so that I can control the content across the site | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a site admin | I can delete user content | so that I can ensure community guidelines are adhered to | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a logged in user | I can comment on posts | so that I can contribute to the discussion or answer a question | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) | 
| As a site admin | I can upload and change the default and blog images | so that I can keep the site fresh and attractive | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a guest | I can read comments | so that I can benefit from user's experience and decide if I want to join | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a user | I can contact the site admin | so that I can report an issue or ask a question | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a logged in user | I can edit or delete my comments | so that I can correct or remove comments that no longer represent me | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a guest | I can read a brief introduction to the site | so that I can decide to browse as a guest or signup | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a logged in user | I can react to comments | so that I can help the community identify the most helpful answers | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a post author | I can upload an image | so that I can ask questions or give advice about my own experiences | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a user | I can filter posts by category | so that I can find relevant content faster | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a user | I can report harmful content | so that site moderators can review and take action | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a user | I can see the most popular comments first | so that the most helpful answers are easy to find | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a logged in user | I can reply to comments | so that I can add more insight to the conversation | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can sort posts by date or popularity | so that I can find the most recent or most engaging content easily | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a logged in user | I can react to posts | so that I can quickly share my feelings without needing to comment | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can expect that multiple posts will spread over several pages | so that I can maintain a clean easy to use interface | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can signup to the newsletter | so that keep up to date with community news | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can search the site content by keyword | so that I can quickly find what I'm looking for | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |

⚠️ ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e)⚠️

## Features

⚠️ --- Work in Progress --- ⚠️

- Digging Deeper blog page
- Comments and replies
    * Edit/delete own comments
- User registration
    * Code of conduct 
- User login & log out
- Visible login state
- Open individual posts (either own page view or expand to fill)
- User post creation form
    * Post edit and delete buttons
- Post filters
- Post Search
- Admin Panel (handled by django)
- Bespoke 404 page with home and/or back button
- Image upload
- Comment likes
- Like counter
- Order comments / posts by like count
- Pagination
- Newsletter sign up 
- Content report button


### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Blog List | The homepage displays basic information about blog posts, including image, title, author, date, and a brief excerpt. | ![screenshot](documentation/features/blog-list.png) |
| View Post | Users can view the full blog post details, including any comments. | ![screenshot](documentation/features/view-post.png) |
| Pagination | Blog posts are displayed in pages, with six posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.png) |
| Add Comments | Authenticated visitors can comment on blog posts; comments require approval before being published. | ![screenshot](documentation/features/add-comment.png) |
| Edit Comments | Authenticated visitors can edit their own comments. | ![screenshot](documentation/features/edit-comment.png) |
| Delete Comments | Authenticated visitors can delete their own comments. | ![screenshot](documentation/features/delete-comment.png) |
| Comment Approvals | Admins can approve or disapprove comments submitted by users before they are visible on the blog post. | ![screenshot](documentation/features/comment-approval.png) |
| Create Post | Site owners can create/publish blog posts, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.png) |
| Update Post | Site owners can update/manage blog posts from the Django admin dashboard. | ![screenshot](documentation/features/update-post.png) |
| Delete Post | Site owners can delete blog posts from the Django admin dashboard. | ![screenshot](documentation/features/delete-post.png) |
| About Page | The About page displays the latest information about the site author, along with the option for visitors to send collaboration requests. | ![screenshot](documentation/features/about.png) |
| Collaboration Requests | Visitors can submit collaboration requests from the *About* page, which are later reviewed by the admin. | ![screenshot](documentation/features/collaboration.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

⚠️ INSTRUCTIONS ⚠️

Do you have additional ideas that you'd like to include on your project in the future? Fantastic, list them here! It's always great to have plans for future improvements. Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

A few examples are listed below to align with possible ways to improve on the sample walkthrough project, to give you some inspiration.

⚠️ --- END ---⚠️

- **Post Categories/Tags**: Allow users to categorize and tag blog posts, making it easier for visitors to filter content based on their interests.
- **Post Search Functionality**: Add a search bar for users to quickly find posts by keywords or phrases.
- **Post Likes/Dislikes or Upvotes**: Implement a "like" or "upvote" system for blog posts to encourage user engagement and give feedback to the author.
- **User Profiles**: Create personalized user profiles where authenticated users can view their comments, liked posts, and account information.
- **Comment Replies & Threads**: Enable users to reply to comments, creating nested comment threads for better discussions.
- **Post Sharing**: Add social media sharing buttons (e.g., Twitter, Facebook, LinkedIn) for users to share blog posts.
- **Notifications**: Implement a notification system that alerts users when their comments are approved, when new comments are made on a post they've commented on, or when new posts are published.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Post Analytics**: Provide post authors with analytics such as views, time spent reading, and engagement rates.
- **Multilingual Support**: Add the ability to write and view blog posts in multiple languages, broadening the audience.
- **Related Posts Recommendations**: Show related posts at the bottom of a blog post to encourage further reading and keep users engaged.
- **Content Flagging/Reporting**: Allow users to flag or report inappropriate content (comments or posts) for moderation.
- **SEO Optimization**: Implement features for SEO, such as meta tags, custom URLs, and keywords for better search engine ranking.
- **User Dashboard**: Provide users with a dashboard to track their activity, such as comments made, likes received, and blog posts they’ve interacted with.
- **Admin Dashboard Analytics**: Provide site admins with an analytics dashboard showing user activity, popular posts, most commented articles, etc.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |
| [![badge](https://img.shields.io/badge/Claude-grey?logo=claude&logoColor=D97757)](https://claude.ai) | Help debug, troubleshoot, and explain things. |

⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

⚠️ --- Work in Progress --- ⚠️

## Database Design

### Data Model

The main model for this project is the post - either admin created blogs or user created forum posts. Five other models interact with the post model in the form of User, Reactions, Comments, Comment Reactions and Categories.

There is also a model for messaging the site admin so that user messages are visible and actionable directly from the admin panel.

I used [dbdiagram.io](https://dbdiagram.io/d/diggit-69cf9ba58089629684134784) to create the ERD.

![screenshot](documentation/erd.png)


⚠️ RECOMMENDED ⚠️

Alternatively, or in addition to, a more comprehensive ERD can be auto-generated once you're at the end of your development stages, just before you submit. Follow the steps below to obtain a thorough ERD that you can include. Feel free to leave the steps below in the README for future use to yourself.

⚠️ --- END --- ⚠️

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/geraldine-mor/codestar_blog/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/geraldine-mor/diggit/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://gm-codestar-blog-fd27c1e92e9f.herokuapp.com).

## Deployment

The live deployed application can be found deployed on [Heroku](https://diggit-938ea2f476b2.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION geraldine-mor !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️
⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary, then remove those keys, or replace with whatever ones you're using. ⚠️

🛑 --- END --- 🛑

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION geraldine-mor !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️
⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary | AWS, then replace those keys with whatever keys you're using. ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/geraldine-mor/diggit).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/geraldine-mor/diggit.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/geraldine-mor/diggit)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/geraldine-mor/diggit).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

Eventually you'll want to learn how to use Git branches. Here's a helpful tutorial called [Learn Git Branching](https://learngitbranching.js.org) to bookmark for later.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
    - [Button Clicks](https://www.zapsplat.com/sound-effect-category/button-clicks)
    - [Lasers & Weapons](https://www.zapsplat.com/sound-effect-category/lasers-and-weapons/page/5)
    - [Puzzle Music](https://soundimage.org/puzzle-music)
    - [Camtasia Audio](https://library.techsmith.com/camtasia/assets/Audio)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.


 