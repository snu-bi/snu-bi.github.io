/*
  manages interactive member filtering by role.
  supports url hash navigation for sharing/bookmarking.
*/

{
  const filterConfig = {
    all: {
      name: "All",
      sectionIds: ["faculty", "research-professor", "phd", "master", "intern", "alumni"]
    },
    faculty: {
      name: "Faculty",
      sectionIds: ["faculty", "research-professor"]
    },
    phd: {
      name: "PhD Students",
      sectionIds: ["phd"]
    },
    master: {
      name: "Master Students",
      sectionIds: ["master"]
    },
    intern: {
      name: "Interns",
      sectionIds: ["intern"]
    },
    alumni: {
      name: "Alumni",
      sectionIds: ["alumni"]
    }
  };

  // Get current filter from URL hash
  const getCurrentFilter = () => {
    const hash = window.location.hash.slice(1);
    return hash && filterConfig[hash] ? hash : "all";
  };

  // Update active button styling
  const updateActiveButton = () => {
    const currentFilter = getCurrentFilter();
    document.querySelectorAll(".filter-btn").forEach((btn) => {
      const btnFilter = btn.getAttribute("data-filter");
      if (btnFilter === currentFilter) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });
  };

  // Map heading text to filter section IDs
  const getHeadingFilterId = (headingText) => {
    const text = headingText.toLowerCase().trim();

    if (text.includes("professor") && !text.includes("research")) {
      return "faculty";
    }
    if (text.includes("research professor")) {
      return "research-professor";
    }
    if (text.includes("phd")) {
      return "phd";
    }
    if (text.includes("master")) {
      return "master";
    }
    if (text.includes("intern")) {
      return "intern";
    }
    if (text.includes("alumni")) {
      return "alumni";
    }
    return null;
  };

  // Filter members by showing/hiding sections
  const filterMembers = (filterKey) => {
    const config = filterConfig[filterKey];
    if (!config) return;

    const allowedSections = new Set(config.sectionIds);

    // Find all headings (h1, h2, h3)
    document.querySelectorAll("h1, h2, h3").forEach((heading) => {
      // Skip main title
      if (heading.closest("body > .container") && heading.textContent.includes("Team")) {
        return;
      }

      const sectionId = getHeadingFilterId(heading.textContent);

      if (sectionId === null) return;

      const shouldShow = allowedSections.has(sectionId);

      // Show/hide heading
      heading.style.display = shouldShow ? "" : "none";
      heading.style.opacity = shouldShow ? "1" : "0";

      // Show/hide content after heading until next heading
      let nextElement = heading.nextElementSibling;
      while (nextElement && !["H1", "H2", "H3"].includes(nextElement.tagName)) {
        if (nextElement.classList.contains("grid")) {
          nextElement.style.display = shouldShow ? "" : "none";
          if (shouldShow) {
            nextElement.classList.add("portrait-grid");
          }
        } else if (nextElement.classList.contains("section")) {
          // Skip section dividers between filter groups
          break;
        } else {
          nextElement.style.display = shouldShow ? "" : "none";
        }
        nextElement = nextElement.nextElementSibling;
      }
    });

    // Smooth scroll to filter
    const filterElement = document.querySelector("#memberFilter");
    if (filterElement && window.innerWidth < 768) {
      filterElement.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  };

  // Handle filter button click
  const handleFilterClick = (event) => {
    const btn = event.target.closest(".filter-btn");
    if (!btn) return;

    const filterKey = btn.getAttribute("data-filter");
    if (!filterKey) return;

    // Update URL hash (triggers hashchange event)
    window.location.hash = filterKey;
  };

  // Initialize filter
  const init = () => {
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach((btn) => {
      btn.addEventListener("click", handleFilterClick);
    });

    // Handle hash change (browser back/forward or direct hash link)
    window.addEventListener("hashchange", () => {
      updateActiveButton();
      filterMembers(getCurrentFilter());
    });

    // Set initial state
    updateActiveButton();
    filterMembers(getCurrentFilter());
  };

  // Run on page load
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
}
