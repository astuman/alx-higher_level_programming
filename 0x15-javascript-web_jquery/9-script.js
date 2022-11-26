$(function () {  
    function getSalut () {
      return $.get({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        dataType: 'json'
      });
    }
  
    getSalut().then((res) => {
        $('#hello').text(res.hellooo);
    });
  });