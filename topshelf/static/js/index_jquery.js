$(document).ready(function() {
//     $(function(){
//          $("#home-button1").click(function(){
//              $("#btn_replace").load("accounts/login/");
//          });
//      });
//});

////Kudos to this person for the solution: http://stackoverflow.com/questions/18525984/jquery-load-multiple-blocks-in-django
//    Doesn't really work but it's close.
    $('#home-button1').click(function(event)
    {
        event.preventDefault();
        $.get("accounts/login/", function(data)
        {
            var test=$(data).find("#login_content");
            $("#btn_replace").html(test);
        });
    });
});