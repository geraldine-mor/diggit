# [diggit](https://diggit-938ea2f476b2.herokuapp.com)

| ![diggit logo](documentation/diggit-logo-small.png) | *Ask what you need or sow a few seeds* |
| --- | --- |

Developer: Geraldine Morey ([geraldine-mor](https://www.github.com/geraldine-mor))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/geraldine-mor/diggit)](https://www.github.com/geraldine-mor/diggit)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://diggit-938ea2f476b2.herokuapp.com/)

It is human nature to grow things and the majority of people have a garden of some description even if it is only a pot plant at home. Most community led garden advice forums tend to be Facebook groups, Reddit threads or visually unappealing and often difficult to use. Diggit is different. It doesn't try to do too much, it has a single purpose: provide an online community for gardeners.  

Diggit is a gardening forum aimed at gardeners of all levels, from first-time growers to seasoned horticulturalists. It is an online allotment or potting shed, a place for sharing ideas and asking questions or simply reading the expert's advice in the 'Digging Deeper' section. It allows users to upload images and ask "what's this?" or "what should I do?" with the community suggesting answers and voting for the best answers via likes. User posts are not confined to questions, they can share useful tips or brag about their own horticultural successes. Digging Deeper allows the site owner to share specially curated, seasonally appropriate, professional content to ensure that there is always a trusted knowledge source for the users.

During project idea discussions with my course facilitator, Tindy, we segued into general garden chat which gave me the idea to create a garden tips/questions sharing platform. This idea grew in my mind over the following days and became Diggit: Ask what you need or sow a few seeds.

**Site Mockups**

![screenshot](documentation/mockup.png)

source: [diggit amiresponsive](https://ui.dev/amiresponsive?url=https://diggit-938ea2f476b2.herokuapp.com/)
## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

Diggit exists to give gardeners of all levels a dedicated, visually engaging space 
to share knowledge, ask questions and access expert advice — free from the noise 
of general social media platforms.

**Primary User Needs**
- Site owners need a simple and intuitive way of maintaining high quality gardening content and moderating user generated content to ensure a welcoming, secure and trusted experience for their target users.
- Registered users need an intuitive way to share gardening knowledge, ask questions of a like-minded community and engage with the responses and expertise of fellow gardeners.
- Guests need an attractive and user friendly site to explore gardening questions and tips without the need to register but delivered in a manner designed to induce a desire to join in the discussion.

**Business Goals**
- Establish Diggit as the primary resource for gardeners looking for peer advice and expert guidance in one place.
- Grow an active community where user generated content reduces the burden on the site owner to produce all the content.
- Convert guest browsers into registered members through a compelling and welcoming user experience.
- Maintain editorial standards through Digging Deeper expert advice to differentiate Diggit from generic social media gardening groups.
<br><br>

**Needs-objectives mapping**
| User Need | Business Goal | Alignment | Resolution | 
| --- | --- | --- | --- |
| Guests want to browse the site content without the need to register | Convert guest users into registered users | Conflict | High quality user experiences encourages registration as a desire not a necessity | 
| Registered users need a quick and easy way to ask questions or share advice | Maintain high content standards to ensure trust | Conflict | Introduce community guidelines at registration to allow instant posting. Admin action is on violation rather than approving each post | 
| Users want trusted expert advice | Stand out from generic social media groups | Full | Digging Deeper provides both expert advice for the user and a USP for the site |
| Users want safe and appropriate content | User generated content reduces burden on site admins | Partial Conflict | Users can message admin to report any content issues via the contact page |
| Users want to feel heard and receive responses | Build a self-sustaining community | Full | Likes and comments build a strong community environment while providing timely feedback to users | 
| Users want intuitive site navigation | Reduce bounce rate | Full | Intuitive navigation design directly reduces bounce rate |
| Admin users need a simple and intuitive way of managing content | Maintain high content standards | Full | Django's built in admin panel provides an accessible management interface | 

_As an owner-operated platform, the business goals and admin users' needs are largely the same_

#### 2. Scope

**[Features](#features)** (see below)

**Functional Requirements**
- Authentication and access control: registration, login, logout, login state, role-based restrictions. Unauthenticated users are redirected to the login page if they attempt to access restricted functionality directly.
- CRUD for posts: create, read, update, delete 
- CRUD for comments: create, read, update, delete
- Role-based permissions: guest, registered user, admin
- Admin functionality: admin panel, content deletion, Digging Deeper blog
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
- Categories 

User generated — created dynamically by registered users:
- Posts (text, image (optional), categories)
- Comments and replies
- Likes

System generated:
- User feedback messages
- Like counts and post ordering
- Form validation errors

**Content Constraints**
 - Title length: Post titles restricted to 200 characters
 - Images: Images up to 10MB as per Cloudinary
 - Categories: Limited to 20 in order to provide colour options that are guaranteed to meet accessibility contrast requirements
 - Language: Currently only english language supported.
 - Content moderation: Reactive content moderation allows for fast posting but opens the site to damaging content.
 - Media types: Audio and video files are not currently supported.
 - External links: Users are asked not to share external links in the community guidelines. Llnks added in posts and comments are displayed as plain text.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Digging Deeper, Community Posts, Register/login/logout and Contact.
- **Hierarchy**:
  - Homepage offers a brief welcoming introduction with options to continue as guest or login.
  - Community posts are displayed clearly in reverse chronological order Each posts shows title, image (if used), author, category labels and created date. Limited to 6 post previews per page.
  - Digging Deeper posts are displayed clearly in reverse chronological order. Limited to 4 post previews per page.
  - Clear call-to-action buttons for account creation and engagement (e.g. commenting).

**User Flow**<br>
Guest users:
1. Guest users land on homepage, continue to browse posts → browse community posts and comments.
2. Navigate to Digging Deeper posts for more expert advice.
3. Report offensive content by messaging admin on the contact page.
4. Create account to leave a comment or post → accept community guidelines and login.

Registered users:
1. Registered users land on homepage, login to account → browse community posts and comments.
2. React to posts and comments. 
3. Navigate to Digging Deeper posts for more expert advice.
4. Create, update or delete posts, comments and replies → receive confirmation messages throughout.
5. Log out to protect account.

Admin users:
1. Login as admin → browse community posts to ensure guidelines are met.
2. Navigate to the admin panel → create, update or delete Digging Deeper articles.
3. Manage users → delete any in breach of community rules.
4. Read user's messages → take action as appropriate.
5. Manage user content → review content, delete any inappropriate content.
6. Manage post categories → create, update and delete categories as needed.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

**[Modals](#modals)** (see below)

**Navigation Design** 

The navigation bar contains links to all pages as well as information about the user's login state. All users can see options to login or register. When a user is logged in, a message reading "Welcome: 'First Name'" displays immediately below the navbar and the login link is replaced with a logout link.

On smaller screens the login/register/logout links are placed in the footer.

Admin users also have access to an additional link to the admin panel alongside the navigation links. The navigation menu collapses on mobile and tablet for better usability.

### Design Decisions
Several decisions were made during development that deviate from conventional UX patterns:
 - **Reactive Content Moderation**: Most community platforms implement a moderation queue, requiring admin approval before user-generated content is published. Diggit takes a reactive approach, allowing posts and comments to go live immediately - as would be expected with a social network/media platform. This decision prioritises user experience — forcing users to wait for approval creates friction and discourages participation, particularly in the early stages of a community. The trade-off is accepted: users are presented with and must acknowledge the community guidelines at registration, and the contact form and admin panel provide the tools needed to act swiftly on any violations. 
 - **Popovers Instead of Modals for CRUD Actions**: Initial wireframes planned for modals to house the edit and delete forms for posts and comments. During development, popovers were chosen instead. Modals interrupt the user's context by overlaying the entire page, whereas popovers anchor directly to the element being acted on, keeping the user oriented within the content. This felt more appropriate for a community forum where users may be managing their contributions mid-conversation. The trade-off is that popovers offer less visual prominence than modals, but clear labelling and consistent placement mitigate this.
 - **Links Rendered as Plain Text**: User-submitted content in posts and comments does not render hyperlinks as clickable anchors. This is a deliberate security decision — clickable links in user-generated content introduce risks including phishing, spam and malicious redirects that are difficult to moderate reactively. Users are advised of this in the community guidelines. The trade-off is a minor reduction in convenience for users sharing legitimate resources, but this is considered acceptable given the community's focus on gardening advice rather than resource sharing.
 - **Authentication Links in Footer on Mobile**: On smaller screens, the login, logout and register links are moved from the navigation bar to the footer rather than being housed in the hamburger menu alongside the page navigation links. This decision was made to keep the mobile navigation menu clean and focused on page navigation. Authentication is a secondary action for most visits — users are either already logged in or are browsing as a guest — and the footer remains accessible without scrolling on most content pages. The trade-off is a slight departure from the convention of keeping all navigation in one place on mobile, but the login state indicator in the navbar ensures users are never unaware of their current status.

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

I used [Google Fonts](https://fonts.google.com/)to select a monospace font for the Diggit branding and used [Fontjoy](https://fontjoy.com/) to find pairings that I liked. The same dark charcoal grey was chosen for the body text ![#13171C](https://img.shields.io/badge/%2313171C-13171C)

- [PT Mono](https://fonts.google.com/specimen/PT+Mono) was used for the branding and main headings.
- [Dosis](https://fonts.google.com/specimen/Dosis?preview.script=Latn) was used for the main content.
- [Slabo 27px](https://fonts.google.com/specimen/Slabo+27px?preview.script=Latn) was used for headings and emphasis.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the burger menu icon in the navbar.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes. The finished site deviated somewhat from the initial designs as plans changed.
I used [Whimsical](https://whimsical.com/ger-s-workspace48/diggit-Kj1maBK5a39CKjbMMnXobr) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot of homepage on mobile](documentation/wireframes/home-mobile.png) | ![screenshot of homepage on tablet](documentation/wireframes/home-tablet.png) | ![screenshot of homepage on desktop](documentation/wireframes/home-desktop.png) |
| Digging Deeper Blog | ![screenshot of blog page on mobile](documentation/wireframes/blog-mobile.png) | ![screenshot of blog page on tablet](documentation/wireframes/blog-tablet.png) | ![screenshot of blog page on desktop](documentation/wireframes/blog-desktop.png) |
| Diggit Forum | ![screenshot of Forum on mobile](documentation/wireframes/forum-mobile.png) | ![screenshot of Forum on tablet](documentation/wireframes/forum-tablet.png) | ![screenshot of Forum on desktop](documentation/wireframes/forum-desktop.png) |
| Single Post View | ![screenshot of expanded view on mobile](documentation/wireframes/expanded-mobile.png) | ![screenshot of expanded view on tablet](documentation/wireframes/expanded-tablet.png) | ![screenshot of expanded view on desktop](documentation/wireframes/expanded-desktop.png) |
| Create Post | ![screenshot of create post on mobile](documentation/wireframes/create-post-mobile.png) | ![screenshot of create post on tablet](documentation/wireframes/create-post-tablet.png) | ![screenshot of create post on desktop](documentation/wireframes/create-post-desktop.png) |
| Contact | ![screenshot of contact form on mobile](documentation/wireframes/contact-mobile.png) | ![screenshot of contact form on tablet](documentation/wireframes/contact-tablet.png) | ![screenshot of contact form on desktop](documentation/wireframes/contact-desktop.png) |
| 404 | ![screenshot of 404 page on mobile](documentation/wireframes/404-mobile.png) | ![screenshot of 404 page on tablet](documentation/wireframes/404-tablet.png) | ![screenshot of 404 page on desktop](documentation/wireframes/404-desktop.png) |

### Authentication & CRUD UI Planning
Initial planning included a range of modals for authentication forms and CRUD actions. In reality the authentication forms are templates and I used popovers rather than modals to house the CRUD forms.

The general design idea remains the same though.

| Form | Mockup |
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

_Report post and report comment were part of the initial planning but were descoped during development_

## User Stories

| Target | Expectation | Outcome | Priority |
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
| As a site admin | I can upload and change the blog images | so that I can keep the site fresh and attractive | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a guest | I can read comments | so that I can benefit from user's experience and decide if I want to join | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a user | I can contact the site admin | so that I can report an issue or ask a question | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a logged in user | I can edit or delete my comments | so that I can correct or remove comments that no longer represent me | ![Must Have](https://img.shields.io/badge/Must_Have-ff0000) |
| As a guest | I can read a brief introduction to the site | so that I can decide to browse as a guest or signup | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a logged in user | I can react to comments | so that I can help the community identify the most helpful answers | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a post author | I can upload an image | so that I can ask questions or give advice about my own experiences | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a user | I can see the most popular comments first | so that the most helpful answers are easy to find | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a user | I want to return to the page I was viewing after signup/login | so that I can continue interacting with the content | ![Should Have](https://img.shields.io/badge/Should_Have-ff8c00) |
| As a logged in user | I can reply to comments | so that I can add more insight to the conversation | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can expect that multiple posts will spread over several pages | so that I can maintain a clean easy to use interface | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can assign categories to my post | so that it can be discovered by other users | ![Could Have](https://img.shields.io/badge/Could_Have-1d76db) |
| As a user | I can sort posts by date or popularity | so that I can find the most recent or most engaging content easily | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a logged in user | I can react to posts | so that I can quickly share my feelings without needing to comment | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a user | I can filter posts by category | so that I can find relevant content faster | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a user | I can report harmful content | so that site moderators can review and take action | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a user | I can signup to the newsletter | so that keep up to date with community news | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a user | I can search the site content by keyword | so that I can quickly find what I'm looking for | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |
| As a user | I can choose a default image for my post | so that it is visually more engaging | ![Won't Have](https://img.shields.io/badge/Won't_Have-6e6e6e) |


## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register for an account. New users are presented with the community code of conduct and must acknowledge it before completing registration. | ![screenshot of signin page](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. Users are returned to the page they were viewing prior to login. | ![screenshot of login page](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot of logout page](documentation/features/logout.png) |
| Login State | The navigation bar reflects the user's current login state at all times, showing different options depending on whether the user is logged in or out. | ![screenshot of logged in user login state](documentation/features/login-state.png) ![screenshot of logged out user login state](documentation/features/logged-out.png) ![screenshot of admin user login state](documentation/features/admin-state.png) |
| Digging Deeper Blog | The Digging Deeper page displays professional gardening advice post previews created by site admins, including image, title, author, and date. | ![screenshot of digging deeper page](documentation/features/digging-deeper.png) |
| Diggit Forum | The Diggit Forum community post feed displays previews of posts created by registered users, allowing users to browse tips and questions from the community. | ![screenshot of diggit forum](documentation/features/diggit-forum.png) |
| View Post | Users can open an individual post to read the full content and view its comments. | ![screenshot of expanded post](documentation/features/read-post.png) |
| Create Post | Logged in users can create their own posts to ask questions or share tips with the gardening community, including uploading an image. | ![screenshot of post creation form](documentation/features/create-post.png) |
| Edit Post | Logged in users can edit their own posts at any time. | ![screenshotofedit post form](documentation/features/edit-post.png) |
| Delete Post | Logged in users can delete their own posts at any time. | ![screenshot of delete post form](documentation/features/delete-post.png) |
| Add Comment | Logged in users can comment on any post to contribute to the discussion. Guests without an account can only read comments. | ![screenshot of add comment form](documentation/features/add-comment.png) |
| Edit Comment | Logged in users can edit their own comments. | ![screenshot of edit comment form](documentation/features/edit-comment.png) |
| Delete Comment | Logged in users can delete their own comments. | ![screenshot of delete comment form](documentation/features/delete-comment.png) |
| Comment Likes | Logged in users can like comments to help the community identify the most helpful answers. | ![screenshot of comment likes](documentation/features/comment-likes.png) |
| Comment Ordering | Comments are ordered by like count so that the most helpful responses are displayed first. | ![screenshot of timestamp ordering](documentation/features/datetime-order.png) ![screenshot of likes affecting order](documentation/features/comment-likes.png) |
| Replies | Logged in users can reply directly to comments to add further insight to a conversation. | ![screenshot](documentation/features/replies.png) |
| Pagination | Post preview pages are paginated to keep the interface clean and easier to navigate. | ![screenshot of pagination controls](documentation/features/pagination.png) |
| Contact Form | Users can contact the site admin to report an issue or ask a question via a dedicated contact form. | ![screenshot of contact form](documentation/features/contact.png) |
| Admin Panel | Site admins have access to the Django admin panel to manage all site content and ensure community guidelines are upheld. | ![screenshot of admin panel](documentation/features/admin-panel.png) |
| Admin - Create Blog Post | Site admins can create and publish Digging Deeper posts, including uploading a featured image, from the Django admin panel. | ![screenshot of admin create post form](documentation/features/admin-blog.png) |
| Admin - Edit Blog Post | Site admins can edit existing Digging Deeper posts to keep content accurate and up to date. | ![screenshot of admin edit post form](documentation/features/admin-edit.png) |
| Admin - Delete Blog Post | Site admins can delete Digging Deeper posts and user-generated content to ensure community guidelines are upheld. | ![screenshot of admin delete page](documentation/features/admin-delete.png) |
| 404 Page | A custom 404 page is displayed when a user navigates to a non-existent page, maintaining the site's look and feel and providing a clear route back to the homepage. | ![screenshot](documentation/features/404.png) |
| Homepage | The homepage provides a welcoming introduction to the Diggit community, a brief description of the platform's purpose, and three call-to-action cards directing users to Ask the Community, Share your Wins, and explore the Digging Deeper expert blog. The layout is designed to immediately communicate the site's purpose to new visitors and provide clear onward navigation without the need to register. | ![screenshot of homepage](documentation/features/home.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to users for both successful and unsuccessful actions. Feedback messages are triggered by post and comment create, update and delete, login and logout. | ![screenshot](documentation/features/messages.png) |

### Future Features

- **Post Category Default Images**: Allow users to select a default category image to enhance their posts where they don't have an image.
- **Category Filtering**: Allow users to filter the post lists based on post categories
- **Post Search Functionality**: Add a search bar for users to quickly find posts by keywords or phrases.
- **Post Likes and ordering**: Implement a "like" or "reactions" system for the posts to provide instant feedback and allow ordering by popularity.
- **User Profiles**: Create personalised user profiles where authenticated users can view their comments, liked posts, and account information.
- **User Feed**: Allow users to share posts to their feed for easy reference.
- **User Following**: Implement a system to allow users to "follow" fellow users that appeal to them.
- **Nested Threads**: Enable replies to replies with clear thread following.
- **Built-in enforcement of community rules**: Enable post screening for prohibited words and/or phrases.
- **Notifications**: Implement a notification system that alerts users when there is new content or if their posts have received a comment.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Report Content**: Add a button directly to posts and comments to implement reported behaviour (greyed out, links desabled) with admin review required.
- **Post Analytics**: Provide post authors with analytics such as views, time spent reading, and engagement rates.
- **Multilingual Support**: Add the ability to write and view blog posts in multiple languages, broadening the audience.
- **Related Posts Recommendations**: Show related posts at the bottom of a blog post to encourage further reading and keep users engaged.
- **User Dashboard**: Provide users with a dashboard to track their activity, such as comments made, likes received, and blog posts they’ve interacted with.
- **Admin Dashboard Analytics**: Provide site admins with an analytics dashboard showing user activity, popular posts, most commented articles, etc.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.
- **Mobile App**: Develop the site into a mobile app for users to have a better experience on the go.
- **Social login**: Enable users to login via their Google or social media accounts.
- **Draft Posts**: Allow users to save posts as drafts to be completed later.
- **Post Scheduling**: Allow admins to schedule posts for efficiency and ease of use.
- **Diggit Calendar**: Develop a gardener's year calendar with important jobs and planting schedules clearly marked and searchable.
- **Plant Database Integration**: Develop a searchable plant database with planting and care information which is also taggable directly from the posts. 
- **Notice Board**: A place for users to post services or links that are useful to the community.
- **Marketplace**: Users can post adverts for item they are looking to donate, swap or sell.
- **Site Shop**: Admin can upload products to the site shop where they could sell gardening books, seeds, tools, branded merchandise and gardening inspired gifts. 
- **Images in comments**: It would be useful in future to add the ability to upload images in the comments.
- **Emoji Keyboard**: Emojis only currently available to mobile and tablet users, enhance desktop experience by adding an emoji keyboard.
- **UX Improvements**: Add open in place for forum posts and ensure that the page loads in the same place after comment and likes saves.

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
| [![badge](https://img.shields.io/badge/Claude-grey?logo=claude&logoColor=D97757)](https://claude.ai) | Help plan, explain things and assist with documentation. |
| [![badge](https://img.shields.io/badge/dbdiagram.io-grey?)](https://dbdiagram.io/home) | Construct ERD |
| [![badge](https://img.shields.io/badge/Whimsical-grey?)](https://whimsical.com/) | Wireframes |

## Database Design

### Data Model

The central model is Post, which handles both the admin created Digging Deeper blog posts and the user generated forum posts, differentiated by the `post_type` field.

Post connects to User as author and to Category through a Post_category junction table forming a many-to-many relationship. 

The Comment model links to both Post and User and includes a self-referencing `parent` field to support replies.

CommentLikes links to Comment and User to track per-user likes.

The User model is Django's built-in model. The is_superuser field is depicted in the ERD as `role` to highlight its function in controlling access to the admin panel and differentiating site admins from regular users.

Finally the Message model is independent of the Post structure and stores contact form submissions with a `read` field allowing admins to track actioned messages.

I used [dbdiagram.io](https://dbdiagram.io/d/diggit-69cf9ba58089629684134784) to create the ERD and referenced it throughout the build.

![screenshot](documentation/erd.png)

At the end of the project I used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps I took are as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `uv pip install pygraphviz`
- in my `settings.py` file, I made sure the following was in my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o advanced-erd.png`
- drag the new `advanced-erd.png` file into my `documentation/` folder
- finally, in the terminal: `uv pip uninstall pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/users/geraldine-mor/projects/8) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/geraldine-mor/diggit/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/geraldine-mor/diggit?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/geraldine-mor/diggit/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization at project level.

Each user story was written to address one or more of the business goals and primary user needs indentified in the strategy plane, ensuring that all development work could be traced back to a defined project objective.

- **Must Have**: guaranteed to be delivered 
- **Should Have**: adds significant value, but not vital 
- **Could Have**: has small impact if left out 
- **Won't Have**: not a priority for this iteration - future features

When user stories were moved into a milestone (or sprint), they were re-categorised within the timebox. Labels were used to denote the EPIC, MoSCoW classification and Story Points.

![screenshot of milestones](documentation/gh-milestones.png)
![screenshot of issue history](documentation/gh-issue-history.png)

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

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

- `uv pip install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `uv pip freeze > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.13` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

- Select Github as the **deployment method**, you may need to log in to your GitHub, choose your app repository.  

- Select **Manual Deploy** from the Heroku app, deploying the main branch only after setting `DEBUG=False`. It is not advisable to use automatic deploys in order to avoid deploying the site with `DEBUG=True`.


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
    - `uv pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `uv pip freeze > requirements.txt`
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

- `uv pip install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

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

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Codestar Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [dbdiagram.io](https://dbdiagram.io/d/69cf9ba58089629684134784) | Creating the ERD |
| [DBML](https://dbml.dbdiagram.io/docs/) | DBML syntax help | 
| [Coolors](https://coolors.co/dce0d9-261617-002500-52e620) | Colour palette |
| [Google Fonts](https://fonts.google.com/) | Fonts |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stack Overflow](https://stackoverflow.com/questions/44837733/how-to-make-add-replies-to-comments-in-django) | Comment Replies |
| [Django](https://docs.djangoproject.com/en/6.0/ref/models/constraints/) | Constraints - unique likes |
| [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Models) | Using unique constraint |
| [Stack Overflow](https://stackoverflow.com/questions/60523103/why-save-method-has-another-save-method-with-super-in-django-model) | Using the save() method to update signup form |
| [w3 Schools](https://www.w3schools.com/django/django_admin_set_list_display.php) | Using ModelAdmin to set up the admin panel |
| [Django Forum](https://forum.djangoproject.com/t/cant-create-link-to-admin-page-in-my-template/12533/7) | Link to admin page from site |
| [Django](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#ref-templates-builtins-filters) | Date filter to remove time from date stamp |
| [Stack Overflow](https://stackoverflow.com/questions/22767509/python-get-the-x-first-words-in-a-string) | Returning the first x words - excerpt helper function |
| [Stack Overflow](https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string) | Turning the list back into a string |
| [Django Extensions](https://django-extensions.readthedocs.io/en/latest/field_extensions.html) | AutoSlugField - to ensure unique slugs where posts have the same title |
| [Django](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/) | Exclude excerpt from admin post form | 
| [Stack Overflow](https://stackoverflow.com/a/12308807) | Customising the signup form |
| [Django](https://docs.djangoproject.com/en/5.2/ref/forms/widgets/) | Djangos form widgets |
| [Bootstrap](https://getbootstrap.com/docs/5.1/forms/checks-radios/) | Toggle switch (signup form) |
| [w3 Schools](https://www.w3schools.com/cssref/pr_pos_overflow.php) | Scrollable terms and conditions |
| [Django](https://docs.djangoproject.com/en/5.2/ref/forms/api/#django.forms.Form.label_suffix) | Remove colon from form label |
| [Stack Overflow](https://stackoverflow.com/a/63551565) | request.resolver_match.url_name conditional display based on url |
| [w3 Schools](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_att_popover2) | Popovers used for forms |
| [Django](https://github.com/django/django/blob/main/django/utils/text.py#L224) | Truncator to show preview of comment in admin panel |
| [Cloudinary](https://cloudinary.com/documentation/django_helper_methods_tutorial) | Image uploads | 
| [Django](https://docs.djangoproject.com/en/6.0/topics/http/file-uploads/) | request.FILES to accept image uploads |
| [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest) | .closest() method used on like buttons (replaced by $(this).parent) | 
| [Django](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#exists) | Using .exists() with querysets to toggle user likes |
| [Django](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.create) | Working with querysets specifically .create() and .delete() for toggling the CommentLike instance per user | 
| [Medium](https://medium.com/@akshatgadodia/chapter-8-extending-querysets-with-custom-methods-in-django-orm-d0b13f05408f) | Custom querysets and methods used for comment ordering |
| [Django Forum](https://forum.djangoproject.com/t/model-methods-custom-managers-queryset-when-to-use-them/7028/3) | Custom querysets and methods used for comment ordering |
| [Medium](https://python.plainenglish.io/enhancing-security-and-maintainability-custom-managers-and-querysets-in-django-638f77e69117) | Custom querysets and methods used for comment ordering |
| [Stack Overflow](https://stackoverflow.com/questions/806835/django-redirect-to-previous-page-after-login) | Return to same page following login/signup/logout |
| [Django](https://docs.djangoproject.com/en/6.0/topics/auth/default/) | Login required decorator |
| [Django](https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values) | Form initial values to avoid asking the user for name and email on the contact form |
| [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover) | Show/hide popover manually in JS |
| [Django](https://docs.djangoproject.com/en/6.0/topics/pagination/) | Pagination in function based views |
| [Django](https://docs.djangoproject.com/en/5.2/ref/forms/widgets/#checkboxselectmultiple) | Checkbox field for categories on the create post form |
| [oddbird](https://github.com/oddbird/popover-polyfill) | Popoverfill |
| [Cloudinary](https://cloudinary.com/documentation/resizing_and_cropping) | Cropping and optimizing images |
| [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env) | env(safe-area-inset-bottom) css function |
| [Claude](https://claude.ai) | Help with code logic and explanations, documentation and planning. |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Adobe Stock](https://as1.ftcdn.net/v2/jpg/16/01/00/92/1000_F_1601009208_6OIfBMxLi3sEUC3DLK3wdmxzGlbY0lgW.jpg) | Diggit logo |
| [Freepik](https://www.freepik.com/free-photo/shot-white-bench-park_17465507.htm#fromView=search&page=1&position=5&uuid=1d759506-28fd-461d-b3fe-94d64b5c0d87&query=garden) | Homepage backdrop |
| [Magnific](https://www.magnific.com/free-photo/ripe-strawberry-hanging-from-plant_426972403.htm#fromView=search&page=1&position=4&uuid=7994d07b-3c9e-4ca9-a723-45b484f5ca95&query=strawberry+plant) | Strawberry plant |
| [Pexels](https://www.pexels.com/photo/serene-overgrown-meadow-in-rural-taiwan-29698253/) | Overgrown grass |
| [Adobe Stock](https://as2.ftcdn.net/v2/jpg/01/71/50/01/1000_F_171500112_9tRgKpwBkuh7pk4cAgug8PnnO48wxpbw.jpg) | April showers post |
| [Pexels](https://www.pexels.com/photo/tranquil-autumn-scene-with-wooden-fence-and-trees-34266490/) | Shady fence | 
| [Pexels](https://www.pexels.com/photo/gray-steel-watering-can-beside-brown-wooden-fence-5919766/) | Raised bed |
| [Pexels](https://www.pexels.com/photo/vegetables-on-the-soil-5503338/) | Compost bin |
| [Pexels](https://www.pexels.com/photo/close-up-shot-of-hosta-sieboldiana-leaves-9379214/) | Hosta slugs |
| [Pexels](https://www.pexels.com/photo/close-up-of-a-cute-forest-mouse-in-nature-30374722/) | Mouse |
| [Adobe Stock](https://as2.ftcdn.net/v2/jpg/03/81/19/89/1000_F_381198933_gtRts0ctYpFqRyWyMVTcGtKOnFNGSPgz.jpg) | Late autumn tasks post |
| [Pikwizard](https://pikwizard.com/photo/sunlit-planting-onion-bulbs-with-metal-trowel-in-rich-soil-closeup-for-spring-garden/6168844f5eb786ff8d926733247b0281/) | October garden care post |
| [Pexels](https://www.pexels.com/photo/fresh-organic-vegetables-and-fruits-display-35974369/) | Harvest time post |
| [Pexels](https://www.pexels.com/photo/decorative-clock-in-serene-garden-setting-36091191/) | Chelsea flower show post |
| [Pexels](https://www.pexels.com/photo/vibrant-floral-garden-in-full-bloom-36825680/) | Summer garden post |
| [Pexels](https://www.pexels.com/photo/close-up-on-a-ladybug-sitting-on-an-aubrieta-flower-21967399/) | Companion planting post | 
| [Adobe Stock](https://stock.adobe.com/ie/images/grass-path-with-bench-and-perennials-in-the-vlinderhof-a-garden-designed-by-piet-oudolf/477594224) | Winter garden planning post |
| [Adobe Stock](https://stock.adobe.com/ie/images/garden-wheelbarrow-with-leaves-or-cleaning-city-park-in-spring-at-sunny-day/445546304) | Waking the garden post |
| [Adobe Stock](https://stock.adobe.com/ie/images/gardener-in-a-green-apron-cleaning-a-dirty-metal-spade-with-a-wooden-brush-hands-maintaining-gardening-tools-on-a-rustic-outdoor-table/1967485573) | Midwinter care post |
| [Freepik](https://www.magnific.com/free-photo/top-view-gardening-tools-flower-pot_13560868.htm#fromView=search&page=1&position=1&uuid=3be56098-870b-46a7-9dec-d12d9d0dbea2&query=seedlings) | Spring planting guide post |
| [Pexels](https://www.pexels.com/photo/green-potted-plants-inside-the-house-9707262/) | Winter Houseplants post |
| [Pexels](https://www.pexels.com/photo/lush-garden-in-mississauga-with-blooming-flowers-33402974/) | Contact page backdrop |
| [Adobe Stock](https://stock.adobe.com/ie/images/wooden-garden-gate-stands-invitingly-open-along-a-stone-pathway-leading-into-a-lush-green-paradise-illuminated-by-bright-sun-flare-filtering-through-large-trees/1918821068) | Login/Logout backdrop |
| [Adobe Stock](https://stock.adobe.com/ie/images/patio-garden-with-containers-full-of-colorful-flowers-container-gardening-and-flower-display-idea/517647406) | Signup backdrop |
| [Pexels](https://www.pexels.com/photo/abandoned-land-full-of-trees-and-green-grass-11573626/) | 404 backdrop |
| [Claude](https://claude.ai) | Blog post contents |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [ImageResizer](https://imageresizer.com/) | Resizing, compressing and converting images to `.webp` |
| Developer's Own Images | Apple tree, damaged brassica and pitcher plant |

### AI Use
I worked mainly with [claude.ai](https://claude.ai).

#### Planning
During the planning phase, AI served mainly as a sounding board — helping me stress-test the overall concept against the assessment criteria, identify gaps, and keep scope from drifting. It was also useful for time-consuming, repetitive tasks, such as running accessibility checks across the full colour palette.

Rather than generating content or making decisions for me, the most valuable thing the AI did at this stage was surface possibilities I hadn't considered, which I could then research and evaluate independently.
| ![screenshot](documentation/claude-planning.png) | ![screenshot](documentation/claude-colours.png) | ![screenshot](documentation/claude-user-mapping.png) |
| --- | --- | --- |

#### Troubleshooting and Explanations

During the build, I used AI primarily for debugging. I set a personal rule of working in "Socratic mode" — asking the AI to guide me with questions rather than provide direct solutions. This kept the learning intact while still moving things forward when I was stuck.
Many errors turned out to be simple syntax mistakes or typos, which the AI was quick to identify. The more valuable moments came when a Google search had drawn a blank and I needed to know what to search for, not just the answer itself — being pointed in the right direction made a significant difference.

| ![screenshot](documentation/claude-typo.png) | ![screenshot](documentation/sample-claude.png) |
| --- | --- |

#### Content Creation
For content that a client would typically supply in a real-world project, I used AI freely. In this case that meant the Digging Deeper blog posts and the sample forum posts, both generated as .json files. The initial blog content was too thin and was later improved by asking the AI to produce fuller, more professional versions. Getting clean output into Summernote required routing the text through a plain text editor first to strip formatting and hidden HTML.

| ![screenshot](documentation/claude-json.png) |
| --- | 

#### Testing
For automated testing, I provided the AI with the app's models, views, and forms and asked it to suggest a list of relevant tests. This gave me a structured starting point, which I then worked through systematically, prioritising authentication and CRUD functionality. As with troubleshooting, I found the Socratic approach most effective — being guided toward the right testing patterns rather than given ready-made code helped me understand and adapt the tests properly.

| ![screenshot](documentation/claude-test-suggestions.png) | ![screenshot](documentation/claude-test-help.png) |
| --- | --- |

### Acknowledgements

- I would like to thank [Tim Nelson](https://www.github.com/TravelTimN) for [Markdown Builder](https://markdown.2bn.dev).
- I would like to thank my mentor Tom Cowen for his time and advice. 
- I would like to thank the [Code Institute](https://codeinstitute.net) for the instruction provided to get me here.
- I would like to thank the [Code Institute Discord community](https://discord-portal.codeinstitute.net) and [Future Coders of The World](https://discord.gg/uFbJcW9rv) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my Code Institute facilitators Tindy Chan who helped me to come up with the idea and Marko Tot who encouraged me to keep going. 