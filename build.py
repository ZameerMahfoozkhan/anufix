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
        "extra": {"name": "Privacy Policy", "text": "<p>At ANUFIX, we respect your privacy and are committed to protecting your personal information.</p><h3>Information We Collect</h3><p>We may collect basic details such as your name, phone number, and address when you contact us or request a service.</p><h3>How We Use Information</h3><p>The information collected is used only to:</p><ul><li>Provide fabrication services</li><li>Contact you regarding your request</li><li>Improve our services</li></ul><h3>Information Sharing</h3><p>We do not sell, trade, or share your personal information with any third parties.</p><h3>Data Security</h3><p>We take appropriate measures to keep your information safe and secure.</p><h3>Cookies</h3><p>Our website may use cookies to improve user experience.</p><h3>Third-Party Services</h3><p>We may use tools like Google Ads or analytics to improve our services, but your personal data is not misused.</p><h3>Contact Us</h3><p>If you have any questions regarding this privacy policy, you can contact us:</p><p>ANUFIX<br>Sector 22, Noida, Uttar Pradesh<br>Phone: 9560208785</p><p>By using our website, you agree to this privacy policy.</p>"}
    },
    {
        "filename": "terms.html",
        "title": "Terms & Conditions | Anufix",
        "description": "Terms & Conditions for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Terms & Conditions", "text": "<p>Welcome to ANUFIX. By using our website and services, you agree to the following terms and conditions.</p><h3>Services</h3><p>ANUFIX provides metal fabrication services including gates, grills, railings, and custom fabrication work. All services are subject to availability and project requirements.</p><h3>Pricing</h3><p>All prices are based on material, design, and work scope. Final cost may vary after site inspection or discussion.</p><h3>Booking & Payment</h3><p>Advance payment may be required to confirm your order. Remaining payment must be completed after work completion.</p><h3>Work Timeline</h3><p>Project timelines are estimated and may vary depending on design complexity, material availability, and site conditions.</p><h3>Customer Responsibility</h3><p>Customers must provide accurate details and proper site access for smooth work execution.</p><h3>Cancellation</h3><p>Orders once confirmed may not be cancelled. Any cancellation request will be considered on a case-by-case basis.</p><h3>Liability</h3><p>ANUFIX is not responsible for any indirect or unforeseen damages during or after service completion.</p><h3>Changes to Terms</h3><p>We may update these terms at any time without prior notice.</p><h3>Contact Us</h3><p>ANUFIX<br>Sector 22, Noida, Uttar Pradesh<br>Phone: 9560208785</p><p>By using our services, you agree to these terms and conditions.</p>"}
    },
    {
        "filename": "disclaimer.html",
        "title": "Disclaimer | Anufix",
        "description": "Disclaimer for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Disclaimer", "text": "<p>The information provided on this website is for general information purposes only. ANUFIX makes every effort to ensure that the information is accurate and up to date, but we do not guarantee completeness or accuracy.</p><h3>Service Disclaimer</h3><p>All fabrication services (gates, grills, railings, and custom work) are subject to site conditions, material availability, and design requirements. Final results may vary based on project specifications.</p><h3>Pricing Disclaimer</h3><p>Prices mentioned on the website are indicative and may change after site inspection or discussion.</p><h3>Third-Party Disclaimer</h3><p>Our website may use third-party services such as Google Ads or analytics. We are not responsible for the content or policies of these external platforms.</p><h3>Liability</h3><p>ANUFIX shall not be held liable for any direct or indirect damages arising from the use of our website or services.</p><h3>Consent</h3><p>By using our website, you agree to this disclaimer.</p><h3>Contact Us</h3><p>ANUFIX<br>Sector 22, Noida, Uttar Pradesh<br>Phone: 9560208785</p>"}
    },
    {
        "filename": "refund-policy.html",
        "title": "Refund Policy | Anufix",
        "description": "Refund Policy for Anufix Fabrication Services.",
        "content_generator": "generate_legal",
        "extra": {"name": "Refund Policy", "text": "<p>At ANUFIX, we strive to provide quality metal fabrication services. Please read our refund policy carefully.</p><h3>Advance Payment</h3><p>Advance payment is required to confirm the order and start the fabrication work. This amount is generally non-refundable as it is used for material purchase and initial work.</p><h3>Refund Eligibility</h3><p>Refunds may be considered only in the following cases:</p><ul><li>If the service is not started by our team</li><li>If we are unable to complete the project due to internal reasons</li></ul><h3>No Refund Cases</h3><p>Refunds will not be provided in the following situations:</p><ul><li>Change of mind after order confirmation</li><li>Delay due to customer-side issues</li><li>Work already started or completed</li></ul><h3>Partial Refund</h3><p>In some cases, a partial refund may be provided depending on the work completed and material used.</p><h3>Cancellation</h3><p>Any cancellation request will be reviewed on a case-by-case basis.</p><h3>Contact Us</h3><p>ANUFIX<br>Sector 22, Noida, Uttar Pradesh<br>Phone: 9560208785</p><p>By booking our services, you agree to this refund policy.</p>"}
    },
    {
        "filename": "business-verification.html",
        "title": "Business Verification | Anufix",
        "description": "Business Verification details for Anufix.",
        "content_generator": "generate_legal",
        "extra": {"name": "Business Verification", "text": "<p>ANUFIX is a Government of India registered MSME (Udyam Registration No: UDYAM-UP-28-0211436).</p><p>We are based in Noida, Uttar Pradesh, and provide professional metal fabrication services including gates, grills, railings, and custom fabrication work.</p><h3>Business Details:</h3><ul><li>Name: ANUFIX</li><li>Type: Micro Enterprise (MSME)</li><li>Activity: Metal Fabrication (NIC 25999)</li><li>Address: G-227B, 1st Floor, Sector 22, Noida – 201301</li><li>Phone: 9560208785</li></ul><p>This registration confirms that our business is officially recognized and operates as a verified fabrication service provider.</p>"}
    }
]

def generate_home(page):
    return """
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Custom <span>Metal Fabrication Services</span> in Noida</h1>
            <p>MSME Registered (UDYAM-UP-28-0211436) | Expert Gate, Grill & Structural Fabrication<br>We provide high-quality iron, steel, and custom fabrication work for residential and commercial projects.</p>
            <div class="hero-btns animate-on-scroll">
                <a href="tel:9560208785" class="btn"><i class="fas fa-phone-alt"></i> Call Now: 9560208785</a>
                <a href="services.html" class="btn btn-outline">Book Fabrication Service</a>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="section">
        <div class="container animate-on-scroll">
            <h2 class="section-title">WHY CHOOSE US</h2>
            <p class="section-subtitle">We deliver high-quality, strong and long-lasting fabrication work.</p>
            
            <div class="feature-list">
                <div class="feature-item">
                    <i class="fas fa-check-circle feature-icon"></i>
                    <h4>MSME Registered Business (Government Verified)</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-users feature-icon"></i>
                    <h4>Skilled Fabricators</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-shield-alt feature-icon"></i>
                    <h4>Strong & Durable Materials</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-pen-nib feature-icon"></i>
                    <h4>Custom Design Available</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-tags feature-icon"></i>
                    <h4>Affordable Pricing</h4>
                </div>
                <div class="feature-item">
                    <i class="fas fa-clock feature-icon"></i>
                    <h4>On-Time Project Delivery</h4>
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
                    <h2>ABOUT US:</h2>
                    <p>ANUFIX is a Government of India registered MSME (Udyam Registration No: UDYAM-UP-28-0211436), based in Noida, Uttar Pradesh.</p>
                    <p>We specialize in metal fabrication services including gates, grills, railings, and custom structural work. Our focus is on delivering strong, durable, and precision-built fabrication solutions for homes, shops, and industrial requirements.</p>
                    <p>With skilled fabricators and quality materials, we ensure long-lasting and cost-effective fabrication work tailored to client needs.</p>
                    
                    <h3 style="margin-top:30px; font-size:1.4rem;">Business Details:</h3>
                    <ul style="list-style:disc; margin-left:20px; color:var(--text-light); margin-bottom: 20px;">
                        <li>Enterprise Type: Micro (MSME)</li>
                        <li>Industry: Metal Fabrication (NIC 25999)</li>
                        <li>Location: Sector 22, Noida, Uttar Pradesh</li>
                        <li>Established: 2025</li>
                    </ul>
                    <p>We are committed to quality workmanship, timely delivery, and customer satisfaction.</p>
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
                            <p>9560208785</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon"><i class="fas fa-map-marker-alt"></i></div>
                        <div class="info-text">
                            <h4>Service Location</h4>
                            <p>Sector 22, Noida. Serving Noida, Greater Noida, Ghaziabad & nearby areas</p>
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
