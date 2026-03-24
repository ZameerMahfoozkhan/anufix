import json
import os

TEMPLATE_FILE = '_template.html'

with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template = f.read()

pages = [
    {
        "filename": "index.html",
        "title": "Anufix - Best Fabrication Work in Noida & Greater Noida",
        "description": "Iron, Steel & Aluminium Fabrication Services with Material & Labour. Fast, Reliable & Affordable.",
        "content_generator": "generate_home"
    },
    {
        "filename": "services.html",
        "title": "Our Fabrication Services | Anufix Noida",
        "description": "We provide all types of fabrication work including metal fabrication, gate & grill work, shed fabrication and welding services in Noida, Greater Noida.",
        "content_generator": "generate_services"
    },
    {
        "filename": "about.html",
        "title": "About Anufix | Trusted Fabrication Services",
        "description": "Learn about Anufix. We specialize in all types of iron, steel and aluminium fabrication work with material and labour.",
        "content_generator": "generate_about"
    },
    {
        "filename": "gallery.html",
        "title": "Our Recent Work | Anufix Gallery",
        "description": "View our successfully completed fabrication projects including gates, grills, sheds and staircase work in Noida & Greater Noida.",
        "content_generator": "generate_gallery"
    },
    {
        "filename": "contact.html",
        "title": "Contact Anufix | Request a Free Quote",
        "description": "Get in touch with Anufix for fast and reliable fabrication service in Noida & Greater Noida.",
        "content_generator": "generate_contact"
    },
    # Individual Services
    {
        "filename": "ms-fabrication.html",
        "title": "MS Fabrication Work in Noida & Greater Noida | Anufix",
        "description": "Mild Steel (MS) fabrication work for residential, commercial and industrial projects.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "MS Fabrication Work", "types": ["MS Gate Fabrication", "MS Structure Work", "MS Grill & Railing", "Custom MS Design"], "text": "We provide all types of Mild Steel (MS) fabrication work for residential, commercial and industrial projects. Strong, durable and affordable MS fabrication service available.", "img": "Metal Fabrication.png"}
    },
    {
        "filename": "ss-fabrication.html",
        "title": "Stainless Steel Fabrication in Noida | Anufix",
        "description": "High-quality stainless steel fabrication work for modern and long-lasting structures.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Stainless Steel Fabrication", "types": ["SS Railing", "SS Gate", "SS Design Work", "SS Furniture"], "text": "We provide high-quality stainless steel fabrication work for modern and long-lasting structures. Premium finish and rust-proof fabrication work.", "img": "Custom Fabrication Work.png"}
    },
    {
        "filename": "aluminium-fabrication.html",
        "title": "Aluminium Fabrication Work in Noida | Anufix",
        "description": "Lightweight and durable aluminium fabrication services for homes and offices.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Aluminium Fabrication Work", "types": ["Aluminium Doors & Windows", "Aluminium Partition", "Custom Aluminium Work"], "text": "We provide lightweight and durable aluminium fabrication services for homes and offices.", "img": "Custom Fabrication Work.png"}
    },
    {
        "filename": "gate-fabrication.html",
        "title": "Gate Fabrication in Noida & Greater Noida | Anufix",
        "description": "We design and install strong and stylish gates for residential and commercial use.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Gate Fabrication", "types": ["Main Gate", "Sliding Gate", "Designer Gate"], "text": "We design and install strong and stylish gates for residential and commercial use.", "img": "Gate & Grill Fabrication.png"}
    },
    {
        "filename": "grill-fabrication.html",
        "title": "Grill Fabrication in Noida | Anufix",
        "description": "We provide secure and durable grill fabrication services for windows and balconies.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Grill Fabrication", "types": ["Window Grill", "Balcony Grill", "Safety Grill"], "text": "We provide secure and durable grill fabrication services for windows and balconies.", "img": "Gate & Grill Fabrication.png"}
    },
    {
        "filename": "railing-work.html",
        "title": "Railing Fabrication in Noida | Anufix",
        "description": "We provide modern and strong railing work for stairs and balconies.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Railing Fabrication", "types": ["Stair Railing", "Balcony Railing", "Glass Railing"], "text": "We provide modern and strong railing work for stairs and balconies.", "img": "Staircase & Railing Work.png"}
    },
    {
        "filename": "staircase.html",
        "title": "Staircase Fabrication in Noida | Anufix",
        "description": "We design and install strong and modern staircase fabrication work.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Staircase Fabrication", "types": ["Metal Staircase", "Spiral Staircase", "Custom Stair Design"], "text": "We design and install strong and modern staircase fabrication work.", "img": "Staircase & Railing Work.png"}
    },
    {
        "filename": "shed-fabrication.html",
        "title": "Shed Fabrication in Greater Noida | Anufix",
        "description": "We provide industrial shed and warehouse fabrication services.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Shed Fabrication", "types": ["Industrial Shed", "Factory Shed", "Roof Structure"], "text": "We provide industrial shed and warehouse fabrication services.", "img": "Industrial Shed Fabrication.png"}
    },
    {
        "filename": "welding-work.html",
        "title": "Welding Work in Noida | Anufix",
        "description": "We provide all types of welding services including repair and installation.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Welding Work", "types": ["Gate Welding", "Grill Repair", "Structure Welding"], "text": "We provide all types of welding services including repair and installation.", "img": "Welding & Repair Work.png"}
    },
    {
        "filename": "repair-maintenance.html",
        "title": "Fabrication Repair Services in Noida | Anufix",
        "description": "We provide repair and maintenance services for all types of fabrication work.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Fabrication Repair Services", "types": ["Gate Repair", "Grill Repair", "Structure Maintenance"], "text": "We provide repair and maintenance services for all types of fabrication work.", "img": "Welding & Repair Work.png"}
    },
    {
        "filename": "custom-fabrication.html",
        "title": "Custom Fabrication Work in Noida | Anufix",
        "description": "We provide customized fabrication work as per customer requirements.",
        "content_generator": "generate_service_detail",
        "extra": {"name": "Custom Fabrication Work", "types": ["Metal Furniture", "Storage Racks", "Cabinets"], "text": "We provide customized fabrication work as per customer requirements.", "img": "Custom Fabrication Work.png"}
    },
    # Legal Pages
    {
        "filename": "privacy-policy.html",
        "title": "Privacy Policy | Anufix",
        "description": "Privacy Policy for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Privacy Policy", "text": "<h3>Introduction</h3><p>Welcome to Anufix.com. We respect your privacy and are committed to protecting your personal information. This Privacy Policy explains how we collect, use and safeguard your data when you visit our website or contact us for services.</p><h3>Information We Collect</h3><p>We may collect the following information:</p><ul><li>Name</li><li>Phone Number</li><li>Location</li><li>Service Requirements</li></ul><p>This information is collected only when you contact us through call, WhatsApp or contact form.</p><h3>How We Use Your Information</h3><p>We use your information for the following purposes:</p><ul><li>To provide fabrication services</li><li>To contact you regarding your service request</li><li>To improve our services and customer experience</li></ul><h3>Data Protection</h3><p>We take appropriate measures to protect your personal information. Your data is kept secure and is not misused.</p><h3>Sharing of Information</h3><p>We do not sell, trade or share your personal information with any third party.</p><h3>Your Consent</h3><p>By using our website, you consent to our Privacy Policy.</p>"}
    },
    {
        "filename": "terms.html",
        "title": "Terms & Conditions | Anufix",
        "description": "Terms & Conditions for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Terms & Conditions", "text": "<h3>Services</h3><p>Anufix provides fabrication services including metal fabrication, gate & grill work, shed fabrication, welding and repair services in Noida, Greater Noida and nearby areas. All services are provided based on customer requirements and project specifications.</p><h3>Pricing & Payment</h3><ul><li>Service charges depend on the type of work, material and project size</li><li>Inspection or visit charges may apply</li><li>Advance payment may be required before starting the work</li><li>Final payment must be completed after service delivery</li></ul><h3>Work Timeline</h3><ul><li>Project completion time depends on the type and size of work</li><li>Delays may occur due to weather, material availability or site conditions</li></ul><h3>Customer Responsibility</h3><ul><li>Customer must provide correct details and site access</li><li>Any changes in work after confirmation may affect cost and timeline</li></ul><h3>Cancellation Policy</h3><ul><li>Orders once confirmed may not be cancelled without prior notice</li><li>Any advance payment may be non-refundable depending on work progress</li></ul><h3>Liability</h3><p>We are not responsible for any damage caused due to pre-existing site conditions. We ensure proper work quality but do not provide warranty unless agreed.</p>"}
    },
    {
        "filename": "disclaimer.html",
        "title": "Disclaimer | Anufix",
        "description": "Disclaimer for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Disclaimer", "text": "<h3>General Information</h3><p>The information provided on Anufix.com is for general informational purposes only. While we strive to keep the information accurate and up to date, we make no guarantees of any kind regarding the completeness, reliability or accuracy of the information.</p><h3>Independent Service Provider</h3><p>Anufix is an independent fabrication service provider. We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with any brand, company or organization.</p><h3>Service Responsibility</h3><p>All services provided by Anufix are based on customer requirements and site conditions. We are not responsible for any issues arising due to incorrect information provided by the customer or pre-existing site conditions.</p><h3>No Professional Warranty</h3><p>We aim to provide quality fabrication services, but we do not offer any official warranty or guarantee unless explicitly agreed upon in writing.</p><h3>Limitation of Liability</h3><p>Under no circumstances shall Anufix be liable for any loss or damage arising from the use of our website or services.</p>"}
    },
    {
        "filename": "refund-policy.html",
        "title": "Refund Policy | Anufix",
        "description": "Refund Policy for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Refund Policy", "text": "<h3>Advance Payment</h3><ul><li>Advance payment may be required before starting any fabrication work</li><li>Advance amount is used for material purchase and initial work setup</li></ul><h3>Refund Eligibility</h3><ul><li>Refunds are only applicable if the work has not been started</li><li>If the customer cancels the service before work begins, partial refund may be considered after deducting any incurred costs</li></ul><h3>Non-Refundable Cases</h3><ul><li>Once the work has started, advance payment is non-refundable</li><li>No refund will be provided after completion of the work</li><li>Customized fabrication work is non-refundable</li></ul><h3>Service Issues</h3><p>If there is any issue with the service, customers can contact us for resolution. We will make reasonable efforts to fix or adjust the work if required.</p><h3>Payment Disputes</h3><p>Any disputes regarding payment must be reported within 24 hours of service completion.</p>"}
    }
]

def generate_home(page):
    return """
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Best <span>Fabrication Work</span> in Noida & Greater Noida</h1>
            <p>Iron, Steel & Aluminium Fabrication Services with Material & Labour<br>Fast, Reliable & Affordable</p>
            <div class="hero-btns animate-on-scroll">
                <a href="tel:9560208785" class="btn"><i class="fas fa-phone-alt"></i> Call Now: 9560208785</a>
                <a href="services.html" class="btn btn-outline">Explore Services</a>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="section">
        <div class="container animate-on-scroll">
            <h2 class="section-title">Why Choose Anufix</h2>
            <p class="section-subtitle">We deliver high-quality, strong and long-lasting fabrication work.</p>
            
            <div class="feature-list">
                <div class="feature-item">
                    <i class="fas fa-hammer feature-icon"></i>
                    <h4>Experienced Fabrication Team</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-shield-alt feature-icon"></i>
                    <h4>High Quality Material</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-weight-hanging feature-icon"></i>
                    <h4>Strong & Durable Work</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-tags feature-icon"></i>
                    <h4>Affordable Pricing</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-clock feature-icon"></i>
                    <h4>On-Time Completion</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-map-marker-alt feature-icon"></i>
                    <h4>Service in Noida & NCR</h4>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Overview -->
    <section class="section" style="background: var(--white);">
        <div class="container">
            <h2 class="section-title">Our Services</h2>
            <p class="section-subtitle">We provide all types of fabrication work for residential, commercial and industrial needs.</p>
            
            <div class="grid-3">
                <div class="service-card animate-on-scroll">
                    <div class="service-img">
                        <img loading="lazy" src="img/Metal Fabrication.png" alt="Metal Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Metal Fabrication</h3>
                        <p>MS, SS, and Aluminium fabrication work including cutting, bending and welding.</p>
                        <a href="ms-fabrication.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                
                <div class="service-card animate-on-scroll">
                    <div class="service-img">
                        <img loading="lazy" src="img/Gate & Grill Fabrication.png" alt="Gate & Grill Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Gate & Grill Fabrication</h3>
                        <p>Design and installation of strong iron gates, window grills, and security structures.</p>
                        <a href="gate-fabrication.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                
                <div class="service-card animate-on-scroll">
                    <div class="service-img">
                        <img loading="lazy" src="img/Industrial Shed Fabrication.png" alt="Industrial Shed">
                    </div>
                    <div class="service-content">
                        <h3>Industrial Shed Fabrication</h3>
                        <p>High-quality steel material sheds and warehouse structures for industrial needs.</p>
                        <a href="shed-fabrication.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
            <div style="text-align:center; margin-top: 40px;">
                <a href="services.html" class="btn btn-outline">View All Services</a>
            </div>
        </div>
    </section>
    
    <!-- About Mini Section -->
    <section class="section">
        <div class="container animate-on-scroll">
            <div class="contact-wrapper" style="align-items: center;">
                <div style="padding: 40px;">
                    <h2 class="section-title" style="left:0; transform:none; text-align:left;">About Anufix</h2>
                    <p style="margin-top:20px;">Anufix is a professional fabrication service provider offering all types of iron, steel and aluminium work. We provide complete fabrication solutions with material and labour.</p>
                    <p>Our goal is to deliver high-quality, strong and long-lasting fabrication work for homes, shops and industrial projects.</p>
                    <a href="about.html" class="btn" style="margin-top:20px;">Read More About Us</a>
                </div>
                <div class="service-img" style="height:100%;">
                    <img loading="lazy" src="img/Custom Fabrication Work.png" alt="Fabrication Works">
                </div>
            </div>
        </div>
    </section>
    """

def generate_services(page):
    return """
    <section class="page-header">
        <div class="container">
            <h1>Fabrication Services in Noida & Greater Noida</h1>
            <p>We provide all types of fabrication work including metal fabrication, gate & grill work, shed fabrication and welding services.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="grid-3 animate-on-scroll">
                
                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Metal Fabrication.png" alt="MS Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>MS Fabrication</h3>
                        <p>Cutting, bending and welding of Mild Steel for homes and industrial use.</p>
                        <a href="ms-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Custom Fabrication Work.png" alt="SS Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>SS Fabrication</h3>
                        <p>High quality stainless steel railings, gates and furniture.</p>
                        <a href="ss-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Gate & Grill Fabrication.png" alt="Aluminium Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Aluminium Fabrication</h3>
                        <p>Lightweight and durable aluminium doors, windows and partitions.</p>
                        <a href="aluminium-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Gate & Grill Fabrication.png" alt="Gate Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Gate Fabrication</h3>
                        <p>Design and install strong designer gates, main and sliding gates.</p>
                        <a href="gate-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Gate & Grill Fabrication.png" alt="Grill Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Grill Fabrication</h3>
                        <p>Window grills, balcony grills and safety grills fabrication services.</p>
                        <a href="grill-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Staircase & Railing Work.png" alt="Staircase Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Staircase Fabrication</h3>
                        <p>Modem staircase, spiral staircases and custom metal stairs.</p>
                        <a href="staircase.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                
                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Staircase & Railing Work.png" alt="Railing Work">
                    </div>
                    <div class="service-content">
                        <h3>Railing Work</h3>
                        <p>Stair railings, balcony railings, and glass railing installation.</p>
                        <a href="railing-work.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Industrial Shed Fabrication.png" alt="Shed Fabrication">
                    </div>
                    <div class="service-content">
                        <h3>Industrial Shed Fabrication</h3>
                        <p>Industrial sheds, warehouse roofs, and factory structures.</p>
                        <a href="shed-fabrication.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-img">
                        <img loading="lazy" src="img/Welding & Repair Work.png" alt="Welding & Repair">
                    </div>
                    <div class="service-content">
                        <h3>Welding & Repair Work</h3>
                        <p>All types of welding and repair maintenance for existing structures.</p>
                        <a href="welding-work.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>

            </div>
        </div>
    </section>
    """

def generate_about(page):
    return """
    <section class="page-header">
        <div class="container">
            <h1>About Anufix</h1>
            <p>Your Trusted Fabrication Service Provider in Noida & Greater Noida.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container animate-on-scroll">
            <div class="contact-wrapper" style="align-items: center; background:transparent; box-shadow:none;">
                <div class="service-img" style="height: 400px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1)">
                    <img loading="lazy" src="img/Metal Fabrication.png" alt="About Anufix">
                </div>
                <div>
                    <h2>Who We Are</h2>
                    <p>Anufix is a trusted fabrication service provider in Noida & Greater Noida. We specialize in all types of iron, steel and aluminium fabrication work with material and labour.</p>
                    <p>We are committed to delivering high-quality work, strong structures and long-lasting solutions for residential, commercial and industrial projects.</p>
                    
                    <h3 style="margin-top:30px; font-size:1.4rem;">Our Core Focus</h3>
                    <ul style="list-style:disc; margin-left:20px; color:var(--text-light); margin-bottom: 20px;">
                        <li>Customer Satisfaction</li>
                        <li>Timely Work Completion</li>
                        <li>High-Quality Materials</li>
                        <li>Affordable Pricing</li>
                    </ul>
                    <a href="contact.html" class="btn">Get a Quote Today</a>
                </div>
            </div>
        </div>
    </section>
    """

def generate_gallery(page):
    return """
    <section class="page-header">
        <div class="container">
            <h1>Our Recent Work</h1>
            <p>We have successfully completed various fabrication projects including gates, grills, sheds and staircase work in Noida & Greater Noida.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="grid-3 animate-on-scroll">
                <div class="service-card"><img loading="lazy" src="img/Metal Fabrication.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
                <div class="service-card"><img loading="lazy" src="img/Gate & Grill Fabrication.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
                <div class="service-card"><img loading="lazy" src="img/Industrial Shed Fabrication.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
                <div class="service-card"><img loading="lazy" src="img/Staircase & Railing Work.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
                <div class="service-card"><img loading="lazy" src="img/Welding & Repair Work.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
                <div class="service-card"><img loading="lazy" src="img/Custom Fabrication Work.png" style="width:100%;height:100%;object-fit:cover; border-radius:8px; box-shadow:0 5px 15px rgba(0,0,0,0.1);"></div>
            </div>
            
            <div style="text-align:center; margin-top:50px;">
                <p style="font-size:1.2rem; color:var(--dark);">Need similar work done for your place?</p>
                <a href="contact.html" class="btn" style="margin-top:10px;">Contact Us Now</a>
            </div>
        </div>
    </section>
    """

def generate_contact(page):
    return """
    <section class="page-header">
        <div class="container">
            <h1>Contact Anufix</h1>
            <p>Looking for fabrication work in Noida & Greater Noida? Contact us today for fast and reliable service.</p>
        </div>
    </section>

    <section class="section">
        <div class="container animate-on-scroll">
            <div class="contact-wrapper">
                <div class="contact-info">
                    <h3>Get In Touch</h3>
                    <p style="color:#ddd; margin-bottom: 40px;">We provide on-site fabrication services at your location. Please call or WhatsApp before visiting.</p>
                    
                    <div class="info-item">
                        <div class="info-icon"><i class="fas fa-phone-alt"></i></div>
                        <div class="info-text">
                            <h4>Call Us</h4>
                            <p>9560208785</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon"><i class="fab fa-whatsapp"></i></div>
                        <div class="info-text">
                            <h4>WhatsApp</h4>
                            <p>Available for instant support</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon"><i class="fas fa-map-marker-alt"></i></div>
                        <div class="info-text">
                            <h4>Service Location</h4>
                            <p>Noida, Greater Noida, Noida Extension & Nearby Areas</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon"><i class="fas fa-clock"></i></div>
                        <div class="info-text">
                            <h4>Working Hours</h4>
                            <p>Monday to Sunday: 8:00 AM – 8:00 PM</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3 style="font-size: 1.8rem; margin-bottom: 25px;">Get a Free Quote</h3>
                    <form id="quoteForm">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="service">Service Required</label>
                            <select id="service" class="form-control" required>
                                <option value="" disabled selected>Select a Service</option>
                                <option value="Metal Fabrication">Metal Fabrication</option>
                                <option value="Gate & Grill">Gate & Grill Work</option>
                                <option value="Shed Fabrication">Shed Fabrication</option>
                                <option value="Staircase & Railing">Staircase & Railing</option>
                                <option value="Welding & Repair">Welding & Repair</option>
                                <option value="Custom Fabrication">Custom Fabrication</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="location">Location</label>
                            <input type="text" id="location" class="form-control" required>
                        </div>
                        <button type="submit" class="btn" style="width: 100%;">Submit Request</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    """

def generate_service_detail(page):
    extra = page.get("extra", {})
    name = extra.get("name", "Service")
    text = extra.get("text", "")
    types = extra.get("types", [])
    img_src = f"img/{extra.get('img', 'Custom Fabrication Work.png')}"
    
    types_html = "".join([f"<li><i class='fas fa-check-circle' style='color:var(--primary); margin-right:10px;'></i>{t}</li>" for t in types])
    
    return f"""
    <section class="page-header">
        <div class="container">
            <h1>{name}</h1>
            <p>{page['description']}</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container animate-on-scroll">
            <div class="contact-wrapper" style="align-items: center; background:transparent; box-shadow:none;">
                <div class="service-img" style="height: 400px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1)">
                    <img loading="lazy" src="{img_src}" alt="{name}">
                </div>
                <div class="content-block">
                    <h2>About This Service</h2>
                    <p>{text}</p>
                    
                    <h3 style="margin-top:25px; margin-bottom:15px; font-size:1.3rem;">What We Included:</h3>
                    <ul style="list-style:none; margin-left:0;">
                        {types_html}
                    </ul>
                    
                    <div style="margin-top:30px;">
                        <a href="contact.html" class="btn">Get a Quote for this Service</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_legal(page):
    extra = page.get("extra", {})
    name = extra.get("name", "Legal")
    text = extra.get("text", "")
    
    return f"""
    <section class="page-header">
        <div class="container">
            <h1>{name}</h1>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="content-block animate-on-scroll">
                {text}
                
                <hr style="margin: 40px 0; border:0; border-top:1px solid var(--border);">
                <h3>Contact Information</h3>
                <p>If you have any questions, you can contact us:</p>
                <ul>
                    <li>Phone: 9560208785</li>
                    <li>Location: Noida & Greater Noida</li>
                </ul>
            </div>
        </div>
    </section>
    """

if __name__ == "__main__":
    for page in pages:
        gen_func = globals().get(page["content_generator"])
        if gen_func:
            content = gen_func(page)
            output = template.replace('{{title}}', page['title'])\
                             .replace('{{description}}', page['description'])\
                             .replace('{{content}}', content)
            
            output_path = page['filename']
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Generated {output_path}")
        else:
            print(f"Error: Generator function {page['content_generator']} not found!")
