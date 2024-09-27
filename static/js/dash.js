// Fetch posts and display them
document.addEventListener('DOMContentLoaded', function () {
    fetchPosts();
});

async function fetchPosts() {
    const accessToken = localStorage.getItem('access'); // Get access token from localStorage

    if (!accessToken) {
        console.error('Access token not found. User might not be authenticated.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/getpost/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`, // Send token in Authorization header
                'Content-Type': 'application/json'
            }
        });

        if (response.status === 401) {
            console.error('Unauthorized. Access token might be expired or invalid.');
            // Redirect to login page if token is invalid or expired
            window.location.href = '/login';
        }

        const posts = await response.json();
        displayPosts(posts);  // Assuming you have a function to display posts
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
}


// Display posts in the container
function displayPosts(posts) {
    const postsContainer = document.getElementById('posts-container');
    postsContainer.innerHTML = '';

    if (posts.length > 0) {
        posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.classList.add('post');
            postElement.innerHTML = `
                <h2>${post.title}</h2>
                <p>${post.caption}</p>
                <div class="meta">Posted by ${post.user} on ${new Date(post.created_at).toLocaleDateString()}</div>
            `;
            postsContainer.appendChild(postElement);
        });
    } else {
        postsContainer.innerHTML = '<p>No posts available.</p>';
    }
}

// Logout function
function logout() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    window.location.href = '/login';
}
