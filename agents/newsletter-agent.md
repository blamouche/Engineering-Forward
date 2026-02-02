# Newsletter Agent

Generates a monthly newsletter with three sections.

## Usage
```
/newsletter-agent <YYYY-MM>
```

## Instructions

### Section 1: Latest from lamouche.fr/notebook
- WebFetch https://lamouche.fr/notebook/
- Extract 10 most recent articles (title + URL)

### Section 2: Technical Watch Synthesis
- Read all files in `src/YYYY-MM/`
- Extract: Title, Source, Elevator pitch, Takeaways
- Write 2-3 paragraph synthesis of trends and practical implications

### Section 3: Worth Watching
- Select 10 most impactful articles from month
- Use elevator pitch as description

### Output
Create `newsletter/YYYY-MM.md`:
```markdown
# Newsletter YYYY-MM

==intro text==

## My latest articles from the notebook

**[Title](https://lamouche.fr/notebook/posts/...)**
Brief description
[repeat 10x]

---

## What's hot today ?

[2-3 paragraphs: themes, trends, practical implications]

---

## Worth watching

Elevator pitch text.
[Link](Source URL)
[repeat 10x]

---

## Cartography for noobs

**🧭 Want to understand how maps really work?**

This newsletter explains, step by step, the foundations of modern cartography: data, projections, use cases, and key challenges — simply, with no prior knowledge required.

[Subscribe](https://subscribepage.io/ylAON7)
```

## Notes
- Section 1: lamouche.fr URLs; Sections 2-3: external Source URLs
- English, factual, editorial tone
- Avoid superlatives (amazing, groundbreaking, etc.)
- Focus on engineering and future of work
