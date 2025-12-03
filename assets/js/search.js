// Lunr.js zoekfunctionaliteit voor dexc-kennisbank
(function() {
  let searchIndex = null;
  let searchData = null;

  // Laad zoekdata
  async function loadSearchData() {
    if (searchData) return searchData;
    const response = await fetch('/dexc-kennisbank/search-data.json');
    searchData = await response.json();
    return searchData;
  }

  // Bouw Lunr index
  async function buildIndex() {
    if (searchIndex) return searchIndex;
    const data = await loadSearchData();
    
    searchIndex = lunr(function() {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('categories', { boost: 5 });
      this.field('content');
      
      data.forEach(doc => this.add(doc));
    });
    
    return searchIndex;
  }

  // Zoekfunctie
  async function search(query) {
    const index = await buildIndex();
    const data = await loadSearchData();
    const results = index.search(query);
    
    return results.map(result => {
      const doc = data.find(d => d.url === result.ref);
      return { ...doc, score: result.score };
    });
  }

  // Render resultaten
  function renderResults(results, container) {
    if (results.length === 0) {
      container.innerHTML = '<p class="no-results">Geen resultaten gevonden.</p>';
      return;
    }
    
    const html = results.map(r => `
      <div class="search-result">
        <h3><a href="${r.url}">${r.title}</a></h3>
        <p class="meta">${r.date} | ${r.categories.join(', ')}</p>
        <p class="excerpt">${r.content.substring(0, 150)}...</p>
      </div>
    `).join('');
    
    container.innerHTML = html;
  }

  // Init
  document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;
    
    let debounceTimer;
    searchInput.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      const query = this.value.trim();
      
      if (query.length < 2) {
        searchResults.innerHTML = '';
        return;
      }
      
      debounceTimer = setTimeout(async () => {
        const results = await search(query);
        renderResults(results, searchResults);
      }, 300);
    });

    // Check URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const q = urlParams.get('q');
    if (q) {
      searchInput.value = q;
      searchInput.dispatchEvent(new Event('input'));
    }
  });
})();
