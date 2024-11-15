$(document).ready(function() {
    // Real-time validation for the rating field
    $('#rating').on('input', function() {
        var rating = $(this).val();
        if (rating < 0 || rating > 5) {
            $(this).siblings('.invalid-feedback').text('Rating must be between 0 and 5 with up to two decimal places.');
            this.setCustomValidity('Rating must be between 0 and 5 with up to two decimal places..');
        } else {
            $(this).siblings('.invalid-feedback').text('');
            this.setCustomValidity('');
        }
    });

    // $('#addItemForm').submit(function(event) {
    //     event.preventDefault();
        
    //     var form = $(this);
    //     if (!form[0].checkValidity()) {
    //         event.stopPropagation();
    //     } else {
    //         var formData = form.serialize();

    //         $.ajax({
    //             url: '/add',
    //             type: 'POST',
    //             data: formData,
    //             success: function(response) {
    //                 // Redirect to the add page with success message
    //                 window.location.href = '/add?success=true';
    //             },
    //             error: function(xhr, status, error) {
    //                 console.error('Error adding item:', error);
    //                 $('#errorMessage').text('Error adding item. Please try again.').show();
    //             }
    //         });
    //     }
    //     form.addClass('was-validated');
    // });

    $('#addItemForm').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        if (!form[0].checkValidity()) {
            event.stopPropagation();
        } else {
            var formData = form.serialize();
            $.ajax({
                url: '/add',
                type: 'POST',
                data: formData,
                success: function(response) {
                    if (response.success) {
                        var successMessage = '<div class="alert alert-success"><strong>Book added successfully.</strong> <a href="/view/' + response.id + '" class="btn btn-primary">View Item</a> <a href="/add" class="btn btn-secondary">Add a New Entry</a></div>';
                        $('#successMessage').html(successMessage).show();
                        form.trigger('reset');
                        form.removeClass('was-validated');
                        $('#title').focus();
                    } else {
                        $('#errorMessage').text(response.error).show();
                    }
                },
                error: function(xhr, status, error) {
                    console.error('Error adding item:', error);
                    $('#errorMessage').text('Error adding item. Please try again.').show();
                }
            });
        }
        form.addClass('was-validated');
    });

    $('#addItemForm input').on('input', function() {
        if (!this.validity.valid) {
            $(this).addClass('is-invalid');
            $(this).next('.invalid-feedback').text(this.validationMessage);
        } else {
            $(this).removeClass('is-invalid');
            $(this).next('.invalid-feedback').text('');
        }
    });

    $('#discardChangesLink').click(function(event) {
        event.preventDefault();
        if (confirm('Are you sure you want to discard the changes?')) {
            var itemId = $(this).data('item-id');
            window.location.href = '/view/' + itemId;
        }
    });

     $('#editItemForm').on('submit', function(event) {
        if (!this.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        $(this).addClass('was-validated');
    });

    // Display error messages on input change
    $('#editItemForm input').on('input', function() {
        if (!this.validity.valid) {
            $(this).addClass('is-invalid');
            $(this).next('.invalid-feedback').text(this.validationMessage);
        } else {
            $(this).removeClass('is-invalid');
            $(this).next('.invalid-feedback').text('');
        }
    });
    
    $('#search-form').submit(function(event) {
        const queryInput = $('#searchInput');
        const query = queryInput.val().trim();

        if (/^\s*$/.test(query)) {
            event.preventDefault();
            queryInput.val('');
            queryInput.focus();
        } else {
            console.log("Performing search with query:", query);

            $.ajax({
                url: '/search',
                type: 'GET',
                data: { query: query },
                success: function(response) {
                    console.log("Search response:", response);
                    updateSearchResults(response.results, query);
                },
                error: function(error) {
                    console.error('Error fetching search results:', error);
                    $('#search-results').html('<p>An error occurred. Please try again later.</p>');
                },
                complete: function() {
                    queryInput.focus();
                }
            });
        }
    });

    $('.button').click(function(event) {
        event.preventDefault();
        const genre = $(this).data('genre');

        console.log("Searching by genre:", genre);

        $.ajax({
            url: '/search',
            type: 'GET',
            data: { query: genre },
            success: function(response) {
                console.log("Genre search response:", response);
                window.location.href = '/search?query=' + encodeURIComponent(genre);
            },
            error: function(error) {
                console.error('Error searching by genre:', error);
            }
        });
    });
});

function updateSearchResults(results, query) {
    const resultsContainer = $('#search-results');
    resultsContainer.empty();

    console.log("Updating search results:", results);

    if (results.length === 0) {
        resultsContainer.html('<p>No results found.</p>');
    } else {
        results.forEach(function(book) {
            const highlightedTitle = highlightText(book.title, query);
            const highlightedAuthor = highlightText(book.author, query);
            const highlightedGenre = book.genre.map(genre => highlightText(genre, query)).join(', ');

            const bookElement = `
                <div class="book mb-4">
                    <div class="row">
                        <div class="col-md-2">
                            <img src="${book.image}" alt="${book.title}" class="img-fluid">
                        </div>
                        <div class="col-md-10">
                            <h4><a href="/view/${book.id}">${highlightedTitle}</a></h4>
                            <p><strong>Author:</strong> ${highlightedAuthor}</p>
                            <p><strong>Rating:</strong> ${book.rating}</p>
                            <p><strong>Genre:</strong> ${highlightedGenre}</p>
                            <p>${book.summary.substring(0, 200)}...</p>
                        </div>
                    </div>
                </div>
            `;

            resultsContainer.append(bookElement);
        });
    }
}

function highlightText(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}
