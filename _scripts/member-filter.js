/*
  manages interactive member filtering by role.
  supports url hash navigation for sharing/bookmarking.
*/

{
  const filterConfig = {
    all:    { sectionIds: ["faculty", "research-professor", "phd", "master", "intern", "alumni"] },
    faculty:{ sectionIds: ["faculty", "research-professor"] },
    phd:    { sectionIds: ["phd", "alumni"] },
    master: { sectionIds: ["master", "alumni"] },
    intern: { sectionIds: ["intern", "alumni"] },
    alumni: { sectionIds: ["alumni"] }
  };

  const getHeadingFilterId = (text) => {
    const t = text.toLowerCase().trim();
    if (t.includes("research professor")) return "research-professor";
    if (t.includes("professor"))          return "faculty";
    if (t.includes("phd"))                return "phd";
    if (t.includes("master"))             return "master";
    if (t.includes("intern"))             return "intern";
    if (t.includes("alumni"))             return "alumni";
    return null;
  };

  const getCurrentFilter = () => {
    const h = window.location.hash.slice(1);
    return h && filterConfig[h] ? h : "all";
  };

  // --- cached section map: built once at init ---
  // sectionId → Array<{ heading: Element, contents: Element[] }>
  let sectionMap = {};

  const buildSectionMap = () => {
    sectionMap = {};
    document.querySelectorAll("h1, h2, h3").forEach((heading) => {
      const id = getHeadingFilterId(heading.textContent);
      if (!id) return;

      const contents = [];
      let el = heading.nextElementSibling;
      while (el && !["H1", "H2", "H3"].includes(el.tagName)) {
        if (el.classList.contains("section")) break;
        contents.push(el);
        el = el.nextElementSibling;
      }

      if (!sectionMap[id]) sectionMap[id] = [];
      sectionMap[id].push({ heading, contents });
    });
  };

  // --- fast filter: no DOM queries, just style toggles ---
  const filterMembers = (filterKey) => {
    const config = filterConfig[filterKey];
    if (!config) return;
    const allowed = new Set(config.sectionIds);

    Object.entries(sectionMap).forEach(([id, items]) => {
      const show = allowed.has(id);
      items.forEach(({ heading, contents }) => {
        heading.style.display = show ? "" : "none";
        contents.forEach((el) => { el.style.display = show ? "" : "none"; });
      });
    });
  };

  const updateActiveButton = () => {
    const cur = getCurrentFilter();
    document.querySelectorAll(".filter-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-filter") === cur);
    });
  };

  const handleFilterClick = (e) => {
    const btn = e.target.closest(".filter-btn");
    if (!btn) return;
    const key = btn.getAttribute("data-filter");
    if (key) window.location.hash = key;
  };

  const init = () => {
    buildSectionMap();

    document.querySelectorAll(".filter-btn").forEach((btn) => {
      btn.addEventListener("click", handleFilterClick);
    });

    window.addEventListener("hashchange", () => {
      updateActiveButton();
      filterMembers(getCurrentFilter());
    });

    updateActiveButton();
    filterMembers(getCurrentFilter());
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
}
