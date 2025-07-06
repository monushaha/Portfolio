# Personal Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, and JavaScript.

## Features

- Responsive design that works on all devices
- Smooth scrolling navigation
- Animated sections and elements
- Project showcase with hover effects
- Skills progress bars
- Contact form
- Social media links
- Modern and clean design

## Customization

### Personal Information
1. Open `index.html`
2. Replace "Your Name" with your actual name
3. Update the email, location, and other personal information
4. Add your social media links

### Profile Image
1. Add your profile image to the `images` folder
2. Name it `profile.jpg` or update the image path in `index.html`

### Projects
1. Add your project images to the `images` folder
2. Update the project information in `index.html`:
   - Project names
   - Descriptions
   - Links to live projects or repositories
   - Project images

### Skills
1. Update the skills section in `index.html` with your actual skills
2. Adjust the progress bar percentages to match your skill levels

### Colors
1. Open `style.css`
2. Modify the color variables in the `:root` section:
   ```css
   :root {
       --primary-color: #4a6bff;
       --secondary-color: #6c757d;
       --dark-color: #212529;
       --light-color: #f8f9fa;
   }
   ```

## Adding New Sections

To add a new section:
1. Add a new `<section>` element in `index.html`
2. Give it a unique `id`
3. Add a corresponding navigation link in the navbar
4. Style the section in `style.css`

## Contact Form

The contact form is currently set up to show a success message. To make it functional:
1. Set up a backend server
2. Update the form submission handling in `script.js`
3. Add your server endpoint to handle the form data

## Browser Support

The website is compatible with:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment

1. Choose a hosting provider (e.g., GitHub Pages, Netlify, Vercel)
2. Upload all files to your hosting provider
3. Make sure all file paths are correct
4. Test the website on different devices and browsers

## Contributing

Feel free to fork this project and customize it for your needs. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE). 