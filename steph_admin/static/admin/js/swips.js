$(document).ready(function(){
  var clone_menu = $('#swips_menu').clone();
  clone_menu.appendTo('#grp-navigation');

});
$(function() {

    var href = $(location).attr('href');
    if(href.includes('feeds/')){
      console.log($.urlParam('language_cd'));
      var filter_lang = $.urlParam('language_cd');
      var filter_sport = $.urlParam('sport');
      var filter_source = $.urlParam('source');
      console.log(filter_lang);
      if(filter_lang){
        console.log('working??');
        $('#language_cd_'+ filter_lang).button('toggle');
      }
      if(filter_sport){
        console.log('working??');
        $('#sport_'+ filter_sport).button('toggle');
      }
      if(filter_source){
        console.log('working??');
        $('#source_'+ filter_source.replace('.','_')).button('toggle');
      }
    }
});
$.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return decodeURI(results[1]) || 0;
    }
}
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
$('.curry-filter-btn').click(function(){
  var url = $(location).attr('href').split('?')[0];
  var data = $(this).attr('data');
  var toggle = $(this).attr('aria-pressed');
  var filter_lang = $.urlParam('language_cd');
  var filter_sport = $.urlParam('sport');
  var filter_source = $.urlParam('source');
  console.log('data='+filter_source);
  if(data.split('=')[0]=='language_cd'){
    if(toggle){
      filter_lang = null;
    }else{
      filter_lang = data.split('=')[1];
    }
  }
  if(data.split('=')[0]=='sport'){
    if(toggle){
      filter_sport = null;
    }else{
      filter_sport = data.split('=')[1];
    }
  }
  if(data.split('=')[0]=='source'){
    console.log('not working1?');
    if(toggle){
      console.log('not working?');
      filter_source = null;
    }else{
      filter_source = data.split('=')[1];
    }
  }
  params = new Array();
  if(filter_lang){
    params.push('language_cd='+filter_lang);
  }
  if(filter_sport){
    params.push('sport='+filter_sport);
  }
  if(filter_source){
    params.push('source='+filter_source);
  }
  url = url + '?' + params.join("&");
  console.log('url='+url);
  $(location).attr('href', url);
});

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
$('.edit_count_text').click(function(){
  var data_max = parseInt($(this).attr('data-max'));
  var data_now = 0;
  try {
    data_now = parseInt($(this).text());
    if(isNaN(data_now)){
      data_now = 0;
    }
  }
  catch(exception){
    data_now = 0;
  }

  var new_value = data_max==data_now?0:data_now+1;
  requestModel = new Object();
  requestModel.db_type = $(this).attr('data-db_type');
  requestModel.table = $(this).attr('data-table');
  requestModel.primary_key = $(this).attr('data-primary_key');
  requestModel.primary_value = $(this).attr('data-primary_value');
  requestModel.change_key = $(this).attr('data-change_key');
  requestModel.default_value = $(this).attr('data-default_value');
  requestModel.new_value = new_value;
  $(this).attr('id', requestModel.primary_key + requestModel.primary_value + requestModel.change_key);
  request_json = JSON.stringify(requestModel);
  $.ajax({
      type : "POST",
      url : "/steph_admin/one_value_change/",
      dataType : "json",
      data : request_json,

      error : function(){
          console.log('error');
          alert('서버오류 값 변경실패!!');
          $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.default_value);
          // location.reload();
      },
      success : function(data){
          console.log(data);
          // $('#f_add_'+data_id+"_"+following).remove();
          $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).attr('data-default_value', requestModel.new_value);
          $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.new_value);
          // location.reload();
          if(requestModel.table=='swips_qna'){
            location.reload();
          }
      }
  });
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
