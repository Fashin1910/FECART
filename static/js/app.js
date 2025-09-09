class MandalaCreator {
    constructor() {
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        this.form = document.getElementById('mandalaForm');
        this.thoughtInput = document.getElementById('thoughtInput');
        this.generateBtn = document.getElementById('generateBtn');
        this.loadingSpinner = document.querySelector('.loading-spinner');
        this.btnText = document.querySelector('.btn-text');
        this.errorAlert = document.getElementById('errorAlert');
        this.errorMessage = document.getElementById('errorMessage');
        this.mandalaResult = document.getElementById('mandalaResult');
        this.mandalaDescription = document.getElementById('mandalaDescription');
        this.mandalaImage = document.getElementById('mandalaImage');
        this.qrCode = document.getElementById('qrCode');
        this.downloadLink = document.getElementById('downloadLink');
        this.createAnotherBtn = document.getElementById('createAnotherBtn');
    }

    bindEvents() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.createAnotherBtn.addEventListener('click', () => this.resetForm());
        this.thoughtInput.addEventListener('input', () => this.hideError());
    }

    async handleSubmit(event) {
        event.preventDefault();
        
        const thought = this.thoughtInput.value.trim();
        if (!thought) {
            this.showError('Por favor, digite um pensamento ou ideia para criar sua mandala.');
            return;
        }

        this.setLoading(true);
        this.hideError();
        this.hideMandalaResult();

        try {
            const response = await fetch('/generate_mandala', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ thought: thought })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Falha ao gerar a mandala');
            }

            this.displayMandala(data);
            
        } catch (error) {
            console.error('Error:', error);
            this.showError(error.message || 'Ocorreu um erro inesperado. Tente novamente.');
        } finally {
            this.setLoading(false);
        }
    }

    displayMandala(data) {
        // Set description
        this.mandalaDescription.textContent = data.description;
        
        // Set image
        this.mandalaImage.src = data.image_url;
        this.mandalaImage.alt = 'Mandala Gerada baseada no seu pensamento';
        
        // Set download link
        this.downloadLink.href = data.image_url;
        this.downloadLink.download = `mandala_${Date.now()}.png`;
        
        // Set QR code if available
        if (data.qr_code) {
            this.qrCode.src = data.qr_code;
            this.qrCode.style.display = 'block';
        } else {
            this.qrCode.style.display = 'none';
        }
        
        // Show results with animation
        this.showMandalaResult();
        
        // Scroll to results
        setTimeout(() => {
            this.mandalaResult.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
        }, 100);
    }

    setLoading(isLoading) {
        if (isLoading) {
            this.generateBtn.disabled = true;
            this.loadingSpinner.classList.add('show');
            this.btnText.innerHTML = '<i class="fas fa-magic mr-2"></i>Criando Sua Mandala...';
        } else {
            this.generateBtn.disabled = false;
            this.loadingSpinner.classList.remove('show');
            this.btnText.innerHTML = '<i class="fas fa-magic mr-2"></i>Criar Minha Mandala';
        }
    }

    showError(message) {
        this.errorMessage.textContent = message;
        this.errorAlert.classList.remove('hidden');
        this.errorAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    hideError() {
        this.errorAlert.classList.add('hidden');
    }

    showMandalaResult() {
        this.mandalaResult.classList.add('show');
    }

    hideMandalaResult() {
        this.mandalaResult.classList.remove('show');
    }

    resetForm() {
        this.thoughtInput.value = '';
        this.hideMandalaResult();
        this.hideError();
        this.thoughtInput.focus();
        
        // Scroll back to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new MandalaCreator();
});

// Add some visual feedback for better UX
document.addEventListener('DOMContentLoaded', () => {
    // Add focus effects to textarea
    const thoughtInput = document.getElementById('thoughtInput');
    
    thoughtInput.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    thoughtInput.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});
