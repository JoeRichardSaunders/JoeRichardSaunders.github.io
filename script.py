# Content for index.html (Updated with 'No One Cares Man' branding)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joe Richard Saunders | No One Cares Man</title>
    <meta name="description" content="Baltimore-based comedian Joe Richard Saunders. Survivor. Producer. No One Cares Man.">
    <link rel="stylesheet" href="style.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Lora:ital,wght@1,400&family=Courier+Prime&display=swap" rel="stylesheet">
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>

    <!-- Mobile Nav Toggle -->
    <button id="nav-toggle" class="mobile-nav-toggle" aria-label="Toggle Navigation">
        <i class="fas fa-bars"></i>
    </button>

    <header class="sidebar" id="sidebar">
        <div class="brand">
            <h1>Joe Richard<br>Saunders</h1>
            <p class="tagline">IS "NO ONE CARES MAN"</p>
        </div>
        <nav>
            <ul>
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#showcase" class="nav-link">The Evidence</a></li>
                <li><a href="#about" class="nav-link">Origin Story</a></li>
                <li><a href="#consulting" class="nav-link">Expertise</a></li>
                <li><a href="#harm-city" class="nav-link">Harm City Comedy</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </nav>
        <div class="socials">
            <a href="https://instagram.com/joe.richard.saunders" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://youtube.com/@Joe.Richard.Saunders" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="#" target="_blank" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section id="home" class="hero">
            <div class="hero-image-wrapper">
                <img src="Joe-Richard-Saunders-Laugh.jpg" alt="Joe Richard Saunders Laughing" class="hero-img">
                <div class="hero-overlay-text">NO ONE CARES MAN</div>
            </div>
            <div class="hero-content">
                <h2>THE HERO<br>NOBODY ASKED FOR.</h2>
                <p>"I survived stage 4 cancer, a brain relapse, and the Baltimore dating scene. And honestly? No one cares."</p>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    <a href="#showcase" class="btn">Watch The Tapes</a>
                    <a href="epk.html" class="btn btn-outline" style="margin-top:0;">View Resume / EPK</a>
                </div>
            </div>
        </section>

        <!-- DYNAMIC SHOWCASE SECTION (THE EVIDENCE) -->
        <section id="showcase" class="content-block showcase-section">
            <div class="showcase-header">
                <h3>THE EVIDENCE</h3>
                <p class="showcase-subtitle">The tragic backstory that led to the punchline.</p>
            </div>

            <!-- Tabs -->
            <div class="tabs">
                <button class="tab-btn active" data-target="video-panel-1">
                    <i class="fas fa-hospital-alt"></i> THE BEFORE
                </button>
                <button class="tab-btn" data-target="video-panel-2">
                    <i class="fas fa-theater-masks"></i> THE RETURN
                </button>
                <button class="tab-btn" data-target="audio-panel">
                    <i class="fas fa-music"></i> SECRET LORE
                </button>
            </div>

            <!-- Tab Content -->
            <div class="tab-content-container">
                
                <!-- Video Panel 1: The Before (Treatment) -->
                <div id="video-panel-1" class="tab-panel active">
                    <div class="video-wrapper">
                        <!-- User to insert Before Treatment video ID -->
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/PLACEHOLDER_BEFORE?si=Placeholder" title="The Before Video" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="caption-box">
                        <h4>The "Before" Tape</h4>
                        <p>Filmed the day before brain treatment began. No pity. Just jokes.</p>
                    </div>
                </div>

                <!-- Video Panel 2: The Return (Marquee) -->
                <div id="video-panel-2" class="tab-panel">
                    <div class="video-wrapper">
                        <!-- User to insert Marquee video ID -->
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/PLACEHOLDER_MARQUEE?si=Placeholder" title="Sense of Tumor Benefit" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="caption-box">
                        <h4>"Sense of Tumor" Benefit</h4>
                        <p>First feature set back. Name on the marquee at The Black Box Silver Spring. Proof of life.</p>
                    </div>
                </div>

                <!-- Audio Panel: The Hinge T-Pain Incident -->
                <div id="audio-panel" class="tab-panel">
                    <div class="audio-visualizer-mock">
                        <div class="bars">
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                            <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                        </div>
                        <i class="fas fa-play play-icon"></i>
                    </div>
                    <div class="caption-box">
                        <h4>The "Hinge Match" Serenades</h4>
                        <p>"She asked for a voice memo. I gave her T-Pain. Yes, I actually produced this."</p>
                        <a href="#" class="btn btn-outline">Listen to the Secret Tracks</a>
                    </div>
                </div>

            </div>
        </section>

        <!-- About Section (ORIGIN STORY) -->
        <section id="about" class="content-block">
            <h3>THE ORIGIN STORY</h3>
            <p class="lead">"I died twice. It was boring. The paperwork was worse."</p>
            <div class="text-columns">
                <p>Joe Richard Saunders is <strong>No One Cares Man</strong>. A superhero whose only power is indifference in the face of annihilation. He played the legendary <strong>9:30 Club</strong> at age 13. He was a bedroom producer on <strong>BBC Radio 1xtra</strong>. Then he survived <strong>Stage 4 Lymphoma</strong>, emergency trauma, and a brain cancer relapse.</p>
                <p>His arch-nemesis? Audiences who don't believe he was ever sick because he "looks too good." He fights crime by telling jokes about spinal taps and Young Adult Cancer Care, all while managing the crushing defeat of being a "Middle Class" comedian.</p>
                <p>He is not here to save you. He is here to remind you that nothing matters, so you might as well laugh.</p>
                <br>
                <a href="epk.html" class="btn">View Secret Identity (Resume)</a>
            </div>
        </section>

        <!-- CONSULTING SECTION -->
        <section id="consulting" class="content-block inverted" style="background: var(--card-bg);">
            <div class="consulting-wrapper" style="text-align: center; max-width: 900px; margin: 0 auto;">
                <h3 style="color: var(--highlight-color); margin-bottom: 1rem;">SUPERPOWERS & EXPERTISE</h3>
                <p class="lead" style="font-size: 1.5rem; margin-bottom: 3rem; color: var(--text-color);">"Expertise born from trauma and obscurity."</p>
                
                <p style="margin-bottom: 1rem; color: var(--secondary-text); font-weight: bold; text-transform: uppercase;">Medical & Advocacy</p>
                <div class="tags-container" style="margin-bottom: 2.5rem;">
                    <span class="tag tag-accent">Young Adult Cancer Care</span>
                    <span class="tag tag-accent">Emergency Trauma Ops</span>
                    <span class="tag tag-accent">"Survivor Guilt" Humor</span>
                    <span class="tag tag-accent">Patient Advocacy</span>
                </div>

                <p style="margin-bottom: 1rem; color: var(--secondary-text); font-weight: bold; text-transform: uppercase;">Culture & Tech</p>
                <div class="tags-container">
                    <span class="tag">DC Defense Culture</span>
                    <span class="tag">Nuclear Submarine School</span>
                    <span class="tag">Gonzo Reporting</span>
                    <span class="tag">Bedroom Producer Lore</span>
                    <span class="tag">Internet Memetics</span>
                </div>
            </div>
        </section>

        <!-- Harm City Comedy Section -->
        <section id="harm-city" class="content-block inverted">
            <div class="accent-box">
                <div class="accent-header">
                    <h3>HARM CITY COMEDY</h3>
                    <span class="badge">HQ</span>
                </div>
                <p>The secret headquarters of Baltimore's indie comedy scene. Proceeds support <strong>Young Adult Cancer Care</strong> initiatives.</p>
                <ul class="feature-list">
                    <li><i class="fas fa-bolt"></i> Curated Lineups</li>
                    <li><i class="fas fa-heart"></i> Charity Focused</li>
                    <li><i class="fas fa-microphone-alt"></i> Artsy Vibe</li>
                </ul>
                <div class="btn-group">
                    <a href="#" class="btn btn-outline">Get Tickets</a>
                    <a href="#" class="btn btn-text">View Archives &rarr;</a>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="content-block footer-section">
            <h3>SIGNAL THE HERO</h3>
            <p>Available for clubs, colleges, and corporate gigs that need a reality check.</p>
            <a href="mailto:booking@joerichardsaunders.com" class="email-link">booking@joerichardsaunders.com</a>
            <p class="copyright">&copy; 2026 Joe Richard Saunders. <br>Design by Perplexity.</p>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
"""

# Content for style.css (Updated with Hero Overlay Text)
css_content = """/* RESET & VARS */
:root {
    /* RAVEN'S LOFT PALETTE */
    --bg-color: #19102E;      /* Deep Midnight Purple */
    --text-color: #FFFFFF;    /* Pure White */
    --accent-color: #E03C31;  /* Maryland Red (Buttons/Links) */
    --highlight-color: #FFD700; /* Flag/Ravens Gold (Hover/Focus) */
    --secondary-text: #A89FBD; /* Muted Purple-Grey */
    
    --card-bg: #261C3D;       /* Slightly lighter purple for cards */
    --border-color: #382E52;  /* Dark purple border */
    
    --sidebar-width: 280px;
    --font-ui: 'Inter', sans-serif;
    --font-script: 'Courier Prime', monospace;
    --font-edit: 'Lora', serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
    font-family: var(--font-ui);
    color: var(--text-color);
    background: var(--bg-color);
    line-height: 1.6;
    display: flex;
    min-height: 100vh;
}

/* TYPOGRAPHY OVERRIDES */
h1, h2, h3, h4 {
    font-family: var(--font-ui);
    font-weight: 900; /* BOLD SANS */
    text-transform: uppercase;
    letter-spacing: -0.02em;
}

/* SIDEBAR NAV (Desktop) */
.sidebar {
    width: var(--sidebar-width);
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    padding: 3rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-right: 1px solid var(--border-color);
    background: var(--bg-color);
    z-index: 100;
}

.brand h1 { font-size: 1.8rem; line-height: 1; color: var(--text-color); }
.tagline { font-size: 0.85rem; color: var(--highlight-color); margin-top: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: bold; }

.sidebar nav ul { list-style: none; margin-top: 2rem; }
.sidebar nav li { margin-bottom: 1rem; }
.nav-link { text-decoration: none; color: var(--secondary-text); font-size: 1rem; font-weight: 700; transition: color 0.3s; text-transform: uppercase; }
.nav-link:hover { color: var(--highlight-color); }

.socials a { color: var(--text-color); font-size: 1.2rem; margin-right: 1rem; transition: color 0.3s; }
.socials a:hover { color: var(--accent-color); }

/* MAIN CONTENT */
main {
    margin-left: var(--sidebar-width);
    width: calc(100% - var(--sidebar-width));
    padding: 0;
}

/* HERO */
.hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 90vh;
    align-items: center;
    padding: 4rem;
    gap: 3rem;
}

.hero-image-wrapper { position: relative; }
.hero-img {
    width: 100%;
    max-height: 80vh;
    object-fit: cover;
    filter: grayscale(100%);
    transition: filter 0.5s ease;
    border: 4px solid var(--text-color); /* Photo Frame border */
    box-shadow: 10px 10px 0px var(--accent-color); /* Pop art shadow */
}

/* SUPERHERO OVERLAY TEXT */
.hero-overlay-text {
    position: absolute;
    bottom: -20px;
    right: -20px;
    background: var(--highlight-color);
    color: #000;
    padding: 0.5rem 1rem;
    font-weight: 900;
    font-size: 1.5rem;
    text-transform: uppercase;
    transform: rotate(-5deg);
    box-shadow: 4px 4px 0px #000;
    z-index: 10;
}

.hero-img:hover { filter: grayscale(0%); box-shadow: 10px 10px 0px var(--highlight-color); } 

.hero-content h2 { font-size: 4rem; line-height: 0.9; margin-bottom: 1.5rem; color: var(--text-color); }
.hero-content p { font-size: 1.2rem; font-weight: 400; color: var(--secondary-text); margin-bottom: 2rem; max-width: 400px; }

/* BUTTONS */
.btn {
    display: inline-block;
    padding: 1.2rem 2.5rem;
    background: var(--accent-color);
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-weight: 900;
    transition: all 0.2s;
    border: none;
    cursor: pointer;
    box-shadow: 4px 4px 0px #000; /* Comic book shadow */
}
.btn:hover { 
    background: var(--highlight-color); 
    color: #000; 
    transform: translate(-2px, -2px);
    box-shadow: 6px 6px 0px #fff;
}

/* SECTIONS */
.content-block { padding: 6rem 4rem; border-bottom: 1px solid var(--border-color); }
.content-block h3 { font-size: 1rem; color: var(--secondary-text); margin-bottom: 2rem; letter-spacing: 0.2em; }

/* DYNAMIC SHOWCASE SECTION */
.showcase-section { background: #120b21; } /* Slightly darker bg */
.showcase-header { margin-bottom: 3rem; text-align: center; }
.showcase-header h3 { font-size: 3rem; color: var(--highlight-color); margin-bottom: 0.5rem; letter-spacing: 0; }
.showcase-subtitle { font-family: var(--font-edit); font-style: italic; color: var(--text-color); font-size: 1.2rem; }

/* Tabs */
.tabs { display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap; }
.tab-btn {
    background: transparent;
    border: 2px solid var(--secondary-text);
    color: var(--secondary-text);
    padding: 1rem 2rem;
    font-family: var(--font-ui);
    font-weight: 900;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s;
    font-size: 1.1rem;
}
.tab-btn i { margin-right: 0.5rem; }
.tab-btn:hover { border-color: var(--text-color); color: var(--text-color); }
.tab-btn.active {
    background: var(--accent-color);
    border-color: var(--accent-color);
    color: #fff;
    box-shadow: 4px 4px 0px var(--highlight-color);
}

/* Tab Panels */
.tab-panel { display: none; animation: fadeIn 0.5s ease; }
.tab-panel.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

.caption-box { margin-top: 1.5rem; text-align: center; color: var(--secondary-text); }
.caption-box h4 { font-size: 1.5rem; color: var(--text-color); margin-bottom: 0.5rem; }

/* Video Wrapper */
.video-wrapper { position: relative; padding-bottom: 56.25%; height: 0; border: 4px solid var(--text-color); box-shadow: 8px 8px 0px var(--accent-color); }
.video-wrapper iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }

/* Script Paper Style */
.script-paper {
    background: #fdfdfd;
    color: #000;
    padding: 3rem;
    font-family: var(--font-script);
    max-width: 800px;
    margin: 0 auto;
    border: 1px solid #ccc;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    position: relative;
    transform: rotate(-1deg);
}
.script-paper:before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image: linear-gradient(#e0e0e0 1px, transparent 1px);
    background-size: 100% 1.5rem; /* Ruling lines */
    opacity: 0.2; pointer-events: none;
}
.slugline { font-weight: bold; text-transform: uppercase; margin-bottom: 1rem; margin-top: 1rem; }
.action { margin-bottom: 1rem; }
.character { margin: 0 auto; width: 50%; text-align: center; margin-top: 1rem; }
.dialogue { margin: 0 auto; width: 70%; text-align: center; margin-bottom: 1rem; }

/* Audio Mock */
.audio-visualizer-mock {
    height: 200px;
    background: #000;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid var(--highlight-color);
    position: relative;
}
.bars { display: flex; align-items: flex-end; gap: 5px; height: 50px; }
.bar { width: 10px; background: var(--accent-color); animation: bounce 1s infinite ease-in-out; }
.bar:nth-child(even) { animation-duration: 1.2s; background: var(--highlight-color); }
@keyframes bounce { 0%, 100% { height: 10px; } 50% { height: 40px; } }
.play-icon { font-size: 4rem; color: #fff; z-index: 2; position: absolute; text-shadow: 0 0 10px var(--accent-color); }

/* TAGS (For Consulting Section) */
.tags-container { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; margin-top: 2rem; }
.tag {
    background: transparent;
    border: 1px solid var(--text-color);
    color: var(--text-color);
    padding: 0.5rem 1rem;
    text-transform: uppercase;
    font-weight: 700;
    font-size: 0.9rem;
    transition: all 0.3s;
}
.tag:hover {
    background: var(--highlight-color);
    color: #000;
    border-color: var(--highlight-color);
    transform: translateY(-2px);
    box-shadow: 4px 4px 0px var(--accent-color);
}
.tag-accent {
    border-color: var(--accent-color);
    color: var(--accent-color);
}
.tag-accent:hover {
    background: var(--accent-color);
    color: #fff;
    box-shadow: 4px 4px 0px var(--highlight-color);
}

/* MANIFESTO */
.lead { font-family: var(--font-edit); font-size: 2rem; font-style: italic; margin-bottom: 2rem; line-height: 1.3; color: var(--text-color); }
.text-columns { column-count: 2; column-gap: 3rem; color: var(--secondary-text); font-size: 1.1rem; }

/* HARM CITY (Pure Black Cut) */
.inverted { background: #000000; color: #fff; border-bottom: none; }
.inverted h3 { color: var(--highlight-color); font-size: 2rem; margin-bottom: 1rem; }
.badge { background: var(--accent-color); color: #fff; padding: 4px 8px; font-size: 0.8rem; border-radius: 4px; vertical-align: middle; transform: rotate(-5deg); display: inline-block; border: 2px solid #fff; }

.btn-outline { border: 2px solid var(--text-color); background: transparent; color: var(--text-color); padding: 1rem 2rem; text-decoration: none; text-transform: uppercase; font-weight: bold; transition: all 0.3s; display: inline-block; margin-top: 1rem; }
.btn-outline:hover { background: var(--text-color); color: #000; }

/* FOOTER */
.email-link { font-size: 1.5rem; color: var(--text-color); text-decoration: none; border-bottom: 4px solid var(--accent-color); font-weight: 700; transition: all 0.3s; }
.email-link:hover { background: var(--accent-color); color: #fff; border: none; padding: 0 5px; }
.copyright { margin-top: 3rem; font-size: 0.8rem; color: var(--secondary-text); }
.mobile-nav-toggle { display: none; }

/* MOBILE RESPONSIVE */
@media (max-width: 768px) {
    body { flex-direction: column; }
    .sidebar { transform: translateX(-100%); width: 100%; height: auto; bottom: 0; padding-top: 5rem; border-right: none; background: var(--bg-color); border-top: 1px solid var(--border-color); }
    .sidebar.active { transform: translateX(0); }
    main { margin-left: 0; width: 100%; }
    
    .mobile-nav-toggle { display: block; position: fixed; top: 1rem; right: 1rem; z-index: 200; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-color); }
    
    .hero { grid-template-columns: 1fr; padding: 2rem; text-align: center; gap: 2rem; }
    .hero-content h2 { font-size: 3rem; }
    .hero-img { border-width: 2px; box-shadow: 6px 6px 0px var(--accent-color); }
    
    .text-columns { column-count: 1; }
    .content-block { padding: 4rem 2rem; }
    
    .script-paper { padding: 1.5rem; transform: rotate(0); }
    .slugline { font-size: 0.9rem; }
    .dialogue { width: 100%; }
    .character { width: 100%; }
}
"""

with open("index.html", "w") as f:
    f.write(html_content)

with open("style.css", "w") as f:
    f.write(css_content)

print("Files updated with 'No One Cares Man' branding.")
