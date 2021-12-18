
function erroeHand(jqXHR, exception){
  if (jqXHR.status === 0) {
    alert('НЕ подключен к интернету!');
  } else if (jqXHR.status == 404) {
    alert('НЕ найдена страница запроса [404])');
  } else if (jqXHR.status == 500) {
    alert('НЕ найден домен в запросе [500].');
  } else if (exception === 'parsererror') {
    alert("Ошибка в коде: \n"+jqXHR.responseText);
  } else if (exception === 'timeout') {
    alert('Не ответил на запрос.');
  } else if (exception === 'abort') {
    alert('Прерван запрос Ajax.');
  } else {
    alert('Неизвестная ошибка:\n' + jqXHR.responseText);
  }
}

function sendId(gname) {
  console.log("123321123321");
  $.ajax({
      url: '/startId',
      method: 'post',
      dataType: 'json',
      data: {'gName': gname},
      error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
      success: function(){
        console.log("Successful sendId");
        window.location.reload();
      }
  });
};

function send(){
  console.log("qwe123qwe123qwe");
  $.ajax({
    url: '/start',
    method: 'post',
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(){
      console.log("Successful send");
      window.location.reload();
    }
  });
}

function removeGroup(gname){
  console.log("qweqweqweqwe");
  $.ajax({
    url: '/removeGroup',
    method: 'post',
    data: {'gName': gname},
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(){
      console.log("Successful delete");
      window.location.reload();
    }
  });
};

function addGroup() {
  $.ajax({
    url: '/addGroup',
    type: 'post',
    dataType: "html",
    data: $("#ajax_form").serialize(),
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(response) {
      console.log("Successful send");
      window.location.reload();
    },
 });
};

function addPayDay() {
  $.ajax({
    url: '/addPayDay',
    type: 'post',
    dataType: "html",
    data: $("#ajax_form2").serialize(),
    error: function (jqXHR, exception){erroeHand(jqXHR, exception)},
    success: function(response) {
      console.log("Successful send");
      window.location.reload();
    },
 });
};

function openWin(gName, money, payDay){
  $('.popup-fade').fadeIn();
  document.getElementById("gName").value = gName;
  document.getElementById("payDay").value = payDay;
  document.getElementById("money").value = money;
};

$( document ).ready(function() {
  // popup1
  $('.popup-open').click(function() {
  $('.popup-fade').fadeIn();
    return false;
  });
  $('.popup-close').click(function() {
    $(this).parents('.popup-fade').fadeOut();
    return false;
  });
  $('.popup-fade').click(function(e) {
    if ($(e.target).closest('.popup').length == 0) {
      $(this).fadeOut();
    }
  });
  // popup2
  $("#btn2").click(function(){addPayDay();});
  $('.popup-open2').click(function() {
  $('.popup-fade2').fadeIn();
    return false;
  });
  $('.popup-close2').click(function() {
    $(this).parents('.popup-fade2').fadeOut();
    return false;
  });
  $('.popup-fade2').click(function(e) {
    if ($(e.target).closest('.popup2').length == 0) {
      $(this).fadeOut();
    }
  });
});
