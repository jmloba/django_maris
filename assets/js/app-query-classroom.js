
$(document).ready(function(){
  

  $("#btn-hide-all").click(function(e){
    e.preventDefault();
    console.log('sss')
    $(".table-area").hide();
  });
  $("#btn-show-all").click(function(e){
    e.preventDefault();
    console.log('sss')
    $(".table-area").show();
  });  

  function html_record(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
      html_template +=  
 

      '<tr id="task-id-'+x[i].id+'"><td data-cell="Name">'+x[i].name+'</td><td><button class="btn btn-danger btn-sm"><a href="/app_query/UpdateDeleteTeacher-ajax/'+x[i].id+'/" class="teacher-link-delete" data-id = '+x[i].id+'><i class="bi bi-trash3"></i></a></button></td><td><button class="btn btn-info btn-sm"><a href="/app_query/UpdateDeleteTeacher-ajax/'+x[i].id+'/" class="teacher-link-update" ><i class="bi bi-pencil"></i></a></button></td></tr>'

    }    
    return html_template
  };

  // $('#edit-teacher-form').click(function(e){
  //   e.preventDefault();  
  //   console.log('edit teacher')
  //   let csrf_token = $('input[name=csrfmiddlewaretoken]').val()

  //   let name = $('#id_name').val()  
  //   let url= $(this).attr('data-url');  
  //   let id = $('#stuid').val()  

  //   mydata={'name':name,
  //     'id':id,
  //     'csrfmiddlewaretoken': csrf_token,

  //   }
   
  //   console.log ('name', name, 'id:',id)
  //   if (name==''){
  //     swal("Please enter Teacher's Name",'Name is required ','error')
  //   }
  //   else {
  //     console.log('no error')
      
  //     $.ajax({
  //       url: url,
  //       method : 'POST',
  //       data : mydata,

  //       success: function(data){  
  //         x= data.datalist
  //         console.log('** success -->> name : ', x)
  //         html_template=''


  //         if (data.status=='Success'){
  //           html_template=html_record(x)
  //           $('.table-body.teacher-tbody').html(html_template)

  //           $('#teacher-form')[0].reset()

  //           swal('Data has been Saved','Record has been saved','success')
  //           console.log('returned record ',x)
  //           $("#add-teacher-form").modal("hide");
            


  //           // clear_data_entries()
  //         }
  //       }
  //     });        


  //   }  

  // });         

  $('#btn-save-add-teacher').click(function(e){
    e.preventDefault();  
    console.log('add button teacher')
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    let name = $('#id_name').val()  
    let url= $(this).attr('data-url');  
    let id = $('#stuid').val()  

    mydata={'name':name,
      'id':id,
      'csrfmiddlewaretoken': csrf_token,

    }
   
    console.log ('name', name, 'id:',id)
    if (name==''){
      swal("Please enter Teacher's Name",'Name is required ','error')
    }
    else {
      console.log('no error')
      
      $.ajax({
        url: url,
        method : 'POST',
        data : mydata,

        success: function(data){  
          x= data.datalist
          console.log('** success -->> name : ', x)
          html_template=''
          if (data.status=='Success'){
            html_template=html_record(x)
            $('.table-body.teacher-tbody').html(html_template)
            $('#teacher-form')[0].reset()
            swal('Data has been Saved','Record has been saved','success')
            console.log('returned record ',x)
            $("#add-teacher-modal").modal("hide");
            // clear_data_entries()
          }
        }
      });        
    }  
  })
  



  


})
