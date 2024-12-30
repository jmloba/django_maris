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


  function html_record_Task(x)  {
    html_template=''
    for ( i=0; i < x.length; i++ ){
      html_template +=
      '<tr id="task-id-'+x[i].id+'"><td data-cell="Owner">'+x[i].owner+'</td><td data-cell="Name">'+x[i].name+'</td><td data-cell="Task Date">'+x[i].task_date+'</td><td data-cell="Start time">'+x[i].start_time+'</td><td data-cell="End time">'+x[i].end_time+'</td><td><a href="/app_query/updateDelete-modal2/'+x[i].id+'" class="Task-link-delete text-danger" >Delete</a></td><td><a href="/app_query/updateDelete-modal2/'+x[i].id+'" class="Task-link-update text-danger"    data-date  = "'+x[i].task_date+'"  data-start  = "'+x[i].start_time+'"   data-end  = "'+x[i].end_time+'"  data-stuid = "'+x[i].id+'">Edit</a></td></tr>'

    }    
    return html_template
  };

  $('#btn-save-add-task').click(function(e){
    e.preventDefault();  
    console.log('add button task')
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    let owner = $('#id_owner').val()  
    let name = $('#id_name').val()  
    let task_date = $('#id_task_date').val()  
    let start_time = $('#id_start_time').val()  
    let end_time = $('#id_end_time').val()  
    let url= $(this).attr('data-url');  
    let id = $('#stuid').val()  

    console.log ('saving the value of id :',id)

    mydata={
      'owner':owner,
      'name':name,
      'id':id,
      'task_date':task_date,
      'start_time': start_time,
      'end_time': end_time,
      'csrfmiddlewaretoken': csrf_token,

    }
   
    console.log ('name', name, 'id:',id)

      
      $.ajax({
        url: url,
        method : 'POST',
        data : mydata,

        success: function(data){  
          x= data.datalist
          console.log('** success -->> name : ', x)
          html_template=''
          if (data.status=='Success'){
            console.log('sving success')
            html_template=html_record_Task(x)
            $('#query-classroom .table-body').html(html_template)


            $('#Task-table-modal #task-form')[0].reset()
            // swal('Data has been Saved','Record has been saved','success')
            console.log('returned record ',x)
            $("#Task-table-modal").modal("hide");
            // clear_data_entries()
          }
        }
      });        

  })


  $('#btn-update-delete-task').click(function(e){
    e.preventDefault(); 
    console.log('update delete task modal edit')
  })

  
  // click delete link
  $('#query-classroom main.table .table-body').on("click",".Task-link-delete",function(e){
    e.preventDefault()
        console.log ('delete - link')
    var  $this = $(this)
    if (confirm('Are you sure you want to delete this record')){
      $.ajax({
        url :  $this.attr("href"),
        type : 'GET',
        dataType : 'json',
        success : function(response){
          if (response.message='success'){
            x= response.data_list
            html_template=html_record_Task(x)
            $('#query-classroom .table-body').html(html_template)
            swal('Data has been Deleted','Record has been deleted','success')

          }

        },
        error : function(response){
          console.log('something went wrong ...')

        },



      })

    }

    
    

    return false

  })
  // click update link
  $('#query-classroom main.table .table-body').on("click",".Task-link-update",function(e){
    e.preventDefault()
    var $this = $(this);
    console.log ('update - link')
    let owner = $this.parents("tr").find('td').eq(0).text();
    let name = $this.parents("tr").find('td').eq(1).text();

    let taskDate = $this.data('date')
    let startTime = $this.data('start');
    let endTime = $this.data('end');
    
    let id = $(this).attr("data-stuid" ) 
   

    console.log('owner:', owner, "name:",name,'task_date:', taskDate, 'start_time : ',startTime,'end_time:', endTime, 'stuid: ',id )

    $("#Task-table-edit-modal input[name='owner' ] ").val(owner)
    $("#Task-table-edit-modal input[name='name' ] ").val(name)
    
    $("#Task-table-edit-modal input[name='task_date' ] ").val(taskDate)

    $("#Task-table-edit-modal input[name='start_time' ] ").val(startTime)

    $("#Task-table-edit-modal input[name='end_time' ] ").val(endTime)
    $("#Task-table-edit-modal input[name='stuid' ] ").val(id);    
    // replace ation with href
    $("#Task-table-edit-modal #task-form").attr('action',$this.attr('href'));
    
    // // replace heading of modal
  
    $('#Task-table-edit-modal').modal("show");
    return false
  })


  // click submit button on Task-table-edit-modal
  $('#Task-table-edit-modal #task-form' ).on("submit",function(e){
    e.preventDefault()
    e.stopPropagation()
    var $this = $(this);
    var valid = true;
    $('#Task-table-edit-modal #task-form input').each(function() {
      let $this = $(this);

      if (!$this.val()){
        valid = false;
        $this.parents('.validate').find('.myspan').text('The '+$this.attr('name').replace(/[\_]+/g,' ')+' this field is required')
      }
    });
    if (valid){
      console.log ('after validating entries' )

      let data = $this.serialize();
      console.log ('valid: \n','data :', data)
      $.ajax({
        url  : $this.attr("action"), 
        type :"POST",
        data : data,
        dataType :"json",
        success : function(data){
          x= data.data_list


          console.log('** success -->> name : ', x)
          if (data.message==='success'){



            html_template=html_record_Task(x)
            $('#query-classroom .table-body').html(html_template)
            $('#Task-table-edit-modal #task-form')[0].reset()
            
            $("#Task-table-edit-modal").modal("hide");
            swal('Data has been Saved','Record has been saved','success')

          }
          else{
            alert(response.message)
          }

        },
        error: function(response){
          console.log ('something went wrong')
        }

      })

    } else     {
      console.log ('invalid fields')

    }


    console.log ('update modal submit clicked')
  });      
});  
