function readURL(input,tag) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $("#" + tag).attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }


  $("#imgInp1").change(function() {
    readURL(this,'blah1');
  });

  $("#imgInp2").change(function() {
    readURL(this,'blah2');
  });
