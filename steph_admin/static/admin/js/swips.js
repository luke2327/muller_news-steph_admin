$(document).ready(function(){
  var clone_menu = $('#swips_menu').clone();
  clone_menu.appendTo('#grp-navigation');
  console.log('go');
});

$('#grp-content').ready(function(){
  $('#grp-content').css({top: 0});
});
$('#grp-header').ready(function(){
  $('#grp-header').css({'position':'relative'});
});
$('.field-title_').ready(function(){
  $('.field-title_').css({'max-width':'150px'});
  $('.field-title_').children().css({'width':'130px'});
});
$('.field-following_desc_').ready(function(){
  $('.field-following_desc_').css({'max-width':'150px'});
  $('.field-following_desc_').children().css({'width':'130px'});
});

// $('#grp-content').attrchange({
//     trackValues: true, /* Default to false, if set to true the event object is
//                 updated with old and new value.*/
//     callback: function (event) {
//       // $('#grp-navigation').attr('position','relative');
//       $('#grp-content').attr('top','0px');
//       // console.log('go');
//       // console.log($('#grp-navigation').attr('position'));
//       // console.log($('#grp-content').attr('position'));
//     }
// });

var db_type;
var table;
var primary_key;
var primary_value;
var change_key;
var default_value;
$('.edit_pop_text').editable({
  type: 'text',
  pk: 1,
  placement: 'top',
  title: '변경할 값을 입력하세요..',
  success: function(response, newValue) {
        requestModel = new Object();
        requestModel.db_type = $(this).attr('data-db_type');
        requestModel.table = $(this).attr('data-table');
        requestModel.primary_key = $(this).attr('data-primary_key');
        requestModel.primary_value = $(this).attr('data-primary_value');
        requestModel.change_key = $(this).attr('data-change_key');
        requestModel.default_value = $(this).attr('data-default_value');
        requestModel.new_value = newValue;
        $(this).attr('id', requestModel.primary_key + requestModel.primary_value + requestModel.change_key);
        request_json = JSON.stringify(requestModel);
        console.log(request_json);
        $.ajax({
            type : "POST",
            url : "/steph_admin/one_value_change/",
            dataType : "json",
            data : request_json,

            error : function(){
                console.log('error');
                alert('서버오류 값 변경실패!!');
                console.log(requestModel.primary_key + requestModel.primary_value + requestModel.change_key);

                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.default_value);
                // location.reload();
            },
            success : function(data){
                //alert("통신데이터 값 : " + data) ;
                alert('성공!!');
                console.log(data);
                // $('#f_add_'+data_id+"_"+following).remove();
                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).attr('data-default_value', requestModel.new_value);
                // location.reload();
                if(requestModel.table=='swips_qna'){
                  location.reload();
                }
            }
        });
    }
});

$('.edit_pop_select').editable({
  type: 'text',
  pk: 1,
  placement: 'top',
  title: 'Enter username',
  success: function(response, newValue) {
        requestModel = new Object();
        requestModel.db_type = $(this).attr('data-db_type');
        requestModel.table = $(this).attr('data-table');
        requestModel.primary_key = $(this).attr('data-primary_key');
        requestModel.primary_value = $(this).attr('data-primary_value');
        requestModel.change_key = $(this).attr('data-change_key');
        requestModel.default_value = $(this).attr('data-default_value');
        requestModel.new_value = newValue;
        request_json = JSON.stringify(requestModel);
        console.log(request_json);
        $.ajax({
            type : "POST",
            url : "/steph_admin/one_value_change/",
            dataType : "json",
            data : request_json,

            error : function(){
                console.log('error');
                alert('서버오류 값 변경실패!!');
                $(this).val($(this).attr('data-primary_value'));
            },
            success : function(data){
                //alert("통신데이터 값 : " + data) ;
                // alert('라인업 추가성공!!');
                // console.log(data);
                // $('#f_add_'+data_id+"_"+following).remove();
                $('#btn_add_lineup').button('reset');
                $('#add_all_lineup').modal('hide');
                // location.reload();
            }
        });
    }
});
