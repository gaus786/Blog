document.addEventListener("DOMContentLoaded", function () {
  const createPostForm = document.getElementById("create-post-form");
  const postContentInput = document.getElementById("post-content");
  const allPostsList = document.getElementById("all-posts-list");
  const userPostsList = document.getElementById("user-posts-list");
  const fetchPostsBtn = document.getElementById("fetch-posts-btn");
  const fetchUserPostsBtn = document.getElementById("fetch-user-posts-btn");
  const userIdInput = document.getElementById("user-id-input");

  const baseUrl = "http://127.0.0.1:8000/"; // Adjust the base URL as per your setup

  // Create a new post
  createPostForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const postData = {
      content: postContentInput.value,
    };
    const token = localStorage.getItem("access");

    fetch(baseUrl + "createpost/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`, // Replace with actual token
      },
      body: JSON.stringify(postData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        alert("Post created successfully!");
        postContentInput.value = "";
      })
      .catch((error) => console.error("Error:", error));
  });

  // Fetch all posts
  fetchPostsBtn.addEventListener("click", function () {
    const token = localStorage.getItem("access");
    fetch(baseUrl + "getpost/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`, // Replace with actual token
      },
    })
      .then((response) => response.json())
      .then((data) => {
        allPostsList.innerHTML = "";
        data.forEach((post) => {
          const li = document.createElement("li");
          li.textContent = post.content;
          allPostsList.appendChild(li);
        });
      })
      .catch((error) => console.error("Error:", error));
  });

  // Fetch user-specific 
  postsfetchUserPostsBtn.addEventListener("click", function () {
    const userId = userIdInput.value;
    const token = localStorage.getItem("access");
    
    fetch(baseUrl + `userpost/${userId}`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // Log the data to inspect the response
        userPostsList.innerHTML = "";
        
        if (Array.isArray(data)) {
          data.forEach((post) => {
            const li = document.createElement("li");
            li.textContent = post.content;
            userPostsList.appendChild(li);
          });
        } else {
          console.error('Error: Expected an array but received:', data);
          alert('Unexpected response format. Please try again.');
        }
      })
      .catch((error) => console.error("Error:", error));
});
