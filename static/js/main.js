// Button function to quick scroll to the top 
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("topBtn").style.display = "block";
        
        } else {
            document.getElementById("topBtn").style.display = "none";
        
        }
    }

    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

// Modal for policies    
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })
  $(function(){
    $('#closeModal').click(function(){
         $('#myModal').modal('hide');
     });
 });