function initProteinTables() {
  document.querySelectorAll('[data-protein-table]').forEach((table) => {
    const panel = table.closest('.table-panel') || document;
    const search = panel.querySelector('[data-search]');
    const statusFilter = panel.querySelector('[data-status-filter]');
    const categoryFilter = panel.querySelector('[data-category-filter]');
    const clear = panel.querySelector('[data-clear]');
    const sortScore = panel.querySelector('[data-sort-score]');
    const sortNuclear = panel.querySelector('[data-sort-nuclear]');
    const visibleCount = panel.querySelector('[data-visible-count]');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const categories = Array.from(new Set(rows.map((row) => row.dataset.category).filter(Boolean))).sort();
    if (categoryFilter && categoryFilter.options.length <= 1) {
      categories.forEach((cat) => { const opt = document.createElement('option'); opt.value = cat; opt.textContent = cat; categoryFilter.appendChild(opt); });
    }
    function apply() {
      const q = (search?.value || '').trim().toLowerCase();
      const status = statusFilter?.value || '';
      const category = categoryFilter?.value || '';
      let shown = 0;
      rows.forEach((row) => {
        const ok = (!q || row.dataset.gene.includes(q)) && (!status || row.dataset.status === status) && (!category || row.dataset.category === category);
        row.hidden = !ok; if (ok) shown += 1;
      });
      if (visibleCount) visibleCount.textContent = String(shown);
    }
    function sortBy(field) {
      const sorted = rows.slice().sort((a, b) => {
        const av = parseFloat(a.dataset[field] || '-Infinity');
        const bv = parseFloat(b.dataset[field] || '-Infinity');
        return bv - av || a.dataset.gene.localeCompare(b.dataset.gene);
      });
      sorted.forEach((row) => tbody.appendChild(row));
    }
    search?.addEventListener('input', apply); statusFilter?.addEventListener('change', apply); categoryFilter?.addEventListener('change', apply);
    clear?.addEventListener('click', () => { if (search) search.value = ''; if (statusFilter) statusFilter.value = ''; if (categoryFilter) categoryFilter.value = ''; apply(); });
    sortScore?.addEventListener('click', () => sortBy('score'));
    sortNuclear?.addEventListener('click', () => sortBy('nuclearScore'));
    apply();
  });
}
document.addEventListener('DOMContentLoaded', initProteinTables);
