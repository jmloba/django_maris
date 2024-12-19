$(document).ready(function(){

  $('#btn-print-task').click(function(e){
    e.preventDefault();
    console.log (' pressed print task')
    let url= $(this).attr('data-url');
    
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    mydata= {
     
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      method :'POST',
      success:function(response){
        if (response.status=='Success'){
          swal(response.status,response.Message,'success')
        }
        if (response.status=='no') {
          swal(response.status,response.Message,'warning')

        }
      }


    })  


  })

})