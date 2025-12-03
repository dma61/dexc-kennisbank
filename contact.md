---
layout: default
title: Contact & Feedback
permalink: /contact/
---

<div class="contact-container">
  <h1>💬 Contact & Feedback</h1>
  
  <p>Heb je een vraag, suggestie of heb je een fout gevonden? Laat het ons weten via GitHub Issues!</p>
  
  <div class="issue-buttons">
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=vraag.md&title=[Vraag]%20" class="btn btn-question">
      ❓ Stel een vraag
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=fout.md&title=[Fout]%20" class="btn btn-bug">
      🐛 Meld een fout
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues/new?template=suggestie.md&title=[Suggestie]%20" class="btn btn-suggestion">
      💡 Doe een suggestie
    </a>
    
    <a href="https://github.com/dma61/dexc-kennisbank/issues" class="btn btn-view">
      📋 Bekijk alle issues
    </a>
  </div>
  
  <h2>Direct contact</h2>
  <p>Voor urgente zaken kun je ook direct contact opnemen met <a href="https://github.com/dma61">@dma61</a> op GitHub.</p>
</div>

<style>
.contact-container { max-width: 700px; margin: 0 auto; padding: 20px; }
.issue-buttons { display: flex; flex-wrap: wrap; gap: 15px; margin: 30px 0; }
.btn { 
  display: inline-block; padding: 15px 25px; 
  border-radius: 8px; text-decoration: none; 
  font-weight: bold; transition: transform 0.2s;
}
.btn:hover { transform: translateY(-2px); }
.btn-question { background: #0066cc; color: white; }
.btn-bug { background: #dc3545; color: white; }
.btn-suggestion { background: #28a745; color: white; }
.btn-view { background: #6c757d; color: white; }
</style>
