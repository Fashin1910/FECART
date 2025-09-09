import os
import logging
import requests
import random

def create_mandala_description_from_thought(user_thought, quote, author):
    """Create a mandala description combining user thought and inspirational quote"""
    
    # Random color palettes for variety
    color_palettes = [
        "deep blues and golden yellows",
        "emerald greens and soft purples", 
        "warm oranges and peaceful whites",
        "rich burgundies and silver accents",
        "sunset reds and calming turquoise",
        "royal purples and gentle golds"
    ]
    
    # Random mandala elements
    elements = [
        "lotus petals radiating from the center",
        "intricate geometric patterns and sacred symbols",
        "flowing arabesque designs and celestial motifs",
        "delicate floral patterns and spiritual emblems",
        "crystalline structures and nature-inspired forms",
        "tribal patterns and cosmic representations"
    ]
    
    color_palette = random.choice(color_palettes)
    mandala_elements = random.choice(elements)
    
    description = f"""Inspired by your thought "{user_thought}" and the wisdom "{quote}" by {author}, envision a magnificent mandala blooming with {color_palette}. 

At its heart lies a perfect symmetrical design featuring {mandala_elements}, each detail reflecting the essence of your inner contemplation. The patterns flow outward in harmonious waves, creating a sacred space for meditation and self-reflection.

This mandala serves as a visual representation of your thoughts transformed into art, a bridge between the tangible and the spiritual, inviting you to find peace and clarity within its intricate beauty."""
    
    return description

def create_fallback_description(user_thought):
    """Create a fallback description when API calls fail"""
    
    descriptions = [
        f'A serene mandala emerges from your thought "{user_thought}", featuring concentric circles of wisdom and tranquility. Delicate patterns dance in harmony, creating a sacred geometry that speaks to the soul and invites peaceful contemplation.',
        
        f'Inspired by "{user_thought}", this mandala unfolds like a spiritual flower, with intricate petals of light and shadow. Each curve and line represents a moment of clarity, woven together in perfect symmetry.',
        
        f'Your reflection "{user_thought}" transforms into a luminous mandala, where ancient symbols and modern inspiration converge. The design radiates outward from a central point of pure consciousness, creating ripples of artistic beauty.',
        
        f'From the depths of "{user_thought}" springs forth a mandala of extraordinary detail. Geometric patterns intertwine with organic forms, creating a visual meditation that bridges the gap between mind and spirit.',
        
        f'This mandala, born from your contemplation "{user_thought}", presents itself as a kaleidoscope of inner wisdom. Symmetrical designs flow in perfect balance, each element carefully placed to inspire peace and introspection.'
    ]
    
    return random.choice(descriptions)

def generate_mandala_description(user_thought):
    """Generate an artistic mandala description using free APIs"""
    try:
        # Use Quotable API to get inspiring quotes and create a mandala description
        response = requests.get('https://api.quotable.io/random', timeout=10)
        
        if response.status_code == 200:
            quote_data = response.json()
            quote = quote_data.get('content', '')
            author = quote_data.get('author', 'Unknown')
            
            # Create a mandala description inspired by the user's thought and the quote
            description = create_mandala_description_from_thought(user_thought, quote, author)
            return description
        else:
            # Fallback to a generic description
            return create_fallback_description(user_thought)
            
    except Exception as e:
        logging.error(f"Error generating mandala description: {str(e)}")
        return create_fallback_description(user_thought)

def generate_mandala_image(description, image_path):
    """Generate a mandala image using Lorem Picsum (placeholder for now)"""
    try:
        # Use Lorem Picsum to generate a random image (512x512)
        # Add a seed based on description to get consistent results for same input
        seed = abs(hash(description)) % 1000
        image_url = f"https://picsum.photos/seed/{seed}/512/512"
        
        # Download the image
        response = requests.get(image_url, timeout=30)
        
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"Mandala image downloaded successfully to {image_path}")
            return True
        else:
            logging.error(f"Failed to download image: {response.status_code}")
            return False
        
    except Exception as e:
        logging.error(f"Error generating mandala image: {str(e)}")
        return False
