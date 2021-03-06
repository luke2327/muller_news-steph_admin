$(document).ready(function(){
  var clone_menu = $('#swips_menu').clone();
  clone_menu.appendTo('#grp-navigation');

});
$(function() {

    var href = $(location).attr('href');
    if(href.includes('feeds/')
    || href.includes('curryfixturesinfo')
    || href.includes('currymajorfixtures')
    || href.includes('swipsqna')){
      console.log($.urlParam('language_cd'));
      var filter_lang = $.urlParam('language_cd');
      var filter_sport = $.urlParam('sport');
      var filter_source = $.urlParam('source');
      var filter_league = $.urlParam('league');
      var filter_del = $.urlParam('del_field');
      var filter_language = $.urlParam('language');
      console.log(filter_lang);
      if(filter_language){
        console.log('working??');
        $('#language_'+ filter_language).button('toggle');
      }
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
      if(filter_league){
        console.log('working??');
        $('#league_'+ filter_league.replace('.','_')).button('toggle');
      }
      if(filter_del){
        $('#del_'+ filter_del).button('toggle');
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
  var filter_language = $.urlParam('language');
  var filter_lang = $.urlParam('language_cd');
  var filter_sport = $.urlParam('sport');
  var filter_source = $.urlParam('source');
  var filter_league = $.urlParam('league');
  var filter_del = $.urlParam('del_field');
  if(data.split('=')[0]=='language'){
    if(toggle){
      filter_language = null;
    }else{
      filter_language = data.split('=')[1];
    }
  }
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
  if(data.split('=')[0]=='league'){
    if(toggle){
      filter_league = null;
    }else{
      filter_league = data.split('=')[1];
    }
  }
  if(data.split('=')[0]=='del'){
    if(toggle){
      filter_del = null;
    }else{
      filter_del = data.split('=')[1];
    }
  }
  params = new Array();
  if(filter_language){
    params.push('language='+filter_language);
  }
  if(filter_lang){
    params.push('language_cd='+filter_lang);
  }
  if(filter_sport){
    params.push('sport='+filter_sport);
  }
  if(filter_source){
    params.push('source='+filter_source);
  }
  if(filter_league){
    params.push('league='+filter_league);
  }
  if(filter_del){
    params.push('del_field='+filter_del);
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
  display: function(value, sourceData) {
   //display checklist as comma-separated values
   if(value=='None'){
     $(this).text('');
     $(this).addClass('editable-empty');
     $(this).attr('data-value',"");
   }
  },
  success: function(response, newValue) {
        var requestModel = new Object();
        requestModel.db_type = $(this).attr('data-db_type');
        requestModel.table = $(this).attr('data-table');
        requestModel.primary_key = $(this).attr('data-primary_key');
        requestModel.primary_value = $(this).attr('data-primary_value');
        requestModel.change_key = $(this).attr('data-change_key');
        requestModel.default_value = $(this).attr('data-default_value');
        requestModel.new_value = newValue;
        $(this).attr('id', requestModel.primary_key + requestModel.primary_value + requestModel.change_key);
        var new_id = $(this).attr('id');
        var request_json = JSON.stringify(requestModel);
        console.log('request_json');
        console.log(request_json);
        $.ajax({
            type : "POST",
            url : "/steph_admin/one_value_change/",
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
                console.log(data);
                // $('#f_add_'+data_id+"_"+following).remove();
                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).attr('data-default_value', requestModel.new_value);
                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.new_value);
                // location.reload();
                if(requestModel.table=='swips_qna'){
                  location.reload();
                }
                if(requestModel.table=="world_peace_por"){
                  var data_tournament = $('#' + new_id).attr('tournament');
                  var data_round = $('#' + new_id).attr('round');
                  console.log(data_tournament);
                  console.log(data_round);
                  requestModel = new Object();
                  requestModel.tournament = data_tournament;
                  requestModel.round = data_round;
                  request_json = JSON.stringify(requestModel);
                  $.ajax({
                      type : "POST",
                      url : "/steph_admin/best11/",
                      data : request_json,
                      error : function(){
                          console.log('error');
                          alert('생성이 안됐음');
                      },
                      success : function(data){
                          console.log(data);
                          if(data!='200'){
                            alert('생성이 안됐음');
                          }
                      }
                  });
                }
            }
        });
    }
});
$('.edit_pop_textarea').editable({
  type: 'textarea',
  pk: 1,
  placement: 'top',
  title: '변경할 값을 입력하세요..',
  display: function(value, sourceData) {
   //display checklist as comma-separated values
   if(value=='None'){
     $(this).text('');
     $(this).addClass('editable-empty');
     $(this).attr('data-value',"");
   }
  },
  success: function(response, newValue) {
        var requestModel = new Object();
        requestModel.db_type = $(this).attr('data-db_type');
        requestModel.table = $(this).attr('data-table');
        requestModel.primary_key = $(this).attr('data-primary_key');
        requestModel.primary_value = $(this).attr('data-primary_value');
        requestModel.change_key = $(this).attr('data-change_key');
        requestModel.default_value = $(this).attr('data-default_value');
        requestModel.new_value = newValue;
        $(this).attr('id', requestModel.primary_key + requestModel.primary_value + requestModel.change_key);
        var request_json = JSON.stringify(requestModel);
        console.log(request_json);
        $.ajax({
            type : "POST",
            url : "/steph_admin/one_value_change/",
            data : request_json,

            error : function(){
                console.log('error');
                alert('서버오류 값 변경실패!!');
                console.log(requestModel.primary_key + requestModel.primary_value + requestModel.change_key);

                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.default_value);
                // location.reload();
            },
            success : function(data){
                // $('#f_add_'+data_id+"_"+following).remove();
                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).attr('data-default_value', requestModel.new_value);
                $("#"+ requestModel.primary_key + requestModel.primary_value + requestModel.change_key).text(requestModel.new_value);
                // location.reload();
                if(requestModel.table=='swips_qna'){
                  location.reload();
                }
            }
        });
    }
});
$('.edit_count_btn').click(function(){
  var id = $(this).attr('id').replace("btn","");
  $('#'+id).click();
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
            // location.reload();
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
$(document).keydown(function (e) {
  if (e.keyCode == 13) {
    if($('#del_following').is(':visible')){
      console.log($('#del_following').is(':visible'));
      $('#btn_del_following').click();
    }
    if($('#send_push').is(':visible')){
      $('#btn_send_push').click();
    }
    if($('#add_following_modal').is(':visible')){
      $('#btn_following_add').click();
    }
    if($('#add_all_lineup').is(':visible')){
      $('#btn_add_lineup').click();
    }
  }
  if (e.keyCode == 27) {
    if($('#del_following').is(':visible')){
      $('#del_following').modal('hide');
    }
    if($('#send_push').is(':visible')){
      $('#send_push').modal('hide');
    }
    if($('#add_following_modal').is(':visible')){
      $('#add_following_modal').modal('hide');
    }
    if($('#add_all_lineup').is(':visible')){
      $('#add_all_lineup').modal('hide');
    }
  }
});
