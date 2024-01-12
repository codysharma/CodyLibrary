// functions
const apiCall = () => {
    bookApiUrl = 'http://localhost:8000/books'
    fetch(bookApiUrl)
        .then(res => {
            res.json().then((booksData) => {
                console.log(booksData);
                displayData(booksData)
            })
        })
        .catch(err => {
            console.log("somthing went wrong", err);
        })
}

function displayData(books) {
    // console.log(books);
    var str = '<ul>'

    books.forEach(function(book) {
        if (book.genre === 'WH')
                str += '<li>' + '"' + book.title + '"' +  ' by: ' + book.author_name + '</li>';
            });

    str += '</ul>'
    document.getElementById('bookList').innerHTML = str;
}

apiCall();
