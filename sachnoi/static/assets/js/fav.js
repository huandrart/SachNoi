function addToFavorite(bookId) {
    fetch(`/add-to-favorite/${bookId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'added') {
                alert('Đã thêm vào danh sách yêu thích!');
            } else {
                alert('Sách đã có trong danh sách yêu thích!');
            }
        });
}

function removeFromFavorite(bookId) {
    fetch(`/remove-from-favorite/${bookId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'removed') {
                alert('Đã xóa khỏi danh sách yêu thích!');
                location.reload();
            }
        });
}