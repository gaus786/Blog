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

//display posts
function displayPosts(posts) {
    const postsContainer = document.getElementById('posts-container');
    postsContainer.innerHTML = '';

    if (posts.length > 0) {
        posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.classList.add('post');

            // Ensure the image URL is correct, using the base URL if necessary
            const imageUrl = post.image;  // Assuming 'post.image' returns the correct path

            postElement.innerHTML = `
                <h2>${post.title}</h2>
                
                <img src="${imageUrl}" alt="${post.title}" width="500" height="600">
                <p>${post.caption}</p>

                <!-- Like Button -->
                <div class="like-container">
                    <button class="like-button" onclick="likePost(${post.id})">
                        <span class="heart">&#10084;</span> 
                        <span id="like-count-${post.id}">${post.likes}</span> Like
                    </button>
                </div>

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
    window.location.href = 'http://127.0.0.1:8000/login';

}






async function likePost(postId) {
    const response = await fetch('http://127.0.0.1:8000/api/like/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`,  // Include the JWT token

        },
        body: JSON.stringify({
            post_id: postId
            // user_id: localStorage.getItem('user_id')
        })
    });

    const data = await response.json();

    if (response.ok) {
        // Update the like count dynamically
        const likeCountElement = document.getElementById(`like-count-${postId}`);
        likeCountElement.textContent = data.likes;
    } else {
        console.error('Error:', data.error);
    }
}
