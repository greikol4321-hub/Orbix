// JavaScript global para navegación
document.addEventListener('DOMContentLoaded', function() {
    // Crear el HTML de navegación
    const navHTML = `
        <nav class="navbar">
            <div class="nav-container">
                <a href="/" class="logo">
                    <div class="logo-icon">🛡️</div>
                    ORBIX
                </a>
                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="/" class="nav-link" data-page="presentacion">🏠 Presentación</a>
                    </li>
                    <li class="nav-item">
                        <a href="/aenki" class="nav-link" data-page="aenki">🤖 Ae.N.K.I.</a>
                    </li>
                    <li class="nav-item">
                        <a href="/sentinel" class="nav-link" data-page="sentinel">🛡️ Sentinel</a>
                    </li>
                    <li class="nav-item">
                        <a href="/portafolio" class="nav-link" data-page="portafolio">💼 Portafolio</a>
                    </li>
                    <li class="nav-item">
                        <a href="/blog" class="nav-link" data-page="blog">📝 Blog</a>
                    </li>
                    <li class="nav-item">
                        <a href="/documentos" class="nav-link" data-page="documentos">📄 Documentos</a>
                    </li>
                    <li class="nav-item">
                        <a href="/contacto-chat" class="nav-link" data-page="contacto">📞 Contacto</a>
                    </li>
                </ul>
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </nav>
    `;

    // Insertar la navegación al inicio del body
    document.body.insertAdjacentHTML('afterbegin', navHTML);

    // Resaltar página actual
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || 
            (currentPath === '/' && href === '/') ||
            (currentPath.includes('aenki') && href === '/aenki') ||
            (currentPath.includes('sentinel') && href === '/sentinel') ||
            (currentPath.includes('portafolio') && href === '/portafolio') ||
            (currentPath.includes('blog') && href === '/blog') ||
            (currentPath.includes('contacto') && href === '/contacto-chat')) {
            link.classList.add('active');
        }
    });

    // Funcionalidad del menú hamburguesa
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Cerrar menú al hacer click en un enlace
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Smooth scrolling para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Función para crear botones de navegación en el contenido
function createNavButtons() {
    return `
        <div class="nav-buttons">
            <a href="/" class="nav-btn">🏠 Presentación Orbix</a>
            <a href="/aenki" class="nav-btn">🤖 Ae.N.K.I. IA</a>
            <a href="/sentinel" class="nav-btn">🛡️ Dashboard Sentinel</a>
            <a href="/portafolio" class="nav-btn">💼 Portafolio</a>
            <a href="/blog" class="nav-btn">📝 Blog Tech</a>
            <a href="/documentos" class="nav-btn">📄 Documentos</a>
            <a href="/contacto-chat" class="nav-btn">📞 Contacto + Chat</a>
        </div>
    `;
}

// Función para añadir efectos visuales
function addVisualEffects() {
    // Efecto de partículas en el fondo (opcional)
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '-1';
    canvas.style.opacity = '0.3';
    
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    
    for (let i = 0; i < 50; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            size: Math.random() * 2 + 1
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'rgba(0, 255, 128, 0.5)';
        
        particles.forEach(particle => {
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;
            
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fill();
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}
