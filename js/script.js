document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuBtn = document.querySelector('.menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = menuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                navLinks.classList.remove('active');
                if (menuBtn) {
                    menuBtn.querySelector('i').classList.remove('fa-times');
                    menuBtn.querySelector('i').classList.add('fa-bars');
                }
                
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('scrolled');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Form Submission Details
    const contactForm = document.getElementById('quoteForm');
    if(contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            const service = document.getElementById('service').value;
            const location = document.getElementById('location').value;

            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Redirecting...';
            btn.disabled = true;

            // Format WhatsApp message
            const message = `*New Quote Request from Anufix*%0A` +
                            `--------------------------%0A` +
                            `*Name:* ${name}%0A` +
                            `*Phone:* ${phone}%0A` +
                            `*Service:* ${service}%0A` +
                            `*Location:* ${location}`;

            const whatsappUrl = `https://wa.me/919560208785?text=${message}`;

            // Redirect to WhatsApp
            setTimeout(() => {
                window.location.href = whatsappUrl;
                btn.innerHTML = originalText;
                btn.disabled = false;
                contactForm.reset();
            }, 800);
        });
    }

    // Active link highlighting
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
    // Popup Logic
    const popup = document.getElementById('quotePopup');
    const closePopupBtn = document.querySelector('.popup-close');
    
    if (popup && closePopupBtn) {
        // Show popup after 5 seconds if not seen before in this session
        if (!sessionStorage.getItem('popupShown')) {
            setTimeout(() => {
                popup.classList.add('show');
                sessionStorage.setItem('popupShown', 'true');
            }, 5000);
        }

        closePopupBtn.addEventListener('click', () => {
            popup.classList.remove('show');
        });

        // Close when clicking outside content
        popup.addEventListener('click', (e) => {
            if (e.target === popup) {
                popup.classList.remove('show');
            }
        });
    }

    // Popup Form Submission
    const quoteFormPopup = document.getElementById('quoteFormPopup');
    if(quoteFormPopup) {
        quoteFormPopup.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('namePopup').value;
            const phone = document.getElementById('phonePopup').value;
            const service = document.getElementById('servicePopup').value;
            const location = document.getElementById('locationPopup').value;

            const btn = quoteFormPopup.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Redirecting...';
            btn.disabled = true;

            const message = `*New Quote Request from Anufix (Popup)*%0A` +
                            `--------------------------%0A` +
                            `*Name:* ${name}%0A` +
                            `*Phone:* ${phone}%0A` +
                            `*Service:* ${service}%0A` +
                            `*Location:* ${location}`;

            const whatsappUrl = `https://wa.me/919560208785?text=${message}`;

            setTimeout(() => {
                window.location.href = whatsappUrl;
                btn.innerHTML = originalText;
                btn.disabled = false;
                popup.classList.remove('show');
                quoteFormPopup.reset();
            }, 800);
        });
    }
});
