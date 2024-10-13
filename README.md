# Chatbot-with-Azure
Chatbot capable of providing support on Makers Tech products and recommendations

### Explanation of Resources
1. **Knowldge base** The collection of questions and answers for use in our chatbot has been uploaded. Although this document was just the foundation, it was further optimized within the Azure AI Language tools, where prompts were added for each question, in addition to customizing greetings, farewells, and recommendations


### Additional notes
- In the code to implement the bot created in Azure, the secret key of the bot service was used to integrate it into our website. This is not recommended in production environments due to the vulnerabilities it may present, but in this case, it was left this way for development purposes.




# Makers Tech Chatbot Interface

## Overview
**Makers Tech Chatbot Interface** is a dual interface for an e-commerce chatbot designed to assist users with inquiries about products available at Makers Tech, including inventory, features, and pricing. The chatbot is integrated into the left side of the interface, while the right side displays additional information based on user interaction. The design aims to offer a visually appealing and user-friendly experience, providing real-time answers to customer queries.

## Features
1. **Chat Interface**: The left side of the screen is dedicated to the chatbot, which interacts with users and provides answers about product availability, features, and pricing. The chatbot is embedded using the Microsoft Bot Framework.

2. **Content Display Area**: The right side of the screen displays additional information. Users can choose between viewing product details (e.g., laptops) and company metrics by clicking on buttons provided.

3. **Carousel for Laptops**: When the user selects "Laptops", a carousel displays different laptop models, along with images and features. The carousel is styled to make navigation easy and visually appealing.

4. **Back Button**: A "Back" button is available to return to the main menu after selecting a category, such as laptops or metrics.

## Technologies Used
1. **HTML & CSS**: The layout and styling of the interface are implemented using HTML and CSS. CSS provides a modern, gradient background and an elegant Apple-like appearance with smooth transitions for buttons and elements.

2. **JavaScript**: JavaScript is used to provide interactivity for the interface, including:
   - Embedding the chatbot iframe.
   - Handling button clicks to change content dynamically in the right-side panel.
   - Implementing a carousel for displaying laptops with scroll-snap features for a smooth user experience.

3. **Microsoft Bot Framework**: The chatbot itself is embedded using an iframe that integrates a bot from Microsoft Bot Framework.

## Database Challenges
Initially, we intended to use a MySQL database for user management, but we faced some issues configuring MySQL on the local laptop. Due to these challenges, we explored using CSV files for data storage as a temporary alternative, though this approach was not fully implemented in the final version.

### Note
The chatbot iframe relies on an active internet connection to communicate with the Microsoft Bot Framework. Ensure you have an internet connection to fully use the chatbot feature.

## Future Improvements
- **Database Integration**: We plan to resolve the MySQL issues and implement a fully functional database for better data management and user handling.
- **CSV Backup**: Although CSV was considered for simplicity, a proper database would allow for scalability and easier data operations in the future.
- **Admin Dashboard**: Introduce an admin panel to manage inventory and monitor user interactions in real time.

## Acknowledgments
This project was created to enhance the customer support experience for Makers Tech by providing an intuitive and visually appealing dual-interface chatbot that combines AI-driven interactions with easy access to product information.

