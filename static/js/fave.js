$(document).ready(function(){
    $('.add-to-favorites').click(function(event){
        event.preventDefault();

        var button = $(this);
        var itemId = button.data('item-id');
        var urlTemplate = button.data('url-template');

        // Replace the placeholder in the URL template with the actual item ID
        var url = urlTemplate.replace('0', item.id);

        // Fetch the CSRF token from the meta tag
        var csrftoken = $('meta[name="csrf-token"]').attr('content');

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                if(response.success){
                    alert(response.message);
                    // Optionally, update the UI to show that the item has been added to favorites
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(xhr, status, error){
                let errorMessage = 'An error occurred';
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMessage = xhr.responseJSON.message;
                } else if (xhr.responseText) {
                    errorMessage = xhr.responseText;
                }
                alert('Error: ' + errorMessage);
            }
        });
    });
});
