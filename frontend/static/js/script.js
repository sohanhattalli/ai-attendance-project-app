// Scroll reveal — only hides sections when JS runs (avoids invisible content if script fails to load)
document.documentElement.classList.add('js-enabled');

document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px',
    };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                revealObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feature-card, .flow-step').forEach((el) => {
        revealObserver.observe(el);
    });
});
