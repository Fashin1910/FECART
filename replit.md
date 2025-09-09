# Criador de Mandalas

## Overview

Criador de Mandalas is a Flask-based web application that transforms user thoughts and feelings into beautiful mandala artwork. The application currently uses free public APIs (Quotable API for descriptions and Lorem Picsum for images) instead of Gemini AI, making it fully functional without requiring API keys. Users can input any thought or emotion in Portuguese, and the system will produce a unique mandala description and placeholder image, complete with downloadable images and shareable QR codes.

## User Preferences

Preferred communication style: Simple, everyday language.
Interface language: Portuguese (pt-br).

## System Architecture

**Web Framework**: Built using Flask, a lightweight Python web framework that handles routing, templating, and HTTP request processing. The application follows a simple MVC pattern with clear separation between routes (`app.py`), business logic (`gemini_service.py`), and presentation (HTML templates).

**API Integration**: The core functionality currently uses free public APIs: Quotable API for generating inspiring descriptions combined with user thoughts, and Lorem Picsum for generating placeholder mandala images. The system is designed to easily switch back to Gemini AI when API keys become available.

**Frontend Architecture**: Uses a modern web stack with Tailwind CSS for responsive design, glassmorphism effects, and colorful gradients. Features custom fonts (Cinzel for titles, Inter for body text), smooth animations, and vanilla JavaScript for dynamic interactions. The interface provides real-time feedback with loading states, error handling, and smooth animations. The colorful gradient background and glass-effect cards create a meditative aesthetic that complements the spiritual nature of mandala art.

**File Management**: Images are stored locally in the `static/images` directory with UUID-based filenames to prevent conflicts. The application includes automatic directory creation and serves generated images through Flask's static file serving.

**User Experience Flow**: The application follows a streamlined process: user input → AI description generation → AI image generation → result display with download and sharing options. Error handling is implemented at each stage to provide meaningful feedback to users.

## External Dependencies

**Free APIs**: 
- Quotable API (api.quotable.io) for generating inspiring quotes used in mandala descriptions
- Lorem Picsum (picsum.photos) for placeholder mandala images
- QR Code API (api.qrserver.com) for generating shareable QR codes

**Python Libraries**: 
- Flask for web framework functionality
- requests for HTTP API calls
- uuid for generating unique identifiers

**Frontend Libraries**: 
- Tailwind CSS (via CDN) for styling and responsive design
- Google Fonts (Cinzel and Inter) for typography
- Font Awesome for iconography
- Custom CSS and JavaScript for enhanced user experience and animations

**Environment Configuration**: Uses environment variables for sensitive configuration like session secrets, with fallback defaults for development environments.