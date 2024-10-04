# Curls & Glow

###[Visit the deployed site here](https://curls-and-glow-079ed9c8815e.herokuapp.com/).

Welcome to Curls & Glow, your ultimate destination for personalized haircare services and styling expertise. Our platform connects clients with professional stylists, showcasing a variety of services tailored to enhance and celebrate your natural curls. Explore our user-friendly interface to book appointments, browse through our offerings, and engage with our community of curl enthusiasts. Whether you’re looking for advice, inspiration, or a new look, Curls & Glow has everything you need to embrace your unique beauty.
![banner-page](documentation/images/banner-page.png)

# User Experience

## User Stories

## New User
- **US08 - Create user registration page**
  - As a Site User, I can register an account so that I can access the system.


## Existing User
- **US07 - Implement login and logout system**
  - As a Site User, I can securely log in and out so that I can access personalized features.

- **US10 - Create booking list page**
  - As a Site User, I want to create appointments to book services so that I can schedule my desired services at a convenient time and manage my appointments effectively.

- **US09 - Implement Service Management Features**
  - As a Site Admin, I need the services page and admin panel to be visually appealing and functional so that users can view and book services, and I can manage these services effectively.

- **US13 - Create user profile page**
  - As a Site User, I can view and edit my personal information on the profile page so that my account details are up-to-date.

- **US16 - Add feedback system**
  - As a Site User, I can provide feedback on services I've used so that I can help improve the system and share my experience.

- **US17 - Create section to display stylists**(+ New User)
  - As a Site User, I can see a list of stylists with their biographies and photos so that I can choose a professional based on their profiles.

### Website Owner/Developer
- **US01 - Set up development environment**
  - As a developer, I can set up the development environment so that I can start the project without interruptions due to configuration issues.

- **US02 - Set up GitHub repository**
  - As a developer, I can set up a GitHub repository so that the source code is managed properly.

- **US03 - Create superuser model**
  - As a site admin, I can create a superuser account so that I have administrative access to manage the system.

- **US04 - Set up Django with basic models**
  - As a developer, I can establish the basic structure in Django so that the application has a solid foundation.

- **US05 - Implement responsive design with Bootstrap**
  - As a Site User, I can view a responsive website so that I have a seamless experience across devices.

- **US06 - Choose typography and color scheme**
  - As a Developer/Designer, I can define the typography and color scheme so that the site’s visual identity is consistent.

- **US11 - Manage Appointments**
  - As a Site Admin, I need to manage appointments by updating their status so that I can ensure the scheduling system operates smoothly.

- **US19 - Conduct final system testing**
  - As a Developer/QA, I can conduct final testing to ensure the system is free of critical errors so that it is reliable and functions as expected.

- **US20 - Create Comprehensive README Documentation**
  - As a Developer, I can create a detailed README file so that the system is well-documented, making it easier for future developers and users to understand, maintain, and use the system. 
- **US21 - Final fixes and adjustments**
  - As a Developer, I can fix and adjust final issues to ensure the quality of the application so that the system is ready for deployment.
- **US22 - Finalize Deployment to Production Environment on Heroku**
  - As a Developer, I can finalize the deployment of the system to the production environment on Heroku so that it is fully accessible to users and operates smoothly in a live setting.

- **US23 - Gather user feedback post-launch**
  - As a Developer, I can gather user feedback post-launch so that I can inform future updates and improvements.

## Additional Features
- **US18 - Add contact form to services page**
  - As a Site Admin, I want to have all messages saved in the admin interface for control, so that I can manage inquiries effectively.
  - As a Site Staff, I want to view, delete, update the status, and reply to messages through a dedicated interface, so that I can manage communications efficiently.
  - As a Site User, I want to fill out a form to leave a message about the service, so that my inquiries or comments are sent to the administration.

## Site Goals

- Provide a seamless and personalized haircare experience tailored to curly hair.
- Create an intuitive platform where users can easily book appointments with professional stylists.
- Foster a user-friendly environment with a clear, responsive design that ensures accessibility across devices.
- Offer detailed information about available services, stylists, and ongoing promotions to keep users engaged and informed.
- Encourage client feedback to continually improve the platform and services provided.
- Establish a secure, reliable platform with continuous monitoring to ensure smooth operations.
- Empower users to explore different haircare options and receive expert advice for their specific needs.
- Build a community where clients can share their experiences, discover new styles, and connect with stylists who specialize in curls.


# Scope

The project's scope is to create and maintain "Curls & Glow," an online platform dedicated to personalized haircare services and styling expertise. Curls & Glow will serve as a user-friendly and responsive space for individuals to book appointments, browse through services, and engage with a community of curl enthusiasts. Development will be assisted by following a number of EPIC stories which will focus on different aspects of the site. The platform will encompass the following key features:

## [EPIC - Initial Set Up](https://github.com/miriamdosantos/curls-and-glow/milestone/1)
- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval for user information and service details.
- An early deployment of the application will be carried out to confirm the initial setup's functionality and provide a basis for further development.

## [EPIC - Initial Design and Authentication System](https://github.com/miriamdosantos/curls-and-glow/milestone/2)
- A responsive user experience will be implemented, defining the visual identity of the site.
- The authentication system will be created, allowing users to register, log in, and manage their profiles.
- Key design components, such as navigation, layout, and branding elements, will be established.

## [EPIC - Scheduling System and Main Page Design](https://github.com/miriamdosantos/curls-and-glow/milestone/3)
- A scheduling system will be developed to enable users to book and manage appointments.
- The main page design will be enhanced with service listings, promotional sections, and user-friendly navigation.
- Service management features, such as booking confirmation and appointment reminders, will be included.

## [EPIC - Advanced Features and Finalization of Design](https://github.com/miriamdosantos/curls-and-glow/milestone/4)
- Advanced features will be added, such as user feedback and stylist profiles.
- A section to display stylists, including their biographies and photos, will be created to help users choose professionals based on their profiles.
- The design of the platform will be finalized to ensure a cohesive and visually appealing experience.

## [EPIC - Testing and Documentation](https://github.com/miriamdosantos/curls-and-glow/milestone/5)
- Final testing will be conducted to ensure the system functions without critical errors and is reliable for users.
- Comprehensive README documentation will be created, including details such as installation instructions, usage guides, and deployment information.
- Final fixes and adjustments will be applied based on test results, ensuring the quality of the application before deployment.

## [EPIC - Deployment and Monitoring](https://github.com/miriamdosantos/curls-and-glow/milestone/6)
- The system will be deployed to the production environment on Heroku, ensuring it is fully accessible to users.
- Secure configurations, such as environment variables and database connections, will be implemented.
- Monitoring and logging mechanisms will be set up to ensure smooth operation, and rollback procedures will be in place for any critical issues post-launch.
- User feedback post-launch will be gathered and analyzed to inform future improvements.

# Design

The primary design goal of *Curls and Glow* was to create a smooth and welcoming user experience focused on simplicity and ease of navigation. The platform was designed to cater to clients looking for curly haircare services while providing them with an intuitive and aesthetically pleasing interface.

A key objective of the design was to ensure users could easily access essential services, book appointments, and explore stylists' profiles without encountering unnecessary complexity. The homepage presents a clean, responsive layout, highlighting important sections such as services, stylists, and testimonials, while maintaining a balanced visual hierarchy.

## Focus on User-Centric Design

Was designed the platform to be user-centric, ensuring that users could navigate easily between the main services and their accounts, regardless of whether they were booking an appointment or browsing available haircare options. The emphasis was placed on minimal page transitions, allowing users to accomplish their tasks without excessive steps. This focus helped create a smooth, engaging user journey.

## Efficient Booking System

To streamline the booking process, the design includes simple but clear call-to-action buttons, allowing users to book appointments without difficulty. A significant aspect of this design involved the appointment confirmation modals, which are reusable and provide users with clear feedback before finalizing their actions.

## Comprehensive Profile and Service Pages

Profile and service pages were designed with user-friendliness in mind. Users can update their profiles, view their booking history, and explore services in one place, avoiding the need for additional navigation. The stylist profiles provide users with quick access to detailed information and visual examples of their work.

## Visual Consistency

To enhance the overall experience, the design emphasizes consistency in colors, typography, and layout. Colors that evoke warmth and trust were chosen, creating a professional yet inviting atmosphere. The use of images throughout the site, especially in sections like the service gallery and testimonials, further enhances the user experience by showcasing the salon’s work in a visually compelling way.

## Mobile Responsiveness

Ensuring that the platform works seamlessly across devices was a critical aspect of the design. All layouts and components were carefully crafted to adapt to various screen sizes, providing mobile users with the same high-quality experience as desktop users.

The design of *Curls and Glow* aimed to combine functionality with aesthetics, ensuring that users not only enjoyed their experience but also found it efficient and easy to navigate, regardless of the device they were using. This commitment to intuitive and responsive design helped solidify the platform as a go-to place for personalized curly haircare services.

## Logo Design and Colour Scheme

The website embraces a warm and inviting color scheme, designed to reflect the salon's focus on natural beauty and haircare. The palette consists of soft tones of browns and earthy shades, combined with elegant whites and neutral colors to convey a sense of relaxation and professionalism. This choice of colors creates an overall calming ambiance, making users feel welcomed and comfortable while navigating through the website.

## Color Palette

- **Primary Color (Rose Gold)**: 
  - **Hex:** `#b76e79`
  - **Usage**: Highlights in the logo, particularly for curls, establishing a luxurious identity.
  
- **Secondary Color (Dark Brown)**:
  - **Hex:** `#3e2a25`
  - **Usage**: Text elements like "Curls & Glow" and "Beauty Salon," as well as borders and outlines, reinforcing brand recognition.

- **Accent Colors**:
  - **Light Cream**: 
    - **Hex:** `#f7efe5`
    - **Usage**: Primary background color providing soft contrast.
  - **Warm Beige**:
    - **Hex:** `#e5d3c3`
    - **Usage**: Subtle highlights and secondary design elements.
  - **Soft Bronze**: 
    - **Hex:** `#c69c7b`
    - **Usage**: Decorative details like stars around the logo, adding elegance.
  - **White**: 
    - **Hex:** `#ffffff`
    - **Usage**: Text and critical UI elements for clarity on darker backgrounds.

### Design Aesthetic

This color scheme not only establishes a professional and luxurious look but also enhances user experience. The combination of rose gold with earthy tones like dark browns and creams offers a modern feel, aligning seamlessly with the *Curls & Glow* brand identity. 

Light shades combined with earthy accents guide user attention toward essential sections without overwhelming them, promoting a clean and polished interface. The elegant logo design, featuring these earthy tones, creates visual harmony and embodies the essence of *Curls and Glow*, reflecting its commitment to personalized and natural curly haircare.

These color combinations help reinforce the salon’s brand identity, providing users with a cozy, professional, and clean interface that encourages exploration. Light shades paired with earthy accents are used to highlight essential sections and direct attention without overwhelming the user.

The overall aesthetic is further enhanced by the simple, yet elegant, logo design, which incorporates these earthy tones, creating visual harmony throughout the platform. The logo embodies the essence of *Curls and Glow*, reflecting the brand's commitment to personalized and natural curly haircare.

## Fonts
The main fonts used in this project is Playfair Display SC and Poppins , which compliments the techical design of the website.

![database-schema](documentation/images/fonts.png)

# Database Schema
![database-schema](documentation/images/database-schema%20.png)

# Models
## Allauth User Model
The User model is a crucial component of Django Allauth, featuring standard fields for user authentication, including username, email, password, and more. This model is designed for managing user access and should not be altered directly. It works in tandem with the Profile model to handle user-specific data.

## UserProfile Model
The UserProfile model represents each user’s presence on the platform, capturing essential details such as their username, email, password, phone number, and membership status (whether they are staff, active, or a superuser).

## Service Model
The Service model defines the different services offered by the salon, including their titles, descriptions, prices, and durations.

## Stylish Model
The Stylish model represents the salon's stylists, detailing their names, bios, and photos. This helps clients learn more about the stylists available for their appointments.

## Availability Model
The Availability model outlines the days and times when each stylist is available for appointments, ensuring clients can book at convenient times.

## Stylish_Availability Model
The Stylish_Availability model serves as an intermediary table that links stylists to their availability. This is crucial for managing many-to-many relationships between stylists and the times they are available for appointments.

## Booking Model
The Booking model captures the details of customer appointments, linking user profiles, services, stylists, availability, and any applicable offers.

## Offer Model
The Offer model details promotional offers available to customers, including discount percentages and validity dates, which helps clients save on services.

## Testimonial Model
The Testimonial model records customer feedback associated with their bookings, capturing ratings and messages that provide insights into customer satisfaction.

## ContactMessage Model
The ContactMessage model allows users to send messages to the salon, capturing their names, emails, subjects, and messages to facilitate communication.

## Relationships Explained

- **Stylists and Availability**: Each stylist can have multiple available time slots. The Stylish_Availability table links stylists with their corresponding availability, ensuring clients can easily find when a stylist is free for an appointment.

- **Bookings**:The Booking model serves as a central point, connecting a user’s profile (UserProfile), the service they want, the stylist they choose, the availability they select, and any special offers available at the time. This relationship ensures that all necessary information for an appointment is captured in one place.

- **Testimonials**:Each testimonial is linked to a specific booking, providing valuable feedback on the stylist and service received. This relationship helps maintain a record of customer satisfaction for future reference.

- **Contact Messages**:The ContactMessage model connects user inquiries to their profiles, facilitating effective communication between the salon and its customers. This allows the salon to respond to inquiries with the relevant user context.

Using Inline Admin in Django enhances the organization of related data. For instance, when managing the `UserProfile` in the Django Admin, you can include inlines for `Bookings` and `ContactMessages`. This means that when you view a user's profile, you can also see all their bookings and messages directly on the same page.

## Benefits of Using Inline Admin
- **Improved Usability**: Inline forms allow administrators to edit related objects without navigating away from the parent object’s page. This streamlines the management process and saves time.
- **Enhanced Context**: Having bookings and messages associated directly with the user profile provides valuable context for administrators, making it easier to understand a user’s interactions with the salon.
- **Cohesive Data Management**: By consolidating information in one view, it reduces the need for cross-referencing different sections of the admin interface, leading to a more efficient workflow.

## Additional Notes
The Stylish_Availability table is automatically created by Django to handle the many-to-many relationship between stylists and their availability times. The UserProfile model is derived from the implementation of Django Allauth’s user model signals, emphasizing its importance in managing user-specific interactions and data.

# Wiframes

The project's pages and layouts were initially created using the Balsamiqi framework, focusing on the desktop version. The implementation took responsiveness into account, utilizing Bootstrap to adapt the design for mobile versions. This ensures a consistent user experience across different devices, allowing all interface elements to adjust fluidly to various screen widths.

<details>
<summary>➡️Home</summary>

![Imagem da Página 1](documentation/images/wiframes/home.png)

</details>




