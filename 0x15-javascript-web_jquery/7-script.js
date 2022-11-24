$(function () {
    $.get('https://swapi-api.hbtn.io/api/people/1/?format=json', function (data, textStatus) {
        if (textStatus == 'success') {
            $('#character').text(data.name);
        }
        })
    });