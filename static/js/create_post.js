document.querySelector('form').addEventListener('submit', async function (event) {
    event.preventDefault();

    // Get form values
    const title = document.getElementById('title').value;
    const caption = document.getElementById('caption').value;
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    console.log(fileInput);

    // Create FormData object to handle file uploads and other data
    const formData = new FormData();
    formData.append('title', title);
    formData.append('caption', caption);
    formData.append('image', file);
    console.log("FormData" + formData);

    try {
        const response = await fetch('http://127.0.0.1:8000/api/createpost/', {
            method: 'POST',
            headers: {
                // 'Content-Type': 'application/json', // Don't set Content-Type for FormData
                'Authorization': `Bearer ${localStorage.getItem('access')}` // Token for authentication
            },
            body: formData,
        });

        if (response.ok) {
            const data = response.json();
            alert('Post created successfully!');
            // Redirect or refresh after successful post creation
            window.location.href = '/dash/';
        } else {
            const errorData = response.json();
            console.error('Error:', errorData);
            alert('Failed to create post. Please try again.');
        }
    } catch (error) {
        console.log('Error:', error);
        alert('An error occurred. Please try again.');
    }
});
