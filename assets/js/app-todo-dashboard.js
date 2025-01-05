
$(document).ready(function(){
  
  function html_record_Todo(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
      html_template +=
    
      '<tr id="task-id-'+x[i].id+'"><td data-cell="title">'+x[i].title+'</td><td data-cell="completed">'+x[i].completed+'</td></tr>'
  
    }    
    return html_template
  };

  $('#btn-save-add-todo').click(function(e){
    e.preventDefault();  
    console.log(' button save todo')
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    let title = $('#id_title').val()  
    let url= $(this).attr('data-url');  
    mydata={
      'title' :title,
      'csrfmiddlewaretoken': csrf_token,
    }
    $.ajax({
      url: url,
      method : 'POST',
      data : mydata,
      success : function(data){
        x= data.datalist
        if (data.status=='success'){
          html_template=html_record_Todo(x)
          $('#todo-dashboard .table-body').html(html_template)
          $('#Todo-table-modal #todo-form')[0].reset()
          $("#Todo-table-modal").modal("hide");
         swal('Data has been Saved',data.message,'success')          
        } else { 
          console.log(data.message)
        }       

      },
      error : function(data) {
        if (data.status=='failed'){
          console.log(data.message)

        }
      }


    })  

    
  })

})
