document.getElementById("learnMoreBtn").addEventListener("click", () => {
  window.scrollTo({
    top: document.querySelector(".main-content").offsetTop,
    behavior: "smooth",
  });
});
