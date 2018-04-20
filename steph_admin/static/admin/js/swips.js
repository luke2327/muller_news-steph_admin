$(document).ready(function(){
  var clone_menu = $('#swips_menu').clone();
  clone_menu.appendTo('#grp-navigation');

});

$('#grp-content').ready(function(){
  $('#grp-content').css({top: 0});
});
$('#grp-header').ready(function(){
  $('#grp-header').css({'position':'relative'});
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
